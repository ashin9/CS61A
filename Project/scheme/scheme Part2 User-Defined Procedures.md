

### User-Defined Procedures

用户定义的过程（User-defined procedures）通过 `LambdaProcedure` 类的实例来表示。
 一个 `LambdaProcedure` 实例包含三个实例属性：

- `formals`：是一个 Scheme 列表，包含形式参数（symbols），用于命名该过程的参数。
- `body`：是一个 Scheme 列表，包含过程的主体表达式（也就是过程的代码块）。
- `env`：是过程定义时所在的环境（environment）。

这个环境保存了过程创建时的变量绑定信息，是实现词法作用域（lexical scoping）的关键。

### Problem 7 (1 pt) ✅

阅读 Scheme 语言规范，理解 `begin` 特殊形式（special form）的行为！

接下来你需要修改 `scheme.py` 文件中的 `eval_all` 函数（它会被 `do_begin_form` 调用），以完成 `begin` 特殊形式的实现。

`begin` 表达式的行为是：依次按顺序求值它包含的所有子表达式。整个 `begin` 表达式的返回值是最后一个子表达式的值。

例如：

```scss
scm> (begin (+ 2 3) (+ 5 6))
11
```

第一个子表达式 `(+ 2 3)` 被求值为 `5`，第二个子表达式 `(+ 5 6)` 被求值为 `11`。
 整个 `begin` 表达式返回第二个子表达式的值 `11`。

再比如：

```scss
scm> (define x (begin (display 3) (newline) (+ 2 3)))
3
x
scm> (+ x 3)
8
```

解释：

- `(display 3)` 输出 `3`
- `(newline)` 换行
- `(+ 2 3)` 计算并返回 `5`
   最后 `define` 把 `x` 绑定为 `5`，再加上 `3` 得到 `8`。

还有这个例子：

```shell
scm> (begin (print 3) '(+ 2 3))
3
(+ 2 3)
```

第一个子表达式 `print 3` 输出 `3`
 第二个子表达式 `(+ 2 3)` 被 `quote`，所以直接返回 `(+ 2 3)`，不求值。

------

**注意：**
 如果 `eval_all` 被传入一个空的表达式列表（也就是 `nil`），它应该返回 Python 中的 `None`，对应 Scheme 里的 `undefined`。

------

在写代码之前，先通过下面命令检查你是否理解了题目：

```css
python3 ok -q 07 -u
```

完成代码后，运行下面命令来测试你写的实现是否正确：

```css
python3 ok -q 07
```



```shell
➜  scheme py3 ok -q 07 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 1
(cases remaining: 6)

>>> from scheme import *
>>> env = create_global_frame()
>>> eval_all(Pair(2, nil), env)
Choose the number of the correct choice:
0) SchemeError
1) 2
? 2
-- OK! --

>>> eval_all(Pair(4, Pair(5, nil)), env)
Choose the number of the correct choice:
0) 4
1) 5
2) (4 5)
3) SchemeError
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) 4
1) 5
2) (4 5)
3) SchemeError
? 3
-- Not quite. Try again! --

Choose the number of the correct choice:
0) 4
1) 5
2) (4 5)
3) SchemeError
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) 4
1) 5
2) (4 5)
3) SchemeError
? 1
-- OK! --

>>> eval_all(nil, env) # return None (meaning undefined)
---------------------------------------------------------------------
Problem 7 > Suite 1 > Case 2
(cases remaining: 5)

>>> from scheme import *
>>> env = create_global_frame()
>>> lst = Pair(1, Pair(2, Pair(3, nil)))
>>> eval_all(lst, env)
? 3
-- OK! --

>>> lst     # The list should not be mutated!
? Pair(1, Pair(2, Pair(3, nil)))
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 1
(cases remaining: 4)


scm> (begin (+ 2 3) (+ 5 6))
? 11
-- OK! --

scm> (begin (define x 3) x)
? 3
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 2
(cases remaining: 3)


scm> (begin 30 '(+ 2 2))
Choose the number of the correct choice:
0) 4
1) '(+ 2 2)
2) 30
3) (+ 2 2)
? 3
-- OK! --

scm> (define x 0)
? x
-- OK! --

scm> (begin (define x (+ x 1)) 42 (define y (+ x 1)))
? y
-- OK! --

scm> x
? 1
-- OK! --

scm> y
? 2
-- OK! --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 7 > Suite 2 > Case 4
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 7 unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



### Problem 8 (1 pt) ✅

阅读 Scheme 语言规范，理解 `lambda` 特殊形式（special form）的行为！

`LambdaProcedure` 表示用户自定义的过程（函数）。
 它有三个主要属性：

1. `formals`：参数名的列表（形式参数列表），告诉我们调用函数时需要哪些参数。
2. `body`：函数体，由一个或多个表达式组成，依次求值。
3. `env`：定义该过程时所在的环境（父作用域环境）。

------

### 你的任务

实现 `do_lambda_form` 函数，它的作用是创建并返回一个 `LambdaProcedure` 实例。
 虽然现在你还无法调用用户定义的过程，但你可以在解释器里输入 `lambda` 表达式，验证 `LambdaProcedure` 是否创建正确。

例如，在解释器中输入：

```scss
scm> (lambda (x y) (+ x y))
(lambda (x y) (+ x y))
```

你应该能看到这个过程对象被返回。
 其中 `(lambda (x y) (+ x y))` 表示创建了一个接收两个参数 `x` 和 `y`，并返回 `(+ x y)` 结果的函数。

------

在 Scheme 语言中，一个 `lambda` 表达式的函数体 `body` 可以包含多个表达式（但**至少要有一个表达式**）。
 `LambdaProcedure` 的 `body` 属性就是这个表达式列表（Scheme list）。

------

### 编码前检查

在写代码之前，运行下面命令检查你是否理解了题目要求：

```css
python3 ok -q 08 -u
```

### 编码后测试

完成 `do_lambda_form` 函数后，运行下面命令测试你写的实现是否正确：

```css
python3 ok -q 08
```

------

### 小结

这个 `lambda` 特殊形式是用来创建函数（过程）的，
 完成 `do_lambda_form` 就相当于让解释器具备了“定义函数”的能力。



```shell
➜  scheme py3 ok -q 08 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 5)


scm> (lambda (x y) (+ x y))
? (lambda (x y) (+ x y))
-- OK! --

scm> (lambda (x)) ; type SchemeError if you think this causes an error
? (lambda (x))
-- Not quite. Try again! --

? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 1
(cases remaining: 2)

>>> from scheme_reader import *
>>> from scheme import *
>>> env = create_global_frame()
>>> lambda_line = read_line("(lambda (a b c) (+ a (* b c)))")
>>> lambda_proc = do_lambda_form(lambda_line.rest, env)
>>> lambda_proc.formals
? (a b c)
-- Not quite. Try again! --

? a b c
-- Not quite. Try again! --

? "(a b c)"
-- Not quite. Try again! --

? Pair(a, Pair(b, Pair(c, nil)) )
-- Not quite. Try again! --

? Pair(a, Pair(b, Pair(c, nil)))
-- Not quite. Try again! --

? Pair('a', Pair('b', Pair('c', nil)))
-- OK! --


# ❎，注意处理好 nil
>>> lambda_proc.body # Remember that the body is a *list* of expressions!
? Pair(Pair('+', Pair('a', Pari(Pair('*', Pair('b', Pair('c', nil)))))))
-- Not quite. Try again! --

? Pair('+', Pair('a', Pari(Pair('*', Pair('b', Pair('c', nil))))))
-- Not quite. Try again! --

? Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil))))))
-- Not quite. Try again! --

? Pair(Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil)))))))
-- Not quite. Try again! --

? (+ a (* b c))
-- Not quite. Try again! --

? Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil))))), nil)
-- Not quite. Try again! --

? Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil)))), nil), nil)
-- Not quite. Try again! --

? Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil)))), nil))
-- Not quite. Try again! --

? Pair(Pair('+', Pair('a', Pair(Pair('*', Pair('b', Pair('c', nil))), nil))), nil)
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 2 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 8 unlocked.

Performing authentication
Please enter your school email (.edu): ^C%  
```



### Problem 9 (2 pt) ❎ ✅

### 本题任务

在这个问题中，我们要完成 `define` 语法的实现，特别是用来定义**过程（函数）**的 `define`。

#### 当前解释器的现状

你的 Scheme 解释器目前可以通过以下方式把符号绑定到用户自定义过程：

```scss
scm> (define f (lambda (x) (* x 2)))
f
```

#### 目标

我们希望实现 `define` 的**简写形式**，也就是下面这种写法：

```scss
scm> (define (f x) (* x 2))
```

这意味着你需要修改 `do_define_form` 函数，让解释器支持这种简洁的过程定义方式，并且能够处理包含多条表达式的函数体（body）！

#### 具体实现

你的实现需要做到以下几点：

- 利用已经存在的 `target` 和 `expressions` 变量，找出函数的名字（name）、形式参数（formals）和函数体（body）。
- 创建一个 LambdaProcedure 实例，包含 formals 和 body。提示：你可以复用第 8 题中完成的 do_lambda_form，并在合适的位置调用它。
- 把函数名字和 LambdaProcedure 实例绑定起来。



```shell
➜  scheme py3 ok -q 09 -u 
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 7)


scm> (define (f x y) (+ x y))
? f
-- OK! --

scm> f
Choose the number of the correct choice:
0) (define f (lambda (x y) (+ x y)))
1) (lambda (f x y) (+ x y))
2) (lambda (x y) (+ x y))
3) (f (x y) (+ x y))
? 2
-- OK! --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 4
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 5
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 6
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 9 > Suite 2 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 9 unlocked.

Performing authentication
Please enter your school email (.edu): ^C%
```



### Problem 10 (2 pt) ✅

实现 `Frame` 类中的 `make_child_frame` 方法，这个方法用于为用户自定义的过程创建新的调用框架（frame）。该方法接收两个参数：`formals`（一个包含形式参数的 Scheme 列表）和 `vals`（一个包含实参值的 Scheme 列表）。它应当返回一个新的子框架，并将形式参数绑定到对应的实参值。

具体实现要求如下：

- 如果实参值的数量与形式参数的数量不匹配，抛出 `SchemeError`。已提供。
- 创建一个新的 `Frame` 实例，并将 `self` 作为它的父框架。
- 在新创建的子框架中，将每一个形式参数依次绑定到对应的实参值。`formals` 中的第一个符号应绑定到 `vals` 中的第一个值，依此类推。
- 返回新创建的子框架。

提示：`Frame` 实例的 `define` 方法可以在该框架中创建绑定。



```shell
➜  scheme py3 ok -q 10 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 6)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> formals = Pair('a', Pair('b', Pair('c', nil)))
>>> vals = Pair(1, Pair(2, Pair(3, nil)))
>>> frame = global_frame.make_child_frame(formals, vals)
>>> global_frame.lookup('a') # Type SchemeError if you think this errors
? 1
-- Not quite. Try again! --

? SchemeError
-- OK! --

>>> frame.lookup('a')        # Type SchemeError if you think this errors
? 1
-- OK! --

>>> frame.lookup('b')        # Type SchemeError if you think this errors
? 2
-- OK! --

>>> frame.lookup('c')        # Type SchemeError if you think this errors
? 3
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 2
(cases remaining: 5)

>>> from scheme import *
>>> global_frame = create_global_frame()
>>> frame = global_frame.make_child_frame(nil, nil)
>>> frame.parent is global_frame
? True
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 3
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 1
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 2
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 10 > Suite 2 > Case 3
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 10 unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



### Problem 11 (1 pt) ✅

实现 `LambdaProcedure` 类中的 `make_call_frame` 方法，这个方法是 `scheme_apply` 所需要的。它应当使用合适的父环境的 `make_child_frame` 方法创建并返回一个新的 `Frame` 实例，同时将形式参数绑定到实参值。

由于 `lambda` 表达式采用词法作用域（lexical scoping），所以新创建的 `frame` 必须是定义该 `lambda` 时所在环境（`env` 属性）的子环境。而传递给 `make_call_frame` 的 `env` 参数，实际上是过程被调用时的环境，这在后续实现动态作用域（problem 18，可选）时会用到。



做到这里，你的 Scheme 解释器应该已经支持以下功能：

- 使用 `lambda` 表达式创建过程；
- 使用 `define` 表达式定义具名过程；
- 调用用户自定义的过程。





```shell
outer 1 2
x = 1
y = 2
inner
z
x

inner x 10
z = x = 1
x = 10

(+ 10 + 4 + 3) = 17 ✅


outer-func
x = 1
y = 2
inner
z = 1
x = 10

(+ 10 + 4 + 3) ✅


➜  scheme py3 ok -q 11 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 11 > Suite 1 > Case 1
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 11 > Suite 1 > Case 2
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 11 > Suite 2 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 11 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 11 > Suite 3 > Case 1
(cases remaining: 2)


scm> (define (outer x y)
....   (define (inner z x)
....     (+ x (* y 2) (* z 3)))
....   (inner x 10))
? inner
-- Not quite. Try again! --

? outer
-- OK! --

scm> (outer 1 2)
? inner
-- Not quite. Try again! --

? (inner 1 10)
-- Not quite. Try again! --

? 17
-- OK! --

scm> (define (outer-func x y)
....   (define (inner z x)
....     (+ x (* y 2) (* z 3)))
....   inner)
? outer-func
-- OK! --

scm> ((outer-func 1 2) 1 10)
? 17
-- OK! --

---------------------------------------------------------------------
Problem 11 > Suite 3 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 11 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Special Forms

逻辑特殊形式包括 `if`、`and`、`or` 和 `cond`。这些表达式之所以特殊，是因为它们的部分子表达式可能不会被求值。

在 Scheme 中，只有 `False` 被视为假值。所有其他值（包括 `0` 和 `nil`）都被视为真值。你可以使用 `scheme_builtins.py` 文件中提供的 Python 函数 `is_true_primitive` 和 `is_false_primitive` 来判断一个值是真值还是假值。

注意：Scheme 传统上使用 `#f` 表示布尔值中的假。在我们的解释器中，这相当于 `false` 或 `False`。类似地，`true`、`True` 和 `#t` 也是等价的。然而，在解锁测试时，请使用 `#t` 和 `#f`。

为了帮助你入门，我们已经在 `do_if_form` 函数中提供了 `if` 特殊形式的实现。在开始后续问题之前，请务必理解这个实现。



### Problem 12 (2 pt) ✅

阅读 Scheme 规范，了解 `and` 和 `or` 这两个特殊形式的行为！

实现 `do_and_form` 和 `do_or_form` 函数，以便正确地计算 `and` 和 `or` 表达式。

逻辑形式 `and` 和 `or` 是具有**短路求值（short-circuiting）行为**的：

### 对于 `and`：

- 你的解释器应该从左到右依次计算每个子表达式。
- 如果某个子表达式的值为假值（false value），立即返回 `#f`。
- 如果所有子表达式都是真值（true values），返回最后一个子表达式的值。
- 如果 `and` 表达式中没有任何子表达式，它的结果是 `#t`。

示例：

```scheme
scm> (and)
#t

scm> (and 4 5 6)  ; 所有操作数都是真值
6

scm> (and 4 5 (+ 3 3))
6

scm> (and #t #f 42 (/ 1 0))  ; and 的短路行为
#f
```

### 对于 `or`：

- 你的解释器应从左到右依次计算每个子表达式。
- 如果遇到一个子表达式的值为真值（true value），立即返回该值。
- 如果所有子表达式的值都是假值，返回 `#f`。
- 如果 `or` 表达式中没有任何子表达式，它的结果是 `#f`。

示例：

```scheme
scm> (or)
#f

scm> (or 5 2 1)  ; 5 是真值
5

scm> (or #f (- 1 1) 1)  ; 0 在 Scheme 中是真值
0

scm> (or 4 #t (/ 1 0))  ; or 的短路行为
4
```

⚠️ 提示： 你可以使用提供的 Python 函数 `is_true_primitive` 和 `is_false_primitive` 来判断某个值是真值还是假值。

完成之后，`do_and_form` 和 `do_or_form` 的实现将让你的解释器支持逻辑与、逻辑或的短路求值！



```shell
➜  scheme py3 ok -q 12 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 1
(cases remaining: 9)


scm> (and)
Choose the number of the correct choice:
0) #f
1) SchemeError
2) #t
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) #f
1) SchemeError
2) #t
? 2
-- OK! --

scm> (and 1 #f)
Choose the number of the correct choice:
0) #t
1) #f
2) 1
? 1
-- OK! --

scm> (and (+ 1 1) 1)
? 1
-- OK! --

scm> (and #f 5)
? #f
-- OK! --

scm> (and 4 5 (+ 3 3))
? 6
-- OK! --

scm> (not (and #t #f 42 (/ 1 0)))
? #t
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 2
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 3
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 1 > Case 4
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 1
(cases remaining: 5)


scm> (or)
? #f
-- OK! --

scm> (or (+ 1 1))
? 2
-- OK! --

scm> (not (or #f))
? #t
-- OK! --

scm> (define (zero) 0)
? zero
-- OK! --

scm> (or (zero) 3)
? 0
-- OK! --

scm> (or 4 #t (/ 1 0))
? 4
-- OK! --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 12 > Suite 2 > Case 5
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 12 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Problem 13 (2 pt) ✅

阅读 Scheme 规范，了解 `cond` 特殊形式的行为！

完成 `do_cond_form` 函数的剩余部分，使其能够返回第一个为真谓词对应的结果子表达式的值，或者 `else` 对应的结果子表达式的值。需要注意以下特殊情况：

- 如果为真的谓词没有对应的结果子表达式，应返回该谓词自身的值。
- 如果某个 `cond` 分支的结果子表达式包含多个表达式，依次求值并返回最后一个表达式的值。（提示：使用 `eval_all`。）

你的实现需要符合以下示例以及 `tests.scm` 文件中的额外测试：

```scheme
scm> (cond ((= 4 3) 'nope)
           ((= 4 4) 'hi)
           (else 'wait))
hi

scm> (cond ((= 4 3) 'wat)
           ((= 4 4))
           (else 'hm))
#t

scm> (cond ((= 4 4) 'here (+ 40 2))
           (else 'wat 0))
42
```

如果没有任何谓词为真，且没有 `else` 分支，`do_cond_form` 应该返回 `None`（表示 Scheme 中的 `undefined`）。

如果只有一个 `else` 分支，返回其结果子表达式的值。如果 `else` 分支没有结果子表达式，返回 `#t`。

示例：

```scheme
scm> (cond (False 1) (False 2))
; 没有返回值

scm> (cond (else))
#t
```



```shell
➜  scheme py3 ok -q 13 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 13 > Suite 1 > Case 1
(cases remaining: 6)


scm> (cond ((> 2 3) 5)
....       ((> 2 4) 6)
....       ((< 2 5) 7)
....       (else 8))
? 7
-- OK! --

scm> (cond ((> 2 3) 5)
....       ((> 2 4) 6)
....       (else 8))
? 8
-- OK! --

scm> (cond ((= 1 1))
....       ((= 4 4) 'huh)
....       (else 'no))
? #t
-- OK! --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 1
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 2
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 3
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 4
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 13 > Suite 2 > Case 5
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 13 unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



### Problem 14 (2 pt) ❎ 如何嵌套？ 检查长度为 2，value 求值

阅读 Scheme 规范，了解 `let` 特殊形式的行为！

`let` 特殊形式用于在**局部范围内绑定符号到值**，并为它们提供初始值。例如：

```scheme
scm> (define x 5)
x
scm> (define y 'bye)
y
scm> (let ((x 42)
           (y (* x 10)))  ; 这里的 x 仍然指的是全局作用域中的 x，而不是 42
       (list x y))
(42 50)
scm> (list x y)
(5 bye)
```

实现 `make_let_frame`，该函数返回 `env` 的子帧，并将 `bindings` 中的每个符号绑定到其对应的表达式求值结果。`bindings` 是一个 Scheme 列表，其中每个元素都是一个包含符号和对应表达式的对（`Pair`）。

你可能会用到以下函数和方法：

- `validate_form`：用于验证 `bindings` 的结构。该函数接受一个表达式列表 `expr` 以及 `min` 和 `max` 长度。如果 `expr` 不是一个正确的列表，或者其长度不在 `min` 和 `max`（含）之间，则会引发错误。如果 `max` 没有提供，则默认为无限。
- `validate_formals`：用于验证 `bindings` 中的形式参数是否是一个 Scheme 符号列表，且所有符号都是唯一的。
- `make_child_frame`：`Frame` 类的方法（你在问题 11 中实现），它接受一个 `Pair` 形式的参数列表（符号）和 `Pair` 形式的值列表，并返回一个新的帧，将所有符号绑定到对应的值。

在编写代码之前，先测试你对问题的理解：

```bash
python3 ok -q 14 -u
```

编写代码后，测试你的实现：

```bash
python3 ok -q 14
```

运行额外的 Scheme 测试（值 1 分），运行以下命令：

```bash
python3 ok -q tests.scm
```

确保删除所有 **不在可选部分的 `(exit)`** 语句，以便运行所有测试！检查是否删除正确 `(exit)` 语句的最佳方法是运行以下命令：

```bash
python3 ok --score
```

如果通过所有必需测试，在 `tests.scm` 部分，你应该看到 **1/1** 分数。

完成 **Part II** 后，确保提交以获得完整的检查点分数：

```bash
python3 ok --submit
```

如果你想检查当前得分，可以运行：

```bash
python3 ok --score
```

🎉 **恭喜！你的 Scheme 解释器实现已完成！** 🎉

**注意：** 在正常的 Office Hours 和 Project Parties 期间，助教将优先帮助学生完成必做问题。如果问题队列已清空，他们才会帮助解答额外的加分题。



```shell
➜  scheme py3 ok -q 14 -u
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 1
(cases remaining: 9)


scm> (define x 1)
? x
-- OK! --

scm> (let ((x 5))
....    (+ x 3))
? (5 4)
-- Not quite. Try again! --

? ((5) 4)
-- Not quite. Try again! --

? 8
-- OK! --

scm> x
? 1
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 2
(cases remaining: 8)


scm> (let ((a 1) (b a)) b)
Choose the number of the correct choice:
0) y
1) 1
2) SchemeError
3) x
? 2
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 3
(cases remaining: 7)


scm> (let ((x 5))
....    (let ((x 2)
....          (y x))
....        (+ y (* x 2))))
? 9
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 4
(cases remaining: 6)


scm> (let ((a 2) (a 3)) (+ a a)) ; how should we catch something like this?
? 6
-- Not quite. Try again! --

? 5
-- Not quite. Try again! --

? 3
-- Not quite. Try again! --

? 4
-- Not quite. Try again! --

? SchemeError
-- OK! --

scm> (let ((y 2 3)) (+ y y)) ; should this be an allowable form?
? 6
-- Not quite. Try again! --

? SchemeError
-- OK! --

---------------------------------------------------------------------
Problem 14 > Suite 1 > Case 5
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 2 > Case 1
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 2 > Case 2
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 2 > Case 3
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem 14 > Suite 3 > Case 1
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 14 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



