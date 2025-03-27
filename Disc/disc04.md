## 1 Tree Recursion

一个递归体包含多个递归调用

有时候用迭代实现树递归

### 1.1

爬 n 个台阶楼梯，每次只能走 1 或 2 个台阶，共有多少种方式爬上去？



先思考最小情况，递归边界。1或 2。最小为 0 ？为 1？还要考虑 n < 0 特殊情况

```python
def count_stair_ways(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  else:
    return count_stair_ways(n-1) + count_stair_ways(n-2)
```



### 1.2

1.1 问题上，每次可以最多走 k 步

```python
def count_k(n, k):
  if n < 0:
    return 0
  if n == 0:
    return 1
  else:
    sum = 0
    i = 1
    while i <= k:
      sum += count_k(n - i, k)
      i += 1
    return sum
```



## 2 List

值类型任意



### List 切片

start

end

step size，为负数时？

创建新的



### List 生成式



### Questions

### 2.1

1

3

5

False

True

2



### 2.2

偶数元素，乘以索引

```python
def even_weighted(s):
  return [x * index(s,x) for x in s if index(s,x) % 2 == 0 ]
思路可以， 但无法直接取得索引


关键：以 i 为迭代对象，而非 s
def even_weighted(s):
  return [i * s[i] for i in range(len(s)) if i % 2 == 0]

必须是 range(len(s)) 而不能是 len(s)

等价于：

def even_weighted(s):
  result = []
  for i in range(len(s)):
    if i % 2 == 0:
    	result = result + [s[i] * i]
  return result
```



### 2.3

编写一个函数，该函数接受列表并返回可以使用列表的非连续元素形成的最大乘积。输入列表将仅包含大于或等于 1 的数字。



```python
def max_product(s):
  # 递归边界
  if s == []:
    return 0
  elif len(s) == 1:
    return s[0]
  # 树递归, 选择或不选择第一个元素
  else:
    return max(max_product(s[1:]), s[0] * max_product(s[2:]))
```

