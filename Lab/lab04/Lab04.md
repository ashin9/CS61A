## Lists Practice

### Q1：List Indexing

注意点

- 索引从 0 开始
- 列表嵌套

```python
py3 ok -q list-indexing -u 
=====================================================================
Assignment: Lab 4
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
List Indexing > Suite 1 > Case 1
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> x = [1, 3, [5, 7], 9] # Write the expression that indexes into x to output the 7
? x[2][1]
-- OK! --

>>> x = [[3, [5, 7], 9]] # Write the expression that indexes into x to output the 7
? x[0][1][1]
-- OK! --

---------------------------------------------------------------------
List Indexing > Suite 2 > Case 1
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> lst = [3, 2, 7, [84, 83, 82]]
>>> lst[4]
? Error
-- OK! --

>>> lst[3][0]
? 84
-- OK! --

---------------------------------------------------------------------
OK! All cases for List Indexing unlocked.

Performing authentication
Please enter your school email (.edu): ^C%
```



## Recursion

### Q2: Skip Add

递归求解和，规模跳着减小，注意边界

### Q3: Summation

递归求解和，每次应用传入的函数

## Tree Recursion

### Q4: Insect Combinatorics

递归求解路径条数问题

### Q5: Maximum Subsequence

固定长度下，求解最大子序列（子序列不一定连续）



## Optional Questions

### Q6: Add Characters

递归求解，序列与其子序列所差字母，顺序为从左向右插入的顺序，若序列多个字符匹配子序列则以第一个字母为准

挨个字母判断，若不同则返回该字母 + w2 后移一位；若相同则都后移一位；若 w1 为空则返回 w2（不同字母追加 w2 剩下的）