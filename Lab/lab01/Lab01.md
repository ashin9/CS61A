## What Would Python Display? (Part 1)

## Q1: WWPD: Control

```shell
py3 ok -q control -u --local
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Control > Suite 1 > Case 1
(cases remaining: 5)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def xk(c, d):
...     if c == 4:
...         return 6
...     elif d >= 4:
...         return 6 + 7 + c
...     else:
...         return 25
>>> xk(10, 10)
? 23
-- OK! --

>>> xk(10, 6)
? 23
-- OK! --

>>> xk(4, 6)
? 6
-- OK! --

>>> xk(0, 0)
? 25
-- OK! --

---------------------------------------------------------------------
Control > Suite 1 > Case 2
(cases remaining: 4)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def how_big(x):
...     if x > 10:
...         print('huge')
...     elif x > 5:
...         return 'big'
...     elif x > 0:
...         print('small')
...     else:
...         print("nothin")
>>> how_big(7)
? big
-- Not quite. Try again! --

? None
-- Not quite. Try again! --

? 
-- Not quite. Try again! --

? 'big'
-- OK! --

>>> how_big(12)
? huge
-- OK! --

>>> how_big(1)
? small
-- OK! --

>>> how_big(-1)
? nothin
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> n = 3
>>> while n >= 0:  # If this loops forever, just type Infinite Loop
...     n -= 1
...     print(n)
(line 1)? 2
(line 2)? 1
(line 3)? 0
(line 4)? 
-- Not quite. Try again! --

(line 1)? 2
(line 2)? 1
(line 3)? 0
(line 4)? -1
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = 28
>>> while positive: # If this loops forever, just type Infinite Loop
...    print("positive?")
...    positive -= 3
? Infinite Loop
-- OK! --

---------------------------------------------------------------------
Control > Suite 2 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> positive = -9
>>> negative = -12
>>> while negative: # If this loops forever, just type Infinite Loop
...    if positive:
...        print(negative)
...    positive += 3
...    negative += 3
(line 1)? -12
(line 2)? -9
(line 3)? -6
-- OK! --

---------------------------------------------------------------------
OK! All cases for Control unlocked.
```



### 易错和迷惑处

返回值问题

```python
def how_big(x):
  return 'big'

>>> how_big()
'big'            # 而非 big
```

布尔表达式问题，数字时 0 为 false，非 0 为 true

-  0、 `None` 和布尔值 `False`，**所有其他数字都是真值**

```python
i = 28
while i: 				# 0 表示 false，非 0 表示 true，因此是死循环
  i -= 3
```



## Q2: WWPD: Veritasiness



```python
lab01 python3 ok -q short-circuit -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 13
? true
-- Not quite. Try again! --

? True
-- Not quite. Try again! --

? 13
-- OK! --

>>> False or 0
? 0
-- OK! --

>>> not 10
? false
-- Not quite. Try again! --

? False
-- OK! --

>>> not None
? True
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> True and 1 / 0 and False  # If this errors, just type Error.
? False
-- Not quite. Try again! --

? Error
-- OK! --

>>> True or 1 / 0 or False  # If this errors, just type Error.
? True
-- OK! --

>>> True and 0  # If this errors, just type Error.
? 0
-- OK! --

>>> False or 1  # If this errors, just type Error.
? 1
-- OK! --

>>> 1 and 3 and 6 and 10 and 15  # If this errors, just type Error.
? 15
-- OK! --

>>> -1 and 1 > 0 # If this errors, just type Error.
? True
-- OK! --

>>> 0 or False or 2 or 1 / 0  # If this errors, just type Error.
? 2
-- OK! --

---------------------------------------------------------------------
Veritasiness > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> not 0
? True
-- OK! --

>>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
? 1
-- OK! --

>>> 1/0 or True  # If this errors, just type Error. If this is blank, just type Nothing.
? Error
-- OK! --

>>> (True or False) and False  # If this errors, just type Error. If this is blank, just type Nothing.
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for Veritasiness unlocked.
```

### 易错和迷惑处

短路计算原则

```python
>>> True and 13
? 13
```

not 计算原则，只输出布尔

```python
>>> not 10
? false			# 首字母不是小写
-- Not quite. Try again! --
? False
```

错误问题，1 / 0 还是会有检查错误的机制的

```python
>>> True and 1 / 0 and False  # If this errors, just type Error.
? False
-- Not quite. Try again! --

? Error
-- OK! --
```



## Q3: Debugging Quiz!



```shell
lab01 python3 ok -q debugging-quiz -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 1
(cases remaining: 12)

Q: In the following traceback, what is the most recent function call?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) g(x + x, x)
1) h(x + y * 5)
2) f("hi")
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 2
(cases remaining: 11)

Q: In the following traceback, what is the cause of this error?
Traceback (most recent call last):
    File "temp.py", line 10, in <module>
      f("hi")
    File "temp.py", line 2, in f
      return g(x + x, x)
    File "temp.py", line 5, in g
      return h(x + y * 5)
    File "temp.py", line 8, in h
      return x + 0
  TypeError: must be str, not int
Choose the number of the correct choice:
0) the code looped infinitely
1) there was a missing return statement
2) the code attempted to add a string to an integer
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 3
(cases remaining: 10)

Q: How do you write a doctest asserting that square(2) == 4?
Choose the number of the correct choice:
0) def square(x):
       '''
       square(2)
       4
       '''
       return x * x
1) def square(x):
       '''
       input: 2
       output: 4
       '''
       return x * x
2) def square(x):
       '''
       >>> square(2)
       4
       '''
       return x * x
3) def square(x):
       '''
       doctest: (2, 4)
       '''
       return x * x
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 4
(cases remaining: 9)

Q: When should you use print statements?
Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 1 2 3
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 1,2,3,
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 1,2,3
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0 1 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0,1,2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0,2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 5
(cases remaining: 8)

Q: How do you prevent the ok autograder from interpreting print statements as output?
Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You don't need to do anything, ok only looks at returned values, not printed values
1) Print with # at the front of the outputted line
2) Print with 'DEBUG:' at the front of the outputted line
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 6
(cases remaining: 7)

Q: What is the best way to open an interactive terminal to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits --trace
1) python3 -i lab01.py
2) python3 ok -q sum_digits -i
3) python3 ok -q sum_digits
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 7
(cases remaining: 6)

Q: What is the best way to look at an environment diagram to investigate a failing test for question sum_digits in assignment lab01?
Choose the number of the correct choice:
0) python3 ok -q sum_digits
1) python3 ok -q sum_digits --trace
2) python3 ok -q sum_digits -i
3) python3 -i lab01.py
? 1
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 8
(cases remaining: 5)

Q: Which of the following is NOT true?
Choose the number of the correct choice:
0) It is generally bad practice to release code with debugging print statements left in
1) Debugging is not a substitute for testing
2) It is generally good practice to release code with assertion statements left in
3) Code that returns a wrong answer instead of crashing is generally better as it at least works fine
4) Testing is very important to ensure robust code
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 9
(cases remaining: 4)

Q: You get a SyntaxError. What is most likely to have happened?
Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) You forgot a return statement
2) Your indentation mixed tabs and spaces
3) You had an unmatched parenthesis
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) You forgot a return statement
2) Your indentation mixed tabs and spaces
3) You had an unmatched parenthesis
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 10
(cases remaining: 3)

Q: You get a IndentationError. What is most likely to have happened?
Choose the number of the correct choice:
0) You had an unmatched parenthesis
1) You typed a variable name incorrectly
2) Your indentation mixed tabs and spaces
3) You forgot a return statement
? 2
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 11
(cases remaining: 2)

Q: You get a TypeError: ... 'NoneType' object is not ... . What is most likely to have happened?
Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) Your indentation mixed tabs and spaces
2) You had an unmatched parenthesis
3) You forgot a return statement
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) Your indentation mixed tabs and spaces
2) You had an unmatched parenthesis
3) You forgot a return statement
? 3
-- OK! --

---------------------------------------------------------------------
debugging-quiz > Suite 1 > Case 12
(cases remaining: 1)

Q: You get a NameError. What is most likely to have happened?
Choose the number of the correct choice:
0) You had an unmatched parenthesis
1) You typed a variable name incorrectly
2) You forgot a return statement
3) Your indentation mixed tabs and spaces
? 1
-- OK! --

---------------------------------------------------------------------
OK! All cases for debugging-quiz unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```

### 易错和迷惑处

什么时候用 print？检查代码中某些位置的变量值

```shell
Q: When should you use print statements?
Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) To investigate the values of variables at certain points in your code
1) For permanant debugging so you can have long term confidence in your code
2) To ensure that certain conditions are true at certain points in your code
? 0
-- OK! --
```

syntax 错误，不匹配的括号

```shell
debugging-quiz > Suite 1 > Case 9
(cases remaining: 4)

Q: You get a SyntaxError. What is most likely to have happened?
Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) You forgot a return statement
2) Your indentation mixed tabs and spaces
3) You had an unmatched parenthesis
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) You forgot a return statement
2) Your indentation mixed tabs and spaces
3) You had an unmatched parenthesis
? 3
-- OK! --
```

TypeError: ... 'NoneType' object is not ...，忘记返回

```shell
debugging-quiz > Suite 1 > Case 11
(cases remaining: 2)

Q: You get a TypeError: ... 'NoneType' object is not ... . What is most likely to have happened?
Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) Your indentation mixed tabs and spaces
2) You had an unmatched parenthesis
3) You forgot a return statement
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) You typed a variable name incorrectly
1) Your indentation mixed tabs and spaces
2) You had an unmatched parenthesis
3) You forgot a return statement
? 3
-- OK! --
```



## Coding Practice

## Q4: Falling Factorial

两种方法，递归或迭代



## Q5: Sum Digits

取余来取到末位数字, 然后累加

整除来舍去末位数字





## Extra Practice

## What Would Python Display? (Part 2)

## Q6: WWPD: What If？



```shell
lab01 python3 ok -q if-statements -u
=====================================================================
Assignment: Lab 1
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
What If? > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def ab(c, d):
...     if c > 5:
...         print(c)
...     elif c > 7:
...         print(d)
...     print('foo')
>>> ab(10, 20)
(line 1)? 10
(line 2)? foo
-- OK! --

---------------------------------------------------------------------
What If? > Suite 1 > Case 2
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> def bake(cake, make):
...    if cake == 0:
...        cake = cake + 1
...        print(cake)
...    if cake == 1:
...        print(make)
...    else:
...        return cake
...    return make
>>> bake(0, 29)
(line 1)? 1
(line 2)? 29
(line 3)? 0
-- Not quite. Try again! --

(line 1)? 1
(line 2)? 29
(line 3)? 29
-- OK! --

>>> bake(1, "mashed potatoes")
(line 1)? mashed phtatoes
-- Not quite. Try again! --

(line 1)? mashed potatoes
(line 2)? mashed potatoes
-- Not quite. Try again! --

(line 1)? mashed potatoes
(line 2)? "mashed potatoes"
-- OK! --

---------------------------------------------------------------------
OK! All cases for What If? unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```

### 易错和迷惑处

分支选择，进了一个分支，则另外的分支则不会进入

退出分支选择，顺序执行后续的分支选择

解释器调用函数，打印返回值，若是字符则打印带引号的字符



## More Coding Practice

## Q7: Double Eights

转字符串

遍历字符串

切片，每次切 2 字符，判断是否为 88
