## Part II: The Evaluator

在提供给你的初始实现中，解释器只能求值自求值表达式：数字、布尔值和 nil。

阅读 scheme.py 文件中的前两个部分，分别是 Eval/Apply 和 Environments。

- scheme_eval 在给定环境中求值一个 Scheme 表达式。此函数几乎已经完成，但缺少对调用表达式的处理逻辑。
- 当求值一个特殊形式时，scheme_eval 会将求值过程转发到 scheme.py 文件中 Special Forms 部分的相应 do\_?_form 函数。
- scheme_apply 将某个过程应用到一些参数上。这个函数已经完成。
- Procedure 的子类中的 .apply 方法和 make_call_frame 函数，用于辅助应用内建过程和用户自定义过程。
- Frame 类实现了环境帧。
- LambdaProcedure 类（在 Procedures 部分）表示用户自定义过程。

这些都是解释器的核心组件；而 scheme.py 的剩余部分定义了特殊形式和输入/输出行为。

通过解锁 eval_apply 的测试，检验你对这些组件如何协作的理解。

```shell
➜  scheme py3 ok -q eval_apply -u

=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Understanding scheme.py > Suite 1 > Case 1
(cases remaining: 6)

# scheme_eval 三种情况，原子直接解析，非原子特殊和非特殊 
Q: What types of expressions are represented as Pairs?
Choose the number of the correct choice:
0) All expressions are represented as Pairs
1) Only call expressions
2) Call expressions and special forms
3) Only special forms
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) All expressions are represented as Pairs
1) Only call expressions
2) Call expressions and special forms
3) Only special forms
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) All expressions are represented as Pairs
1) Only call expressions
2) Call expressions and special forms
3) Only special forms
? 2
-- OK! --

---------------------------------------------------------------------
Understanding scheme.py > Suite 1 > Case 2
(cases remaining: 5)

Q: What expression in the body of scheme_eval finds the value of a name?
Choose the number of the correct choice:
0) SPECIAL_FORMS[first](rest, env)
1) scheme_symbolp(expr)
2) env.lookup(expr)
3) env.find(name)
? 2
-- OK! --

---------------------------------------------------------------------
Understanding scheme.py > Suite 1 > Case 3
(cases remaining: 4)

Q: How do we know if a given combination is a special form?
Choose the number of the correct choice:
0) Check if the first element in the list is a symbol
1) Check if the first element in the list is a symbol and that the
   symbol is in the dictionary SPECIAL_FORMS
2) Check if the expression is in the dictionary SPECIAL_FORMS
? 1
-- OK! --

---------------------------------------------------------------------
Understanding scheme.py > Suite 1 > Case 4
(cases remaining: 3)

Q: When and how do we create new Frames?
Choose the number of the correct choice:
0) Whenever a user-defined procedure is called; we use the
   make_call_frame method of LambdaProcedure
1) Whenever a primitive or user-defined procedure is called; we use
   the apply method in subclasses of Procedure
2) Whenever a primitive or user-defined procedure is called; we use
   the make_call_frame method of LambdaProcedure
3) Whenever a new procedure is defined; we use the make_child_frame
   method in Frame
? 3
-- Not quite. Try again! --

# 代码
Choose the number of the correct choice:
0) Whenever a user-defined procedure is called; we use the
   make_call_frame method of LambdaProcedure
1) Whenever a primitive or user-defined procedure is called; we use
   the apply method in subclasses of Procedure
2) Whenever a primitive or user-defined procedure is called; we use
   the make_call_frame method of LambdaProcedure
3) Whenever a new procedure is defined; we use the make_child_frame
   method in Frame
? 0
-- OK! --

---------------------------------------------------------------------
Understanding scheme.py > Suite 1 > Case 5
(cases remaining: 2)

# 内建过程（Builtins）和用户定义过程（User-defined procedures）都不一定是“固定”参数数量的。
# 内建过程可以接受可变数量的参数。例如，(+ 1 2 3 4)，+ 是内建过程，但它可以接受任意数量的参数。
# 是否“固定数量的参数”跟是不是 Builtin 没直接关系，两者都可以是“定长”或“变长”参数，具体看实现。
Q: What is the difference between applying builtins and applying user-defined procedures?
(Choose all that apply)

I.   User-defined procedures open a new frame; builtins do not
II.  Builtins simply execute a predefined function; user-defined
     procedures must evaluate additional expressions in the body
III. Builtins have a fixed number of arguments; user-defined procedures do not

---
Choose the number of the correct choice:
0) I and III
1) II and III
2) I, II and III
3) II only
4) I and II
5) I only
6) III only
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) I and III
1) II and III
2) I, II and III
3) II only
4) I and II
5) I only
6) III only
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) I and III
1) II and III
2) I, II and III
3) II only
4) I and II
5) I only
6) III only
? 5
-- Not quite. Try again! --

Choose the number of the correct choice:
0) I and III
1) II and III
2) I, II and III
3) II only
4) I and II
5) I only
6) III only
? 4
-- OK! --

---------------------------------------------------------------------
Understanding scheme.py > Suite 1 > Case 6
(cases remaining: 1)

Q: What exception should be raised for the expression (1)?
Choose the number of the correct choice:
0) AssertionError
1) SchemeError("1 is not callable")
2) SchemeError("malformed list: (1)")
3) SchemeError("unknown identifier: 1")
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) AssertionError
1) SchemeError("1 is not callable")
2) SchemeError("malformed list: (1)")
3) SchemeError("unknown identifier: 1")
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for Understanding scheme.py unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Some Core Functionality

### Problem 2 (1 pt) ✅

实现 `Frame` 类中的 `define` 和 `lookup` 方法。每个 `Frame` 对象都有以下实例属性：

- `bindings` 是一个字典，表示当前帧（frame）中的绑定。它将 Scheme 符号（在 Python 中用字符串表示）映射到对应的 Scheme 值。
- `parent` 是当前帧的父 `Frame` 实例。全局帧（Global Frame）的父帧是 `None`。

1. `define` 方法接受一个符号（在 Python 中用字符串表示）和一个值，然后在当前帧中将该符号绑定到该值。
2. `lookup` 方法接受一个符号，并返回该符号在当前环境中第一次被绑定时对应的值。注意，环境（environment）由当前帧、它的父帧以及所有祖先帧（包括全局帧）组成。因此：

- 如果该符号在当前帧中有绑定，返回对应的值。
- 如果该符号不在当前帧中，并且当前帧有父帧，则继续在父帧中查找。
- 如果该符号不在当前帧中，且没有父帧，则抛出 `SchemeError` 异常（此异常已在代码中提供）。



```shell
➜  scheme py3 ok -q 02 -u        
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 5)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> global_frame.define("x", 3)
>>> global_frame.parent is None
? True
-- OK! --

>>> global_frame.lookup("x")
? 3
-- OK! --

>>> global_frame.define("x", 2)
>>> global_frame.lookup("x")
? 2
-- OK! --

>>> global_frame.lookup("foo")
Choose the number of the correct choice:
0) SchemeError
1) 3
2) None
? SchemeErro
-- Not quite. Try again! --

Choose the number of the correct choice:
0) SchemeError
1) 3
2) None
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 2
(cases remaining: 4)

>>> from scheme import *
>>> first_frame = create_global_frame()
>>> first_frame.define("x", 3)
>>> first_frame.define("y", False)
>>> second_frame = Frame(first_frame)
>>> second_frame.parent == first_frame
? True
-- OK! --

>>> second_frame.lookup("x")
? 3
-- OK! --

>>> second_frame.lookup("y")
? False
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 2 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 2 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Problem 3 (2 pt) ✅

为了能够调用内置过程（例如 `+`），你需要完成 `BuiltinProcedure` 类中的 `apply` 方法。内置过程通过调用一个对应的 Python 函数来实现该过程。例如，Scheme 中的 `+` 对应的是 Python 中实现的 `add` 函数。

要查看项目中使用的所有 Scheme 内置过程，可以查阅 `scheme_builtins.py` 文件。任何带有 `@builtin` 装饰器的函数，都会被添加到全局定义的 `BUILTINS` 列表中。

一个 `BuiltinProcedure` 有两个实例属性：

- `fn` 是实现该 Scheme 内置过程的 Python 函数。
- `use_env` 是一个布尔值标志，表示这个内置过程是否需要传入当前环境（environment）作为最后一个参数。比如，内置的 `eval` 过程就需要当前环境。

`BuiltinProcedure` 的 `apply` 方法接收一个参数值的列表和当前环境。注意，这里的 `args` 是一个用 `Pair` 对象表示的 Scheme 列表。你的实现需要完成以下操作：

1. 将 Scheme 列表 `args` 转换为 Python 的参数列表。提示：`args` 是一个 `Pair` 对象，拥有 `.first` 和 `.rest` 属性，类似于链表。思考如何将链表的值依次放入一个 Python 列表中。
2. 如果 `self.use_env` 为 `True`，则将当前环境 `env` 作为最后一个参数添加到 Python 列表的末尾。
3. 使用 `*args` 调用 `self.fn`，例如 `f(1, 2, 3)` 等价于 `f(*[1, 2, 3])`。（已提供）
4. 如果调用 `self.fn` 时抛出 `TypeError` 异常，说明传入的参数数量不正确。使用 `try/except` 块捕获该异常，并抛出适当的 `SchemeError`。（已提供）



```shell
➜  scheme py3 ok -q 03 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 7)

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> plus = BuiltinProcedure(scheme_add) # + procedure
>>> scheme_apply(plus, twos, env) # Type SchemeError if you think this errors
? 4
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 2
(cases remaining: 6)

>>> from scheme import *
>>> env = create_global_frame()
>>> twos = Pair(2, Pair(2, nil))
>>> oddp = BuiltinProcedure(scheme_oddp) # odd? procedure
>>> scheme_apply(oddp, twos, env) # Type SchemeError if you think this errors
? False
-- Not quite. Try again! --

? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 6
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 7
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 3 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Problem 4 (1 pt) ❎

`scheme_eval` 函数用于在给定的环境中对一个 Scheme 表达式（表示为一组 `Pair` 对象）进行求值。大部分 `scheme_eval` 的实现已经为你完成。目前，它能够在当前环境中查找变量名，返回自求值表达式（比如数字），以及计算特殊形式（special forms）。

你需要实现 `scheme_eval` 中缺失的部分 —— 对**调用表达式（call expression）**的求值。为了对调用表达式求值，需要完成以下步骤：

1. 对操作符（operator）进行求值，结果应该是一个 `Procedure` 的实例。
2. 对所有的操作数（operands）进行求值。
3. 使用 `apply` 将这个过程应用到已经求值后的操作数上，并返回结果。

在前两步中，你需要递归调用 `scheme_eval`。

这里有一些你应该使用的函数或方法：

- `validate_procedure` 函数：如果提供的参数不是一个合法的 Scheme 过程，就会抛出错误。你可以使用它来确保你的操作符确实是一个过程。
- `Pair` 的 `map` 方法：通过对 Scheme 列表的每一个元素应用一个单参数函数，返回一个新的 Scheme 列表。
- `scheme_apply` 函数：将 Scheme 过程应用到一个 Scheme 列表形式的参数上。

注意：不要修改传入的 `expr`。



注意：其中一些测试称为 print-then-return 的原始 （内置） 过程。这是一个仅在此项目中使用的 “虚拟” 程序，因此您无需在其他地方使用它。只有当您未通过这些测试时，您才会遇到它。 print-then-return 接受两个参数。它打印出第一个参数，然后返回第二个参数。



```shell
➜  scheme py3 ok -q 04 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 5)

>>> from scheme_reader import *
>>> from scheme import *
>>> expr = read_line('(+ 2 2)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> scheme_eval(Pair('+', Pair(2, Pair(2, nil))), create_global_frame()) # Type SchemeError if you think this errors
? 4
-- OK! --

>>> expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? SchemeError
-- Not quite. Try again! --

? 12
-- OK! --

>>> expr = read_line('(yolo)')
>>> scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 1
(cases remaining: 4)


scm> (* (+ 3 2) (+ 1 7)) ; Type SchemeError if you think this errors
? 40
-- OK! --

scm> (1 2) ; Type SchemeError if you think this errors
? SchemeError
-- OK! --

scm> (1 (print 0)) ; validate_procedure should be called before operands are evaluated
? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 4 > Suite 2 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 4 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Problem 5 (1 pt) ❎

接下来，我们要实现**定义（define）**名字的功能。回顾一下，Scheme 中的 `define` 特殊形式可以用来做两件事：

- 给某个名字赋值
- 创建一个过程，并将它绑定到某个名字

例如：

```css
scm> (define a (+ 2 3))  ; 把名字 a 绑定到表达式 (+ 2 3) 的值
a
scm> (define (foo x) x)  ; 创建一个过程，并绑定到名字 foo
foo
```

第一个操作数（operand）告诉我们到底要定义什么：

- 如果它是一个符号，比如 `a`，那么我们是在定义一个变量。
- 如果它是一个列表，比如 `(foo x)`，那么我们是在定义一个过程。

你需要阅读 Scheme 规范（Scheme Specifications），理解 `define` 特殊形式的行为！这道题只要求你实现第一种情况 —— 把表达式的值绑定到名字上，而不是过程的定义。

`do_define_form` 函数是用来处理 `(define ...)` 特殊形式的函数。在这个问题中，有两个需要补全的部分。当前你只需要完成第一个部分：

1. 对第二个操作数进行求值，得到它的值
2. 把第一个操作数（一个符号）绑定到这个值上
3. 函数执行完后应该返回这个名字

例如：

```java
scm> (define tau (* 2 3.1415926))
tau
```

在写代码之前，先通过下面的命令测试你对这个问题的理解：

```css
python3 ok -q 05 -u
```

完成代码后，用下面的命令测试实现是否正确：

```css
python3 ok -q 05
```

现在，你应该可以给值起名字，并且能对这些名字求值了。注意，`eval` 可以对表示为列表的表达式进行求值：

```shell
scm> (eval (define tau 6.28))
6.28
scm> (eval 'tau)
6.28
scm> tau
6.28
scm> (define x 15)
x
scm> (define y (* 2 x))
y
scm> y
30
scm> (+ y (* y 2) 1)
91
scm> (define x 20)
x
scm> x
20
```

再看下面这个测试：

```makefile
(define x 0)
; 预期结果：x
((define x (+ x 1)) 2)
; 预期结果：Error
x
; 预期结果：1
```

这里之所以会抛出 `Error`，是因为操作符（operator）没有求值为一个过程。然而，如果你的解释器在抛出错误之前对操作符求值了多次，`x` 会被绑定为 2 而不是 1，这样测试就会失败。因此，如果你的解释器在这个测试失败了，说明你可能在 `scheme_eval` 函数中对操作符求值了不止一次。你需要确保在 `scheme_eval` 里只对操作符求值一次。



```shell
➜  scheme py3 ok -q 05 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 7)

Q: What is the structure of the expressions argument to do_define_form?
Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 1
-- Not quite. Try again! --

# 上下文重点：Pair(A, Pair(B, nil)) 是 define 的 operands 部分（操作数）。
# 如果解释器在 do_define_form 中已经从外层 Pair('define', rest) 拿到 rest，那么 rest 就是 Pair(A, Pair(B, nil))，这才是它要处理的对象。
# 所以，在这个上下文里：
# Pair(A, Pair(B, nil)) 正是 (define A B) 表达式中的 剩余部分，解释器处理 rest 时的结构。
Choose the number of the correct choice:
0) Pair(A, B), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
1) Pair('define', Pair(A, Pair(B, nil))), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
2) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is an expression whose value should be evaluated and bound to A
3) Pair(A, Pair(B, nil)), where:
       A is the symbol being bound,
       B is the value that should be bound to A
4) Pair(A, B), where:
       A is the symbol being bound,
       B is the value that should be bound to A
? 2
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 2
(cases remaining: 6)

Q: What method of a Frame instance will bind
a value to a symbol in that frame?
Choose the number of the correct choice:
0) bindings
1) define
2) lookup
3) make_child_frame
? 1
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 1
(cases remaining: 5)


scm> (define size 2)
? size
-- OK! --

scm> size
? 2
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 2
(cases remaining: 4)


scm> (define x (+ 2 3))
? x
-- OK! --

scm> x
? 5
-- OK! --

scm> (define x (+ 2 7))
? x
-- OK! --

scm> x
? 9
-- OK! --

# eval 会对 define 表达式求值
# define 会把 tau 绑定到 6.28
scm> (eval (define tau 6.28)) ; eval takes an expression represented as a list and evaluates it
? tau
-- Not quite. Try again! --

? 6.28
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 5 > Suite 2 > Case 5
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 5 unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



### Problem 6 (1 pt) ❎

为了完成核心功能，我们需要在解释器中实现 `quoting`（引用）。在 Scheme 中，你可以通过两种方式引用表达式：使用 `quote` 特殊形式，或使用符号 `'`。
 回忆一下，`quote` 特殊形式会返回它的**操作对象表达式**，而不会对其进行求值：

```shell
scm> (quote hello)
hello
scm> '(cons 1 2)  ; 等价于 (quote (cons 1 2))
(cons 1 2)
```

阅读 Scheme 规范（Scheme Specifications），理解 `quote` 特殊形式的行为。

------

我们先来处理 `quote` 特殊形式。
 实现 `do_quote_form` 函数，使其简单地返回 `quote` 特殊形式的操作数（operand），不对其求值。

完成这个函数后，你应该可以在解释器中评估引用表达式。可以尝试下面的例子：

```css
scm> (quote a)
a
scm> (quote (1 2))
(1 2)
scm> (quote (1 (2 three (4 5))))
(1 (2 three (4 5)))
scm> (car (quote (a b)))
a
```

------

接下来，完善 `scheme_reader.py` 中 `scheme_read` 的实现，处理 `'` 符号的情况。
 首先注意，`'<expr>` 会转换为 `(quote <expr>)`。
 这意味着我们需要将 `'` 后面的表达式（你可以通过递归调用 `scheme_read` 获取）包装进 `quote` 特殊形式中，而所有特殊形式在内部其实就是一个 `list`。

举例：
 `'bagel` 应表示为

```go
Pair('quote', Pair('bagel', nil))
```

再比如：
 `'(1 2)` 应表示为

```less
Pair('quote', Pair(Pair(1, Pair(2, nil)), nil))
```

------

完成 `scheme_read` 实现后，以下引用表达式也应该正常工作：

```shell
scm> 'hello
hello
scm> '(1 2)
(1 2)
scm> '(1 (2 three (4 5)))
(1 (2 three (4 5)))
scm> (car '(a b))
a
scm> (eval (cons 'car '('(1 2))))
1
```

------

在编写代码之前，先测试你对这个问题的理解：

```css
python3 ok -q 06 -u
```

**注意**：在完成解锁测试时，确保使用 `Pair` 表示法书写你的答案（当需要时）。

完成代码编写后，运行测试检查实现：

```css
python3 ok -q 06
```

------

到此为止，你的 Scheme 解释器应该支持以下功能：

1. 计算原子类型（atoms）：包括数字（numbers）、布尔值（booleans）、`nil` 和符号（symbols）。
2. 计算 `quote` 特殊形式。
3. 定义符号（define）。
4. 调用内置过程（built-in procedures），例如计算 `(+ (- 4 2) 5)`。

完成第 6 题后，记得使用 OK 提交，以获得第一个检查点的全部分数：

```css
python3 ok --submit
```

如果你想查看目前的得分情况，可以使用以下命令：

```css
python3 ok --score
```



```shell
➜  scheme py3 ok -q 06 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 8)

Q: What is the structure of the expressions argument to do_quote_form?
Choose the number of the correct choice:
0) A, where:
       A is the quoted expression
1) [A], where:
       A is the quoted expression
2) Pair('quote', Pair(A, nil)), where:
       A is the quoted expression
3) Pair(A, nil), where:
       A is the quoted expression
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) A, where:
       A is the quoted expression
1) [A], where:
       A is the quoted expression
2) Pair('quote', Pair(A, nil)), where:
       A is the quoted expression
3) Pair(A, nil), where:
       A is the quoted expression
? 3
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 2 > Case 1
(cases remaining: 7)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> do_quote_form(Pair(3, nil), global_frame)
? 3
-- OK! --

>>> do_quote_form(Pair('hi', nil), global_frame)
? hi
-- Not quite. Try again! --

? 'hi'
-- OK! --

>>> expr = Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
>>> do_quote_form(expr, global_frame) # Make sure to use Pair notation
? ((+ (x 2)))
-- Not quite. Try again! --

? (+ (x 2))
-- Not quite. Try again! --

? Pair(Pair('+', Pair('x', Pair(2, nil))), nil)
-- Not quite. Try again! --

? Pair('+', Pair('x', Pair(2, nil)))
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 3 > Case 1
(cases remaining: 6)


scm> ''hello
Choose the number of the correct choice:
0) (quote (quote (hello)))
1) hello
2) (hello)
3) (quote hello)
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) (quote (quote (hello)))
1) hello
2) (hello)
3) (quote hello)
? 3
-- OK! --

scm> (quote (1 2))
? (1 2)
-- OK! --

scm> (car '(1 2 3))
? 1
-- OK! --

scm> (cdr '(1 2))
? 2
-- Not quite. Try again! --

? (2)
-- OK! --

(eval (cons 'car '('(4 2))))
→ (eval (cons 'car (quote ((quote (4 2))))))
→ (eval (cons 'car '((quote (4 2)))))
→ (eval '(car (quote (4 2))))

scm> (eval (cons 'car '('(4 2))))
? (4 2)
-- Not quite. Try again! --

? 4
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 4 > Case 1
(cases remaining: 5)

>>> from scheme_reader import *
>>> read_line(" 'x ")
Choose the number of the correct choice:
0) Pair('quote', 'x')
1) Pair('quote', Pair('x', nil))
2) Pair('x', nil)
3) 'x'
? 1
-- OK! --

>>> read_line(" '(a b) ")
Choose the number of the correct choice:
0) Pair('quote', Pair('a', 'b'))
1) Pair('a', Pair('b', nil))
2) Pair('quote', Pair('a', Pair('b', nil)))
3) Pair('quote', Pair(Pair('a', Pair('b', nil)), nil))
? 3
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 4 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 4 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 4 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 6 > Suite 5 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 6 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```

