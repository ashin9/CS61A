## Nonlocal Codewriting

### Q1: Make Adder Increasing ✅

编写一个函数，该函数接受一个整数 `a` 并返回一个**一元函数**。

返回的函数应接受一个值 `b`，并且**第一次调用**时返回 `a + b`，类似于 `make_adder`。

然而，**第二次调用**时，它应该返回 `a + b + 1`，**第三次调用**时返回 `a + b + 2`，以此类推。



### Q2: Next Fibonacci ✅

编写一个函数 `make_fib`，它返回一个**函数**，该函数**每次被调用时**都会返回**下一个斐波那契数**。

（斐波那契序列从 `0` 开始，接着是 `1`，然后每个元素都是前两个元素的和。）

要求：

- 使用 `nonlocal` 语句！
- **不能**使用 Python 的列表 (`list`) 来解决这个问题。



## Mutability

### Q3: List-Mutation ❎

测试你对**列表变异（list mutation）**的理解，回答以下问题。

Python 会显示什么？如果不确定，可以在解释器中输入代码进行测试！

**注意**：如果 Python 不会输出任何内容，请输入 **"Nothing"**。



```python
➜  lab06 py3 ok -q list-mutation -u                
=====================================================================
Assignment: Lab 6
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
List Mutation > Suite 1 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> lst = [5, 6, 7, 8]
>>> lst.append(6)
? [5, 6, 7, 8, 6]
-- Not quite. Try again! --

? nothing
-- OK! --

>>> lst
? [5, 6, 7, 8, 6]
-- OK! --

>>> lst.insert(0, 9)
>>> lst
? [9, 5, 6, 7, 8, 6]
-- OK! --

>>> x = lst.pop(2)
>>> lst
? [9, 5, 7, 8, 6]
-- OK! --

>>> lst.remove(x)
>>> lst
? nothing
-- Not quite. Try again! --

? [9, 5, 7, 8, 6]
-- Not quite. Try again! --

? NameError
-- Not quite. Try again! --

? []
-- Not quite. Try again! --

? 9, 5, 7, 8, 6]
-- Not quite. Try again! --

? [9, 5, 7, 8]
-- OK! --

>>> a, b = lst, lst[:]
>>> a is lst
? True
-- OK! --

>>> b == lst
? True
-- OK! --

>>> b is lst
? False
-- OK! --

---------------------------------------------------------------------
OK! All cases for List Mutation unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



```python
>>> lst.append(6)
无回显

>>> lst
? [9, 5, 6, 7, 8, 6]

x = lst.pop(2)
x = 返回所 pop 的元素 6
```



### Q4: Insert Items ❎

编写一个函数，该函数接收一个列表 `lst`，一个参数 `entry`，以及另一个参数 `elem`。

此函数会遍历 `lst` 中的每个元素，并检查它是否等于 `entry`。
如果找到了等于 `entry` 的元素，则在该元素**之后**插入 `elem`。

在函数执行结束时，应返回修改后的 `lst`。
使用**列表变异（list mutation）**来修改原始列表，不能创建或返回新的列表。

⚠ **注意**：

- 如果 `entry` 和 `elem` 是**相同的值**，要小心避免进入**无限循环**（不断插入相同的值）。
- 如果你的代码运行时间超过几秒钟，可能是进入了无限循环，请检查插入逻辑。



