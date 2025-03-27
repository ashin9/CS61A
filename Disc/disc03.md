## Recursion

### 通用三步

1，计算递归边界，通常是最小值情况

2，递归调用，传入更小的参数

3，解决问题



## Questions

### 1.1 用递归方式计算两个正整数乘积

提示：`5*3 = 5 + 5*2 = 5 + 5 + 5*1`

```python
def mul_recur(a, b) :
    # 递归边界
    if a == 1:
        return b
    # 递归体
    return b + mul_recur(a-1, b)

print(mul_recur(3, 5))
```



### 1.2 画环境图

```python
def rec(x, y):
  if y > 0:
    return x * rec(x, y - 1) 
  return 1
rec(3, 2)
```



```shell
----Global----
rec -> func
----rec(3,2)----
x = 3
y = 2
return 3 * 
----rec(3,1)----
x = 3
y = 2
return 3 * 
----rec(3,0)----
x = 3
y = 0
return 1

----rec(3,1)----
x = 3
y = 2
return 3 * 1

----rec(3,2)----
x = 3
y = 2
return 3 * 3

----Global----
9
```



### 1.3 递归方式实现 hailstone

输入 n，若为偶数则除以 2，若为奇数则 * 3 + 1，直至 n 为 1，返回变换次数

```python
# 记录递归次数方法: 1, 传参记录; 2, 全局变量; 3, 触发器
def hailstone_recur(n, num=1):
    if n == 1:
        return num
    elif n % 2 == 0:
        num += 1
        return hailstone_recur(n//2, num)
    else:
        num += 1
        return hailstone_recur(n*3+1, num)

print(hailstone_recur(10))
```





### 1.4 递归实现合并两个数字为一个降序大数字

与 0 合并，视为没数字

```python
def merge(n1, n2):
    # 递归边界
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    # 递归体
    elif n1 % 10 < n2 % 10:
        # 通过参数减小规模, 不同于常见的-1, 而是运算变换
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    
print(merge(622,41))
```

递归边界能想到

如何减小规模想不到，必然是通过传参来减小规模，参数如何变？

返回值如何计算得到目标值？



### 1.5 递归实现计算 f 应用于参数的次数

定义一个 make fn repeater 函数,该函数接受一个单参数函数 f 和一个整数 x,它应该返回另一个函数,该函数接受一个参数,另一个整数。该函数返回将 f 应用于 x 的次数的结果。

```python
def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(n):
        if n == 0:
            return x
        else:
            return f(repeat(n-1))
    return repeat

incr_1 = make_func_repeater(lambda x: x + 2, 1)
print(incr_1(5))
```

递归体，如何缩小？参数减小

如何运算得到结果？通过 f function



### 1.6 递归实现判断是否为素数



```python
def primer_helper(n, i=2):
    # 特殊情况
    if n == 1:
        return False
    
    # 递归边界
    if i == n:
        return True
    elif n % i == 0:
        return False
    # 递归体, 参数变换规模
    else:
        return primer_helper(n, i+1)

print(primer_helper(16))


# 官方答案
# def prime_helper(index):
#     if index == n:
#         return True 
#     elif n % index == 0 or n == 1:
#         return False 
#     else:
#         return prime_helper(index + 1) 
#     return prime_helper(2)
```

