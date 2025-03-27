## Higher Order Functions (HOF)

HOF 以函数作为参数或返回值或两者都满足的函数，HOF 是强大的抽象工具来表达通用模式



### A Note on Lambda Expressions

函数，输入，返回值

lambda 匿名

直到被 call 前，不会求值计算，同 def 定义函数一样

不同于 def 定义函数，lambda 既可作为 operator 也可作为 operand

```python
>>> (lambda y: y + 5)(4) 
9
>>> (lambda f, x: f(x))(lambda y: y + 1, 10)
11
```



### Curring

HOF 重要应用是把多参数函数柯里化为单参数函数链



### Questions

1.1

```python
def keep_ints(cond, n):
  """Print out all integers 1..i..n where cond(i) is true

	>>> def is_even(x):
	... # Even numbers have remainder 0 when divided by 2. 
	... return x % 2 == 0
	>>> keep_ints(is_even, 5) 
	2 
	4 
	"""
  for i in range(1, n):
    if cond(i):
      print(i)
```

1.2

```python
def make_keeper(n):
	"""Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling 		cond(i) returns True.

	>>> def is_even(x):

	... # Even numbers have remainder 0 when divided by 2. 
	... return x % 2 == 0

	>>> make_keeper(5)(is_even) 
	2 
	4
	"""
  def f(cond):
    for i in range(i, n):
      if cond(i):
        pirnt(i)
    #return f 不用返回f，
  return f  

# 返回 f 多打印一行函数信息
In [90]: def make_keeper(n):
    ...:     def f(cond):
    ...:         for i in range(1, n):
    ...:             if cond(i):
    ...:                 print(i)
    ...:         return f
    ...:     return f
    ...:

In [91]: make_keeper(5)(is_even)
2
4
Out[91]: <function __main__.make_keeper.<locals>.f(cond)>
```



### HOFs in Environment Diagrams

lambda 在环境图中，和 def 定义函数一样，只是没有内在命名，因此用 lambda 表示

所有函数的父环境是定义函数的环境，标记父环境用处是跟踪不在当前环境的变量



1.3

```python
----Global----
curry2 -> func 

----curry2----
h -> lambda func
f -> func
return f

----Global----
make_adder -> f

----f----
x = 3
g -> func
return g

----Global----
make_adder -> f
add_three -> g

----g----
y = 4
return 7

----Global----
add_four = 7

----g----
y = 2
return 3 + 2 = 5

----Global----
five = 5
```



1.4 curry2 为 lambda 匿名函数

```python
lambda x, y : lambda x : lambda y : f(x, y) # 错误写法

# 正确写法
curry2 = lambda f: lambda x : lambda y : f(x, y)
```



1.5

```python
----Global----
n = 7
f -> func f(x)
g -> func g(x)
f -> func f(f,x)
----f(f,x)----
f -> g
x = n = 7
return -> g(14) -> func h()
----g(x)----
x = 14
n = 9
h -> func h()
return -> func h()
----Global----
-> lambda func 
----lambda func----
y -> h()
return h() = 15
----h()----
return 15
----Global----
g = 15
```



1.6

```python
----Global----
y = "y"
h = "y"
y -> func y(y)
----y()----
形参 y = "y" 错误了，应该 y 指向 func y(y)
h = "h"
y -> lambda func y: y(h)
return -> lambda func y: y(h) = 
----lambda func y(h)----
h = y = "y"
return lambda func y(h)
----Global----
----y(h)----
h = y = "y"
h = "h"

# 想不下去了
```



```python
----Global----
y = "y"
h = "y"
y -> func y(y)
----y()----
形参 y -> func y(y)
h = "h"
y -> lmd func y:y(h)
return lmd func h:y(h)
----Global----
----lmd y(h)----
形参 h -> y 
调用 y(y)
---- lmd y(h)----
形参 y -> y
调用 y(h)
h 回溯 "h"
调用 y("h")
----y("h")----
y = "h"
h = "h"
return "h" + "i" = "hi"
----Global----
y="hi"
```



纠正错误理解：

- 绑定命名 y，一开始由字符串换到函数，只能指向一个，即后面绑定的
- return 函数定义，如 lambda 匿名函数，不会马上计算函数，因为也没调用也没传实参。注意区分返回函数还是返回函数调用！
- 向当前环境上面回溯找 y 绑定的函数



## Self Reference

自引用函数，函数自己返回自己，是 HOF 重要的设计方法

不是返回 call 结果，而是返回函数自己



通常引用外部函数辅助

```python
def print_sums(n):
	print(n) 
  def next_sum(k):
    return print_sums(n+k) 
  return next_sum
```

call print_sums 返回 next_sum

call next_sum 返回调用 print_sums(n+k)，又返回 next_sum

达成一种循环

注意：与递归不同！每次调用返回一个函数，而非一个函数调用。



### Questions

1.7

写一个函数，延迟打印参数，直到下个函数调用才打印参数

```python
def print_delayed(x):
  """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
  >>> f = print_delayed(1)
  >>> f = f(2)
  1
  >>> f = f(3)
  2
  >>> f = f(4)(5)
  3 
  4 
  >>> f("hi") 
  5 
  <function print_delayed> # a function is returned 
  """ 
  def delay_print(y):
    print(x)
    return print_delayed(y)
  return delay_print
```



1.8

```python
def print_n(n):
  """
  >>> f = print_n(2)
  >>> f = f("hi")
  hi
  >>> f = f("hello")
  hello
  >>> f = f("bye")
  done
  >>> g = print_n(1)
  >>> g("first")("second")("third") 
  first 
  done 
  done 
  <function inner_print> 
  """ 
  def inner_print(x):
    if n == 0:			# 或 n <= 0 , 一样的
    	print("done") 
    else:
      print(x) 
    return print_n(n-1)
  return inner_print
```

