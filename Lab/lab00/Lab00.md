## 环境

bash

python



## 命令

ls

cd

mkdir

mv



## 基础知识

程序由表达式和语句组成，表达式是一段求值的代码，语句是程序中使某些事情发生的一行或多行代码。

原始表达式，只需一步求值的

- 如：数字和 bool 表达式，对自己求值

算数表达式，+、-、*、/

- % 模，取余

- // 整除，向下取整
- ** 指数

赋值，对 `=` 右侧表达式运算，将其值与左侧名称绑定



## 解锁测试

### 问题

```
ModuleNotFoundError: No module named 'urllib3.packages.six.moves
Python 3.7 or later (ideally Python 3.9)
切换为 python3.7 - 3.9
```



没有重新赋值，则值不变

```
> x = 20
> x + 2
22
> x
20

> y = 8
> y * 2
> y // 4
> y + x
22
```



```shell
➜  lab00 py3 ok -q python-basics -u
=====================================================================
Assignment: Lab 0
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Python Basics > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> 10 + 2
? 12
-- OK! --

>>> 7 / 2
? 3.5
-- OK! --

>>> 7 // 2
? 3
-- OK! --

>>> 7 % 2			# 7 modulo 2, the remainder when dividing 7 by 2.
? 1
-- OK! --

---------------------------------------------------------------------
Python Basics > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = 20
>>> x + 2
? 22
-- OK! --

>>> x
? x
-- Not quite. Try again! --

? 'x'
-- Not quite. Try again! --

? 0
-- Not quite. Try again! --

? 22
-- Not quite. Try again! --

? 20
-- OK! --

>>> y = 5
>>> y = y + 3
>>> y * 2
? 16
-- OK! --

>>> y = y // 4
>>> y + x
? 24
-- Not quite. Try again! --

? 22
-- OK! --

---------------------------------------------------------------------
OK! All cases for Python Basics unlocked.
```



## 理解问题

`"""` docstring，注释？描述 function 作用

`>>>` doctests，假设在解释器中输入这段代码



## 编写代码

```python
def twenty_twenty():
    """Come up with the most creative expression that evaluates to 2020,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty()
    2020
    """
    return abs(1+2-int(3*4/5%6//7**8)-2023)
```



## 运行测试

## 提交作业

```shell
python3 ok --submit
```



## 有用帮助

```shell
# 查看帮助
python3 ok --help
# 交互 py
python3 -i
# 运行特定 doctest
python3 -m doctest
```

