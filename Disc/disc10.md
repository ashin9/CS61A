## 1Introduction

previous versions of CS 61A were taught in the Scheme language.



## 2 Primitives and Deﬁning Variables

原子表达式意味着表达式不能被分割



### 除了 `#f` 其他都为 True，This means that 0 is not false.



定义变量后，define 特殊格式将返回其名称的符号。



特殊形式（Special forms）是一类具有独特求值规则的表达式，可以实现多种功能。通常，特殊形式类似于 Python 中的语句，比如赋值语句、if 语句和 def 语句。

然而，Scheme 中的所有特殊形式在求值后都会返回一个值。

我们将在后续讨论中进一步学习特殊形式的内容。



## 3 Call Expressions

### `(<operator> <operand1> <operand2> ...)`

1. Evaluate the operator to get a procedure.

2. Evaluate each of the operands from left to right.

3. Apply the value of the operator to the evaluated operands.



运算符可以是符号，比如 + 和 *，也可以是更复杂的表达式，只要它们的求值结果是过程（函数）值即可。



### built-in functions

• +, -, *, /

• =, >, >=, <, <=

• quotient, modulo, even?, odd?, null?



### Questions

### 3.1 ✅



```scheme
scm> (define a (+ 1 2))
a

scm> a
3

scm> (define b (- (+ (* 3 3) 2) 1))
b

scm> (= (modulo b a) (quotient 5 3))
b = 10
(modulo b a) = 1
(quotient 5 3) = 1

#t
```



## 4 Special Forms

特殊形式表达式（Special form expressions）以一个特殊形式作为运算符。特殊形式表达式不像调用表达式那样遵循相同的求值规则。

每个特殊形式都有自己独特的求值规则——这正是它们“特殊”的原因！



### If Expression

`(if <predicate> <if-true> [if-false])`



1. Evaluate <predicate>.

2. If <predicate> evaluates to a truth-y value, evaluate <if-true> and return its value. Otherwise, evaluate [if-false] if provided and return its value.



### Boolean Operators

### short-circuiting operators. 短路

### And 从左向右评估，返回第一个 false 值，若全 true 返回最后一个值

### Or 从左向右评估，返回第一个 true 值，若全 false 返回最后一个值

```scheme
scm> (or 1 (/ 1 0))
1
```





### Questions

### 4.1 ✅

```scheme
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1

scm> ((if (< 4 3) + -) 4 100)
-96
```



## Lambdas and Deﬁning Functions

### All Scheme procedures are lambda procedures.

### `(lambda (<param1> <param2> ...) <body>)`



这个表达式创建了一个带有给定参数和函数体的 lambda 函数，但并不会立即对函数体进行求值。就像在 Python 中一样，函数体只有

在函数被调用并应用到某些参数值时才会被求值。正是因为 lambda 表达式中的操作数都不会被求值，这才使得 lambda 成为了一个

特殊形式（special form）。

另一个与 Python 相似的地方是，lambda 表达式并不会自动将返回的函数赋值给某个名字。我们可以使用 define 这个特殊形式来将

某个表达式的值赋给一个名字。



例如，`(define square (lambda (x) (* x x)))` 创建了一个 lambda 过程，这个过程会对传入的参数求平方，并将该过程赋值给名字 `square`。



`define` 特殊形式的第二种写法是这种函数定义的简写形式：

### `(define (<name> <param1> <param2 ...>) <body>)`



```scheme
scm> (define square (lambda (x) (* x x))) ; Bind the lambda function to the name square 
square 
scm> (define (square x) (* x x)) ; Equivalent to the line above 
square 
scm> square 
(lambda (x) (* x x)) 
scm> (square 4) 
16
```



### 4.1 ✅

写一个函数，返回阶乘

```scheme
> (define (factorial x)
    (if (= x 0) 0 
  		(if (= x 1)
        	1
        	(* x (factorial (- x 1)))
   	   )
    )
  )

(if (< x 2)
    1 
    (* x (factorial (- x 1)))))
```



### 4.2 ✅

第 n 个 fib 数

```scheme
(define (fib n)
  (if (= n 0)
      0
      (if (= n 1)
          1
          (+ (fib (- n 1) (fib (- n 2)))
          )
      )
  )
  
  
(if (<= n 1)
    n 
    (+ (fib (- n 1)) (fib (- n 2))))
```



## 5 Pairs and Lists

### Scheme 所有 list 都是链表

deﬁne a list as being either

• the empty list, nil

• a pair whose second element is a list



We use the following procedures to construct and select from lists:

• (cons first rest) constructs a list with the given ﬁrst element and rest of the list. For now, if rest is not a pair or nil it will error.

• (car lst) gets the ﬁrst item of the list

• (cdr lst) gets the rest of the list



另外两种常见的创建列表的方法是使用内置的 `list` 过程或 `quote` 特殊形式：

- `list` 过程可以接受任意数量的参数。因为它是一个过程，所以在调用 `list` 时，所有的操作数都会被求值。然后用这些操作数的值构造出一个列表，并将其返回。
- `quote` 特殊形式接受一个操作数。它会原样返回这个操作数，而不会对其进行求值。需要注意的是，这个特殊形式不仅可以用于返回列表，还可以返回任何值。



```scheme
scm> '(1 x 3) ; Equivalent to the previous quote expression 
(1 x 3) 
scm> '(+ x y) 
(+ x y)
```



### =, eq?, equal?

- `=` 只能用于比较数字

- `eq?` 类似于 Python 中的 `==`，用于比较两个非对偶（non-pair）类型的值（比如数字、布尔值等）。否则，`eq?` 的行为更像 Python 中的 `is`，判断是否是同一个对象。

- `equal?` 会通过比较对偶（pair）的 `car` 和 `cdr` 是否 `equal?`，来判断两个结构是否具有相同的内容。否则，`equal?` 的行为和 `eq?` 相同



```scheme
scm> (define a '(1 2 3))
a
scm> (= a a)
Error
scm> (equal? a '(1 2 3))
#t
scm> (eq? a '(1 2 3))
#f
scm> (define b a)
b
scm> (eq? a b)
#t
```



## Questions

### 5.1 ❎ 如何判断 null？如何赋值语法？重新构造链表？

编写一个函数，它接受两个列表并将它们连接在一起。

注意，直接调用 `(cons a b)` 是行不通的，因为它会创建一个嵌套（深层次）的列表。而不是将两个列表简单地拼接在一起。

不要调用内置过程 `append`，因为 `append` 和你要实现的 `my-append` 做的是相同的事情。



```scheme
(define (my-append a b)
  (if (= (cdr a) nil)
      (= (cdr a) b)
      (my-append (cdr a) b)
      )
   )

(define (my-append a b)
  (if (null? a)
      (= a b)
      (my-append (cdr a) b)
      )
  )

(define (my-append a b)
  (if (null? a)
      b
      (cons (car a) (my-append (cdr a) b))
      )
  )
```



### 5.2 ✅

教程：这些简短的问题旨在帮助你在处理更具挑战性的问题之前，回顾本周讲座和实验中涉及的主题。

描述下面两个 Scheme 表达式之间的区别。

提示：哪个定义了一个新的过程？

- A 是定义了 x 绑定到 6 上  ✅
- B 是定义了过程 x，没有参数，返回 6 ✅

```scheme
Expression A:
(define x (+ 1 2 3))

Expression B:
(define (x) (+ 1 2 3))
```



Write an expression that selects the value 3 from the list below. ✅

```schceme
(define s '(5 4 (1 2) 3 7))

( car( (cdr (cdr (cdr s)))))
```



### 5.3 ❎ 错误点：若 lst 为空则返回什么？返回 lst

编写一个 Scheme 函数，当传入一个列表（例如 `(1 2 3 4)`）时，返回一个新列表，其中每个元素都被重复一次（即返回 `(1 1 2 2 3 3 4 4)`）。



```scheme
(define (duplicate lst)
  (if (null? lst)
      lst
    (cons (car lst) 
          (cons (car lst) 
                (duplicate (cdr lst)
                           )
                )
          )
   )
  )
```





### 5.4 ❎，不好想逻辑，✅ 看了 if 的第一行，后面自己能写出来

编写一个 Scheme 函数，当给定一个元素、一个列表和一个索引时，将该元素插入到列表的指定索引位置。

```scheme
(define (insert element lst index)
  (if (= index 0)
      (cons element lst)
      (cons (car lst) 
            (insert element (cdr lst) (- index 1))
            )
      )
  )
```

