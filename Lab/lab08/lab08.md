### Q1: WWPD: Linked Lists

阅读 `lab08.py` 中的 `Link` 类。确保你理解其中的 doctest。

使用 Ok 测试你对以下 "Python 会输出什么"（WWPD）问题的理解。

```
python3 ok -q link -u --local
```

如果你认为答案是 `<function ...>`，请输入 `Function`；如果会报错，输入 `Error`；如果没有任何输出，输入 `Nothing`。

如果遇到困难，尝试在纸上绘制链表的框图（box-and-pointer diagram），或者使用 `python3 -i lab09.py` 将 `Link` 类加载到解释器中进行调试。



```python
➜  lab08 py3 ok -q link -u                            
=====================================================================
Assignment: Lab 8
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Link > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab09 import *
>>> link = Link(1000)
>>> link.first
? 1000
-- OK! --

>>> link.rest is Link.empty
? True
-- OK! --

>>> link = Link(1000, 2000)
? Nothing
-- Not quite. Try again! --

? Error
-- OK! --

>>> link = Link(1000, Link())
? Nothing
-- Not quite. Try again! --

? Error
-- OK! --

---------------------------------------------------------------------
Link > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab09 import *
>>> link = Link(1, Link(2, Link(3)))
>>> link.first
? 1
-- OK! --

>>> link.rest.first
? 2
-- OK! --

>>> link.rest.rest.rest is Link.empty
? True
-- OK! --

>>> link.first = 9001
>>> link.first
? 9001
-- OK! --

>>> link.rest = link.rest.rest
>>> link.rest.first
? 3
-- OK! --

>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first
? 1
-- OK! --

>>> link = Link(2, Link(3, Link(4)))
>>> link2 = Link(1, link)
>>> link2.first
? 1
-- OK! --

>>> link2.rest.first
? 2
-- OK! --

---------------------------------------------------------------------
Link > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab09 import *
>>> link = Link(5, Link(6, Link(7)))
>>> link                  # Look at the __repr__ method of Link
? 'Link(5, Link(6, Link(7)))'
-- Not quite. Try again! --

? 'Link(5, Link(6, Link(7, '')))'
-- Not quite. Try again! --

? Link(5, Link(6, Link(7)))
-- OK! --

>>> print(link)          # Look at the __str__ method of Link
? Link(5, Link(6, Link(7)))
-- Not quite. Try again! --

? 'Link(5, Link(6, Link(7)))'
-- Not quite. Try again! --

? <5 6 7>
-- OK! --

---------------------------------------------------------------------
OK! All cases for Link unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



```python
➜  lab08 py3 -i lab08.py   

# 判断剩余部分是否也是 Link
>>> link = Link(1000, 2000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/ashing/Study/2语言框架/0SICP(CS61A)/Lab/lab08/lab08.py", line 114, in __init__
    assert rest is Link.empty or isinstance(rest, Link)
AssertionError

# Link() 第一个参数必须有
>>> link = Link(1000,Link())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 1 required positional argument: 'first'

# 调用 __reper__ 是结果，不包括引号 ''
>>> link = Link(5, Link(6, Link(7)))
>>> link
Link(5, Link(6, Link(7)))
>>> 
```



## Linked Lists

### Q2: Convert Link ✅

编写一个函数 `convert_link`，它接受一个链表作为输入，并返回一个包含相同元素的 Python 列表。你可以假设输入链表是浅层的，即其中的元素都不是另一个链表。

尝试分别使用迭代和递归两种方法来解决这个问题！



### Q3: Every Other ❎

实现 `every_other` 函数，该函数接受一个链表 `s`。它会对 `s` 进行原地修改，使得所有奇数索引（基于 0 开始的索引）的元素都从链表中移除。例如：

```
>>> s = Link('a', Link('b', Link('c', Link('d'))))
>>> every_other(s)
>>> s.first
'a'
>>> s.rest.first
'c'
>>> s.rest.rest is Link.empty
True
```

如果 `s` 的元素少于两个，则保持不变。

> 不要返回任何值！`every_other` 应直接修改原链表。



## Trees

### Q4: Cumulative Mul 累积乘积 ❎

编写一个函数 `cumulative_mul`，该函数会修改树 `t`，使得每个节点的标签变为以该节点为根的子树中所有标签的乘积。



# Optional Problems

### Q5: Cycles ✅❎ ❎

`Link` 类可以表示包含循环的链表。也就是说，一个链表可能包含自身作为子链表。

```
>>> s = Link(1, Link(2, Link(3)))
>>> s.rest.rest.rest = s
>>> s.rest.rest.rest.rest.rest.first
3
```

实现 `has_cycle` 函数，判断给定的 `Link` 实例是否包含循环，并返回相应的布尔值。

> *提示*：遍历链表，并尝试记录已经访问过的 `Link` 对象。



作为额外的挑战，请实现 `has_cycle_constant` 函数，并且仅使用[常数空间复杂度](https://composingprograms.netlify.app/2/8#_2-8-5-增长类别)。（如果按照上面的提示实现，空间复杂度将是线性的。）该解法代码较短（少于 20 行），但需要一个巧妙的思路。在向他人请教之前，尝试自己找到解决方案：

```
def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
```





### Q6: Reverse Other ❎

编写一个函数 `reverse_other`，它会修改树，使得*每隔一层*（即奇数深度）的**标签**被反转。例如，

```
Tree(1, [Tree(2, [Tree(4)]), Tree(3)])
```

会变成：

```
Tree(1, [Tree(3, [Tree(4)]), Tree(2)])
```

注意，节点本身*不会*被交换，只有标签会被反转。





