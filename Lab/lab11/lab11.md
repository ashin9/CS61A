## Interpreters

解释器（Interpreter）是一个允许你通过某种语言与计算机交互的程序。它理解你用这种语言输入的表达式，并以某种方式执行相应的操作，通常是使用底层的其他语言来实现这些功能。

在 Project 4 中，你将使用 Python 实现一个 Scheme 的解释器。而你整个学期一直在使用的 Python 解释器，大部分是用 C 语言写的。计算机本身则使用硬件来解释机器码（machine code），即由一串 0 和 1 组成的基本操作指令，比如加法运算、从内存加载数据等等。

当我们讨论解释器时，通常涉及两种语言：

1. **被解释/实现的语言**
    在这个实验（lab）中，你将实现的是 PyCombinator 语言。
2. **底层实现语言**
    在这个实验中，你会用 Python 来实现 PyCombinator 语言。

需要注意的是，**底层语言和实现的语言并不一定要不同**。实际上，在这个实验中，我们就是用 Python 实现一个小型的 Python（PyCombinator）！这种想法被称为 **元循环解释（Metacircular Evaluation）**。

------

很多解释器都会使用 **REPL（Read-Eval-Print Loop）**，也就是 **读-求值-打印-循环**。这个循环的工作流程通常是：

### 1. Read（读取）

解释器接收用户输入（一个字符串），然后通过词法分析器（lexer）和语法分析器（parser）进行处理。

- **Lexer（词法分析器）** 会把用户输入的字符串转化为原子片段（tokens），这些 tokens 类似于语言的“单词”。
- **Parser（语法分析器）** 会接收这些 tokens，并把它们组织成数据结构（通常是抽象语法树，AST），供底层实现语言（这里是 Python）理解和操作。

### 2. Eval（求值）

通过 eval 和 apply 的相互递归来求值表达式，并得到一个值。

- `eval` 负责根据语言的规则去计算表达式的值。
- 如果表达式是一个函数调用，`eval` 会调用 `apply`，传入操作符和参数。

### 3. Print（打印）

把 `eval` 得到的结果展示给用户。

------

下面是整个流程的图示：

```pgsql
         +-------------------------------- Loop -----------+
         |                                                 |
         |  +-------+   +--------+   +-------+   +-------+ |
Input ---+->| Lexer |-->| Parser |-->| Eval  |-->| Print |-+--> Output
         |  +-------+   +--------+   +-------+   +-------+ |
         |                              ^  |               |
         |                              |  v               |
         ^                           +-------+             v
         |                           | Apply |             |
         |    REPL                   +-------+             |
         +-------------------------------------------------+
```

------

- `eval`：负责解释和计算表达式，根据语言的规则处理。
   例如，当 `eval` 遇到一个函数调用表达式时，它会：
  1. 计算出操作符（operator）。
  2. 计算出参数（operands）。
  3. 然后调用 `apply` 去执行函数。
- `apply`：拿到 `eval` 已经计算好的函数和参数后，去“应用”它们，也就是说真正调用函数。
   在执行函数体的时候，`apply` 可能还需要调用 `eval` 来处理函数内部的表达式。
   所以，`eval` 和 `apply` 会形成**互相递归**。

# Required Questions

## PyCombinator Interpreter

今天，我们将构建 **PyCombinator**——我们自己的基础版 Python 解释器！在本次实验结束时，你将能够使用一系列基本操作，例如 `add`、`mul` 和 `sub`。更令人兴奋的是，我们还能通过这个自制解释器创建和调用 `lambda` 函数！

你将实现一些关键部分，使解释器能够评估如下命令及更多操作：

```scss
> add(3, 4)
7
> mul(4, 5)
20
> sub(2, 3)
-1
> (lambda: 4)()
4
> (lambda x, y: add(y, x))(3, 5)
8
> (lambda x: lambda y: mul(x, y))(3)(4)
12
> (lambda f: f(0))(lambda x: pow(2, x))
1
```

------

你可以在 `repl.py` 文件中找到我们解释器的 **Read-Eval-Print Loop (REPL)** 代码。以下是 REPL 每个组成部分的概述：

------

### 1. **Read（读取）**

`reader.py` 中的 `read` 函数负责解析用户输入，它调用了以下两个函数：

- **词法分析（lexer）**
   由 `reader.py` 中的 `tokenize` 函数实现。
   它将用户输入的字符串拆分为**tokens**（标记）。
- **语法分析（parser）**
   由 `reader.py` 中的 `read_expr` 函数实现。
   它接收 tokens 并将其解析为表达式对象（`Expr` 的子类实例），例如 `CallExpr`。

------

### 2. **Eval（求值）**

表达式（`Expr` 对象）被计算求值，得到对应的值（`Value` 对象，同样在 `expr.py` 中定义）。

- 每种表达式类型都有自己的 `eval` 方法来进行求值。
- `CallExpr`（调用表达式）通过 `apply` 方法来应用操作符，并传入参数。
   对于 `lambda` 函数，`apply` 会调用 `eval` 来求值函数体。

------

### 3. **Print（打印）**

将求值得到的结果转换为字符串（调用 `__str__` 方法），并输出。

------

在这个实验中，你只需要实现 **`expr.py`** 中的 **Eval** 和 **Apply** 部分。

------

### 启动 PyCombinator 解释器

运行以下命令启动你的解释器：

```bash
python3 repl.py
```

你可以尝试输入一些值，比如一个字面量（例如 `4`），或者一个 `lambda` 表达式（例如 `lambda x, y: add(x, y)`），来观察它们的求值结果。

你还可以尝试输入一些名字（例如 `add`）。在 `expr.py` 文件的结尾部分，你可以看到当前 PyCombinator 中可以使用的所有名称列表。
 **注意**：PyCombinator 的基本运算符不是 `+`、`-`、`*`、`/`，而是 `add`、`sub` 等。

------

### 当前解释器状态

目前，任何名字（如 `add`）和调用表达式（如 `add(2, 3)`）都会输出 `None`。

 接下来，你的任务是实现 `Name.eval` 和 `CallExpr.eval`，使解释器能够查找名字并调用函数！

------

### 理解 `read` 过程（可选）

你不需要深入理解解释器的 `read` 部分如何实现。

但如果你想了解用户输入是如何被读取和转换成 Python 代码的，可以在运行解释器时加上 `--read` 标志：

```bash
$ python3 repl.py --read
> add
Name('add')
> 3
Literal(3)
> lambda x: mul(x, x)
LambdaExpr(['x'], CallExpr(Name('mul'), [Name('x'), Name('x')]))
> add(2, 3)
CallExpr(Name('add'), [Literal(2), Literal(3)])
```

------

### 退出解释器

按下 `Ctrl-C` 或 `Ctrl-D` 即可退出解释器。

------

### 你的任务

在这个实验中，你将主要在 `expr.py` 文件中编写代码，实现 `Eval` 和 `Apply` 的逻辑。



### Q1: Prologue

在我们开始编写任何代码之前，先来理解一下解释器中已经实现的部分。

以下是当前实现的结构分析：

------

### `repl.py`

包含 REPL 循环的逻辑。
 这个循环会不断执行以下操作：

- 读取用户输入的表达式
- 对表达式进行求值
- 打印求值后的结果

（你不需要完全理解这个文件中的所有代码）

------

### `reader.py`

包含解释器的读取器（Reader）。

 `read` 函数调用 `tokenize` 和 `read_expr` 函数，将输入的表达式字符串转换为 `Expr` 对象。（你也不需要完全理解这个文件中的所有代码）

------

### `expr.py`

包含解释器中表达式（`Expr`）和数值（`Value`）的表示。

- `Expr` 和 `Value` 的子类定义了 PyCombinator 语言中所有表达式和值的类型。
- 文件底部还定义了 **全局环境**（`global_env`），这是一个包含所有原始函数（如 `add`、`mul` 等）绑定的字典。

------

### 接下来的任务

#### 使用 `Ok` 工具来测试你对 Reader 的理解

你可以参考 `reader.py` 文件来回答相关问题。运行以下命令：

```
python3 ok -q prologue_reader -u
```



```shell
➜  lab11 py3 ok -q prologue_reader -u
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 1
(cases remaining: 10)

Q: What does REPL stand for?
Choose the number of the correct choice:
0) Really-Enormous-Purple-Llamas
1) Read-Eval-Parse-Lex
2) Read-Eval-Print-Loop
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 2
(cases remaining: 9)

Q: What does the read component of the REPL loop do?
Choose the number of the correct choice:
0) Ensures a function has been defined before it is called
1) Turns input into a useful data structure
2) Turns input into tokens
3) Evaluates call expressions
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Ensures a function has been defined before it is called
1) Turns input into a useful data structure
2) Turns input into tokens
3) Evaluates call expressions
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 3
(cases remaining: 8)

Q: What does the tokenize function in reader.py return?
Choose the number of the correct choice:
0) Input expression represented as an instance of a subclass of Expr
1) Input expression represented as a list of tokens
2) Result of evaluating the input expression
3) Input expression with corrected number of parentheses
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 4
(cases remaining: 7)

# 数字没有 ''
Q: What will tokenize('add(3, 4)') output?
Choose the number of the correct choice:
0) ['a', 'd', 'd', '(', '3', ',', '4', ')']
1) ['a', 'd', 'd', '(', 3, ',', 4, ')']
2) ['add', '(', 3, ',', 4, ')']
3) ['add', '(', '3', ',', '4', ')']
? 3
-- Not quite. Try again! --

Choose the number of the correct choice:
0) ['a', 'd', 'd', '(', '3', ',', '4', ')']
1) ['a', 'd', 'd', '(', 3, ',', 4, ')']
2) ['add', '(', 3, ',', 4, ')']
3) ['add', '(', '3', ',', '4', ')']
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 5
(cases remaining: 6)

Q: What will tokenize('(lambda: 4)()') output?
Choose the number of the correct choice:
0) ['(', 'lambda', ':', 4, ')', '(', ')']
1) ['(', LambdaExpr, ':', 4, ')', '(', ')']
2) ['(', LambdaExpr, 4, ')', '(', ')']
3) ['lambda', 4, '(', ')']
? 0
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 6
(cases remaining: 5)

Q: What does the read_expr function in reader.py accept as input and
return?  (looking at the read function may help answer this question)
Choose the number of the correct choice:
0) List of tokens and number of parentheses
1) List of tokens and an instance of a subclass of Expr
2) Input expression and an instance of a subclass of Expr
3) Input expression and list of tokens
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 7
(cases remaining: 4)

Q: What does the read function in reader.py return?
Choose the number of the correct choice:
0) Result of evaluating the input expression
1) Input expression represented as an instance of a subclass of Expr
2) Input expression with corrected number of parentheses
3) Input expression represented as a list of tokens
? 1
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 8
(cases remaining: 3)

# 数字是用 Literal
Q: What will read('1') output?
Choose the number of the correct choice:
0) Name(1)
1) Number(1)
2) Literal(1)
3) Name('1')
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Name(1)
1) Number(1)
2) Literal(1)
3) Name('1')
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 9
(cases remaining: 2)

# 字母有 ''
Q: What will read('x') output?
Choose the number of the correct choice:
0) Name('x')
1) Name(x)
2) x
3) Literal(x)
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Name('x')
1) Name(x)
2) x
3) Literal(x)
? 0
-- OK! --

---------------------------------------------------------------------
Prologue - Reader > Suite 1 > Case 10
(cases remaining: 1)

# 为什么是 [] 中？由于调用表达式可以有多个操作数，`operands` 是一个 `Expr` 实例的列表。
Q: What will read('add(3, 4)') output?
Choose the number of the correct choice:
0) CallExpr(Literal('add'), Literal(3), Literal(4))
1) CallExpr(Name('add'), [Literal(3), Literal(4)])
2) CallExpr('add', [Literal(3), Literal(4)])
3) CallExpr(Name('add'), Literal(3), Literal(4))
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Prologue - Reader unlocked.

Performing authentication
Please enter your school email (.edu): ^C%  
```





#### 使用 `Ok` 工具来测试你对 `Expr` 和 `Value` 对象的理解

你可以参考 `expr.py` 文件来回答相关问题。运行以下命令：

```
python3 ok -q prologue_expr -u
```



```shell
➜  lab11 py3 ok -q prologue_expr -u
=====================================================================
Assignment: Lab 11
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 1
(cases remaining: 6)

Q: What are all the types of expressions in PyCombinator?
Choose the number of the correct choice:
0) name, function, number, literal
1) number, lambda function, primitive function, string
2) literal, name, call expression, lambda expression
3) value, expression, function, number
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 2
(cases remaining: 5)

Q: What are all the types of values in PyCombinator?
Choose the number of the correct choice:
0) number, lambda expression, primitive function
1) number, string, function
2) name, number, lambda function
3) number, lambda function, primitive function
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) number, lambda expression, primitive function
1) number, string, function
2) name, number, lambda function
3) number, lambda function, primitive function
? 3
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 3
(cases remaining: 4)

Q: What does a Literal evaluate to?
Choose the number of the correct choice:
0) a Function
1) an Expression
2) a Number
3) a String
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 4
(cases remaining: 3)

Q: What is the difference between a lambda expression and a lambda function?
Choose the number of the correct choice:
0) A lambda function is the result of evaluating a lambda expression
1) They are the same thing
2) A lambda expression is a call to a lambda function
3) A lambda expression is the result of evaluating a lambda function
? 0
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 5
(cases remaining: 2)

Q: Which of the following describes the eval method?
Choose the number of the correct choice:
0) A method of Expr objects that evaluates a call expression and returns a Number
1) A method of Literal objects that returns a Name
2) A method of Expr objects that evaluates the Expr and returns a Value
3) A method of LambdaExpression objects that evaluates a function call
? 2
-- OK! --

---------------------------------------------------------------------
Prologue - Expr > Suite 1 > Case 6
(cases remaining: 1)

Q: How are environments represented in our interpreter?
Choose the number of the correct choice:
0) As dictionaries that map Name objects to Value objects
1) As sequences of Frame objects
2) As dictionaries that map variable names to Value objects
3) As linked lists containing dictionaries
? 2
-- OK! --

---------------------------------------------------------------------
OK! All cases for Prologue - Expr unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



### Q2: Evaluating Names ✅

我们要评估的第一种 PyCombinator 表达式是 **名字（Name）**。在我们的程序中，一个名字是 `Name` 类的一个实例。每个实例都有一个 `var_name` 属性，这个属性表示变量的名字 —— 例如 `"x"`。

回忆一下，一个名字的值依赖于当前的环境（environment）。在我们的实现中，环境被表示为一个字典（dictionary），这个字典将变量名（字符串）映射到它们的值（`Value` 类的实例）。

`Name.eval` 方法接收当前环境作为参数 `env`，返回当前 `Name` 对象的 `var_name` 在该环境中绑定的值。具体实现如下：

- 如果名字存在于当前环境中，就查找它并返回其绑定的值。
- 如果名字不存在于当前环境中，就返回 `None`。

你需要在 `expr.py` 文件中添加这段代码。

```
def eval(self, env):
    """
    >>> env = {
    ...     'a': Number(1),
    ...     'b': LambdaFunction([], Literal(0), {})
    ... }
    >>> Name('a').eval(env)
    Number(1)
    >>> Name('b').eval(env)
    LambdaFunction([], Literal(0), {})
    >>> print(Name('c').eval(env))
    None
    """
    "*** YOUR CODE HERE ***"
```

------

使用 Ok 测试你的代码是否正确：

```
python3 ok -q Name.eval
```

------

现在你已经实现了名字的求值操作，你可以在全局环境中查找 `add` 和 `sub` 等名字（可以查看 `expr.py` 文件底部 `global_env` 中的完整数学运算符列表）。你也可以尝试查找未定义的名字，看看 `NameError` 是如何显示的！

```
$ python3 repl.py
> add
<primitive function add>
```

不幸的是，你现在还无法调用这些函数。接下来我们就来修复这个问题！



### Q3: Evaluating Call Expressions ✅

现在，让我们为 **调用表达式（call expressions）** 添加求值逻辑，比如 `add(2, 3)`。记住，一个调用表达式由一个 **操作符（operator）** 和零个或多个 **操作数（operands）** 组成。

在我们的实现中，一个调用表达式通过 `CallExpr` 实例表示。每个 `CallExpr` 类的实例都有两个属性：`operator` 和 `operands`。`operator` 是一个 `Expr` 实例，而由于调用表达式可以有多个操作数，`operands` 是一个 `Expr` 实例的列表。

例如，在表示 `add(3, 4)` 的 `CallExpr` 实例中：

- `self.operator` 会是 `Name('add')`
- `self.operands` 会是列表 `[Literal(3), Literal(4)]`

------

在 `CallExpr.eval` 方法中，实现以下三个步骤来对一个调用表达式求值：

1. 在当前环境 `env` 中对 `operator` 求值。
2. 在当前环境 `env` 中对所有 `operand` 求值。
3. 将 `operator` 的值（是一个函数）应用于 `operand` 的值。

**提示**：由于 `operator` 和 `operands` 都是 `Expr` 的实例，你可以通过调用它们的 `eval` 方法来对它们求值。而且，一个函数（`PrimitiveFunction` 或 `LambdaFunction` 的实例）可以通过调用它的 `apply` 方法来应用，它接收一个参数列表（`Value` 实例的列表）。



# Optional Questions

### Q4: Applying Lambda Functions ✅

我们现在已经可以做一些基础的数学运算了，但如果还能调用我们自己定义的函数，会更有趣一些！所以接下来，我们要确保可以做到这一点。

在 PyCombinator 中，一个 **lambda 函数** 表示为 `LambdaFunction` 类的一个实例。如果你查看 `LambdaFunction.__init__` 方法，会发现每个 lambda 函数都有三个实例属性：`parameters`、`body` 和 `parent`。举个例子，考虑如下这个 lambda 函数：

```
lambda f, x: f(x)
```

对应的 `LambdaFunction` 实例有以下属性：

- `parameters` —— 一个字符串列表，例如 `['f', 'x']`
- `body` —— 一个 `Expr` 表达式，例如 `CallExpr(Name('f'), [Name('x')])`
- `parent` —— 父环境，用于查找变量的环境。注意，这个环境是定义该 lambda 函数时的环境。`LambdaFunctions` 是在 `LambdaExpr.eval` 方法中创建的，这时候的当前环境会成为该 `LambdaFunction` 的 `parent` 环境。

------

如果你现在尝试在解释器里输入一个 lambda 表达式，你应该会看到它输出了一个 `lambda` 函数。不过，如果你试图调用这个 lambda 函数，比如：

```
(lambda x: x)(3)
```

它会返回 `None`。这是因为我们还没有实现 `LambdaFunction` 的 `apply` 方法。

------

现在，我们来实现 `LambdaFunction.apply` 方法，这样就可以调用我们自己定义的 lambda 函数啦！

这个方法接收一个 `arguments` 列表，它包含传递给函数的实参（`Value` 实例）。在对 lambda 函数求值时，我们需要确保它的形式参数（`parameters`）正确地绑定到了传入的实参（`arguments`）。要做到这一点，我们需要修改对函数体求值时使用的环境。

------

应用一个 `LambdaFunction` 有三个主要步骤：

1. **复制 parent 环境**
    你可以使用 `d.copy()` 方法对字典 `d` 进行复制。
2. **将参数和实参绑定**
    在环境副本上调用 `update` 方法，把 `parameters`（参数名）和 `arguments`（对应值）绑定起来。
    （你可以使用 Python 的 `zip` 函数将它们配对）
3. **用新的环境求值函数体**
    使用刚创建的新环境来对 `body` 求值。



### Q5: Handling Exceptions ✅

到目前为止，我们实现的解释器看起来已经很酷了，好像一切正常，对吧？但其实，还有一种情况我们还没有处理。你能想到一个非常简单但没有定义的计算吗？（也许和除法有关？）试试看，如果你用解释器去计算这个操作（比如用 `floordiv` 或 `truediv`，因为 PyCombinator 没有标准的 `div` 运算符），会发生什么？

是不是有点丑？我们得到了一个冗长的错误信息，解释器直接退出了。可实际上，我们更希望优雅地处理这些错误，而不是程序直接崩溃。

------

再打开你的解释器，试试做一些非法操作，比如：

```
add(3, x)
```

这时候，解释器会给你一个友好的错误信息，提示 `x` 没有定义，但程序依然能够继续运行。这是因为代码中已经处理了 `NameError` 异常，防止它让程序崩溃。

------

接下来聊聊 **如何处理异常**：

在课堂上你学过如何抛出异常（raise exceptions），但同样重要的是学会在必要时 **捕获异常**。我们不想让异常一直传递到用户界面导致程序崩溃，而是可以通过 `try/except` 块捕获异常，让程序继续执行。

```
try:
    <try 块代码>
except <异常类型0> as e:
    <处理异常0的代码>
except <异常类型1> as e:
    <处理异常1的代码>
...
```

把可能产生异常的代码写进 `try` 块。如果程序在 `try` 块里抛出了异常，解释器就会寻找对应类型的 `except` 块进行处理。你可以写多个 `except` 块，处理不同的异常。

来看个简单的例子：

```
try:
    1 + 'hello'
except NameError as e:
    print('hi')  # 处理 NameError 的代码
except TypeError as e:
    print('bye') # 处理 TypeError 的代码
```

上面例子里，`1 + 'hello'` 会抛出 `TypeError`，所以程序会跳转到第二个 `except` 块执行，打印 `bye`。

------

一般来说，我们应该**只捕获特定的异常类型，比如 `OverflowError`、`ZeroDivisionError`（或者两者一起），而不是笼统地捕获所有异常。这样做可以避免不小心屏蔽了程序中别的 bug。**

------

另外，注意 `except` 块里 `as e` 的用法。`e` 是异常对象，你可以从中获取更多的异常信息：

```
>>> try:
...     x = int("cs61a rocks!")
... except ValueError as e:
...     print('Oops! That was no valid number.')
...     print('Error message:', e)
```

输出：

```
Oops! That was no valid number.
Error message: invalid literal for int() with base 10: 'cs61a rocks!'
```

------

你可以在解释器的 `repl.py` 文件中看到类似的异常处理逻辑。接下来的任务是修改 `repl.py`，让它也能优雅地处理「非法算术运算错误」以及「类型错误」。

快去试试看吧！优化你的解释器，让它遇到 `ZeroDivisionError`、`OverflowError` 或 `TypeError` 时，也能像处理 `NameError` 一样优雅！
