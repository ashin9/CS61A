## Part IV: Optional

### Problem 18 ✅

阅读 Scheme 规范，了解 `mu` 特殊形式的行为！

到目前为止，我们看到的所有 Scheme 过程都使用词法作用域（lexical scoping）：**新调用帧的父环境是该过程被定义时所在的环境。**而另一种作用域机制，叫做**动态作用域（dynamic scoping）**，它并不是 Scheme 的标准行为。在动态作用域下，**新调用帧的父环境是过程被调用时所在的环境。**

 使用**动态作用域时，在代码的不同位置调用同一个过程，可能会导致不同的结果（因为父环境不同）。**

在这个问题中，我们将实现 `mu` 特殊形式。它是一种非标准的 Scheme 表达式类型，表示动态作用域的过程。

在下面的示例中，我们使用 `mu` 关键字（而不是 `lambda`）来定义一个动态作用域的过程 `f`：

```scheme
; 定义了一个过程 f，它是 mu 过程。
; (* a b) 会在 f 被调用的时候计算。
; 由于 mu 使用 动态作用域，它不会在定义的时候捕获环境，只会在调用时查找变量 a 和 b。
scm> (define f (mu () (* a b)))
f

;定义了过程 g，它内部定义了局部变量 a = 4 和 b = 5，然后调用 f。
;当 f 被调用时，因为它是 mu 定义的，它用的是动态作用域：
;f 查找变量 a 和 b，而 g 当前的调用环境有 a = 4 和 b = 5，所以 f 计算 (* 4 5)，返回 20。
scm> (define g (lambda () (define a 4) (define b 5) (f)))
g
scm> (g)
20
```

过程 `f` 并没有定义 `a` 或 `b`，但是**因为 `f` 是在过程 `g` 内部被调用的，它能够访问到在 `g` 的帧中定义的 `a` 和 `b`。**



你需要实现 `do_mu_form`，用来求值 `mu` 特殊形式。`mu` 表达式类似于 `lambda` 表达式，但它返回的是一个**动态作用域的 `MuProcedure` 实例**。大部分 `MuProcedure` 类的代码已经为你提供。

除了完成 `do_mu_form` 函数的主体以外，你还需要完善 `MuProcedure` 类，使得当这种过程被调用时，能够实现动态作用域。

这意味着 `mu` 表达式创建的 `MuProcedure` 被调用时，新调用帧的父环境是调用表达式被求值时的环境。
 因此，`MuProcedure` 不需要像 `LambdaProcedure` 一样存储环境作为实例属性。它可以直接引用调用它时所在的环境中的名字。

查看 `LambdaProcedure` 的实现可以为你提供一些思路，帮助你完善 `MuProcedure`。
 你不需要修改已有的方法，但可能需要实现新的方法。



```shell
g
x = 3
y = 7
f
x = x + x = 6
return 6 + 7 = 13


➜  scheme py3 ok -q 18 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 18 (Optional) > Suite 1 > Case 1
(cases remaining: 2)


scm> (define y 1)
? y
-- OK! --

scm> (define f (mu (x) (+ x y)))
? f
-- OK! --

scm> (define g (lambda (x y) (f (+ x x))))
? g
-- OK! --

scm> (g 3 7)
? 13
-- OK! --

---------------------------------------------------------------------
Problem 18 (Optional) > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 18 (Optional) unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



> 之前学习java的时候就不太懂动态作用域是怎么实现的，在写scheme有一个problem过程中他会让你实现动态作用域，我当时直接国粹，有种豁然开朗的感觉，真的牛逼。



### Problem 19 ❓什么是尾递归？什么是尾递归优化？如何优化？

完成 `scheme.py` 文件中的 `optimize_tail_calls` 函数。它返回一个 `scheme_eval` 的替代版本，该版本支持真正的**尾递归优化。**也就是说，解释器可以在**常数空间内处理无限数量的尾递归调用。**

`Thunk` 类表示一个惰性求值的表达式（thunk），即在某个环境中还未被求值的表达式。当 `scheme_optimized_eval` 在尾上下文（tail context）中接收到一个非原子（non-atomic）表达式时，它应返回一个 `Thunk` 实例。否则，它应该不断调用 `prior_eval_function`，直到得到的是一个值，而不是 `Thunk`。

要正确实现这一功能，还需要对解释器中的其他几个函数进行修改，包括一些已经为你提供的函数。你需要确保解释器中所有处于尾上下文的表达式都通过调用 `scheme_eval` 并传入 `True` 作为第三个参数来求值。你的目标是确定哪些表达式处于尾上下文中。 

完成实现后，在 `scheme.py` 中取消以下代码的注释，以使用你的尾递归优化版本：

```python
scheme_eval = optimize_tail_calls(scheme_eval)
```



#### 尾递归理解

递归：函数内调用自身，每次递归调用，当前函数的状态都会被压入**调用栈**，等待子调用返回结果后继续处理。到达递归边界后，一层一层返回，做计算。

- 每层调用都要等递归返回，还要干点事（比如乘法），所以每一层都压栈。

```scheme
(define (fact n)
  (if (= n 0)
      1
      (* n (fact (- n 1)))))
```

尾递归：递归调用是**当前函数的最后一步操作**。调用完递归函数后，不做任何其他操作，直接返回递归结果。

- 只有递归调用，没有任何其他计算

- 此处用传递参数记录每一步计算值，最后不用一层一层返回计算，直接返回就可以计算出值。实际上已经将变量保存到第二次调用的栈帧的变量`acc`中，上一次的栈帧我们不需要再保留。
- 递归调用后啥都不干，可以**复用**当前栈帧，理论上递归可以不增加额外栈空间。

```scheme
(define (fact-iter n acc)
  (if (= n 0)
      acc
      (fact-iter (- n 1) (* n acc))))
```

#### 尾递归优化（Tail Call Optimization, TCO）

解释器或编译器如果能识别尾调用，就可以优化为一个**循环**（消除递归的栈帧增长）。不优化递归深度上去就会爆栈，优化后应该无限递归也不报错。

要做的事情就是：

- 如果发现一个表达式在尾上下文里，**不要立即求值**，而是打包成 `Thunk`，说明“我要延迟计算”。
- `Thunk` 是一个“待办任务”，表示“等会我再算”。
- 然后你用一个 `while` 循环来不断处理这些 `Thunk`，直到得到最终值。

#### 理解 `Thunk` 类

`Thunk` 类作用是：保存一个还没求值的表达式和环境。

```python
class Thunk:
    def __init__(self, expr, env):
        self.expr = expr  # 表达式
        self.env = env    # 环境
```

#### 解释器的工作流程

先回忆一下解释器最核心的 `scheme_eval`：

```python
def scheme_eval(expr, env, tail=False):
    # 分情况讨论（简化）
    if 原子表达式:
        return eval_atom(expr, env)
    elif 是特殊形式 if / lambda / define:
        return eval_special(expr, env, tail)
    else:
        # 正常函数调用
        proc = scheme_eval(operator, env)
        args = eval_args(operands, env)
        return apply(proc, args, env)
```

**重点**：

- 在尾上下文时，`scheme_eval` 不应该直接递归调用，而应该返回 `Thunk`。
- 然后循环处理这些 `Thunk`，直到返回值。

#### 实现 `optimize_tail_calls` 的思路

`optimize_tail_calls` 是一个函数生成器，它接受你原来的 `scheme_eval`（也叫 `prior_eval`），返回一个优化过的新 `scheme_eval`。

#### 确定尾上下文（tail context）在哪里

尾上下文是指：

- `if` 的 `consequent` 和 `alternative` 分支
- `cond` 的 `body`（如果是最后一组子句）
- `and`、`or`、`begin` 的最后一个表达式
- 函数 `lambda` 的 `body`
- 在 `scheme_apply` 调用的 `body`

解释器里只要你发现这些表达式，递归求值时需要传 `tail=True`。



### Scheme 解释器中的优化实现 （参考：https://github.com/ZonePG/cs-notes/blob/main/CS61A/CS61A-tail-recursion.md）

当 `optimized_eval` 接受非原子的 tail-call 表达式，它立即返回 Thunk 实例，而不是继续去递归 `scheme_eval(expr, env)` 计算表达式，而是先返回，再计算 Thunk 实例中的 expr，相当于回收之前的递归深度/空间。

否则的话，它应当反复调用 `original_scheme_eval`，直到它返回值不是 Thunk 类型。

```python
def optimize_tail_calls(original_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in environment ENV. If TAIL,
        return a Thunk containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Thunk(expr, env)

        result = Thunk(expr, env)
        # BEGIN PROBLEM 19
        "*** YOR CODE HERE ***"
        while isinstance(result, Thunk):
            result = original_scheme_eval(result.expr, result.env)
        return result
        # END PROBLEM 19
    return optimized_eval

scheme_eval = optimize_tail_calls(scheme_eval) # uncomment this!
```

遵循尾递归调用判断规则，设置 optimize_tail_calls 的第三个参数 `tail` 为 True。

- lambda, cond, let, begin 涉及 `eval_all`。
- if 涉及 `do_if_form`。
- and, or 分别是 `do_and_form`, `do_or_form`。

```python
def eval_all(expressions, env):
    # BEGIN PROBLEM 7
    # return scheme_eval(expressions.first, env) # replace this with lines of your own code
    value = None
    while expressions is not nil:
        if expressions.rest is not nil:
            value = scheme_eval(expressions.first, env)
        else:
            value = scheme_eval(expressions.first, env, True)
        expressions = expressions.rest
    return value
    # END PROBLEM 7


def do_if_form(expressions, env):
    validate_form(expressions, 2, 3)
    if is_true_primitive(scheme_eval(expressions.first, env)):
        return scheme_eval(expressions.rest.first, env, True)
    elif len(expressions) == 3:
        return scheme_eval(expressions.rest.rest.first, env, True)


def do_and_form(expressions, env):
    # BEGIN PROBLEM 12
    value = True
    "*** YOUR CODE HERE ***"
    while expressions is not nil:
        if expressions.rest is not nil:
            value = scheme_eval(expressions.first, env)
        else:
            value = scheme_eval(expressions.first, env, True)
        if value is False:
            return False
        expressions = expressions.rest
    return value


def do_or_form(expressions, env):
    # BEGIN PROBLEM 12
    "*** YOUR CODE HERE ***"
    while expressions is not nil:
        if expressions.rest is not nil:
            value = scheme_eval(expressions.first, env)
        else:
            value = scheme_eval(expressions.first, env, True)
        if value is not False:
            return value
        expressions = expressions.rest
    return False
    # END PROBLEM 12
```



### Problem 20 ❓

宏（Macros）允许用户扩展语言本身。可以通过 `define-macro` 特殊形式来定义简单的宏。`define-macro` 必须像过程定义一样使用，它创建的过程与 `define` 类似。不过，这个过程有一个特殊的求值规则：在将参数传递给过程时，不会先对这些参数求值。随后，将应用宏过程得到的结果再进行一次求值。

这个最终的求值步骤发生在调用者的环境中，就好像宏调用的位置被宏返回的表达式直接替换了一样。

下面是一个简单的例子：首先定义了一个 `map` 函数，然后定义了一个 `for` 宏，它的行为类似于 `map`，但不需要在 `body` 外部再写一个 `lambda`。例如，调用 `(for i '(1 2 3) (print (* i i)))` 会依次输出 `1`、`4` 和 `9`。

为了实现 `define-macro`，你需要完成 `do_define_macro` 的实现，这个函数应创建一个 `MacroProcedure`，并像 `do_define_form` 一样将其绑定到给定的名字上。接着，需要修改 `scheme_eval`，使其能正确处理对宏过程的调用。

提示：可以使用 `MacroProcedure` 类中的 `apply_macro` 方法将宏过程应用到调用表达式中的操作数上。这个方法已经设计好，可以很好地与尾递归优化协作。

完成实现后，可以运行以下命令来测试是否正确：

```bash
python3 ok -q 20
```

#### 宏是什么？

**普通过程 (Procedure)**：

- 参数在传入前会先求值。
- 比如 `(f (+ 1 2))`，`(+ 1 2)` 先算出 `3`，然后 `f` 接收到 `3`。

**宏过程 (Macro)**：

- 参数 **不会** 先求值，宏过程拿到的是 **原始的表达式**（语法树/AST）。
- 宏过程的返回值是一个 **表达式**，会在调用者环境中再求值，相当于“展开”代码。

##### 简单类比

- 普通过程：像函数调用，把结果传给你。

- 宏过程：像写代码生成器，写个 `for` 宏，代码在调用点自动“展开



| 部分              | 功能                                                         |
| ----------------- | ------------------------------------------------------------ |
| `do_define_macro` | 解析 `define-macro`，创建 `MacroProcedure` 并注册环境        |
| `scheme_eval`     | 识别宏调用，自动 `apply_macro` 展开宏，再递归 `scheme_eval` 评估结果 |