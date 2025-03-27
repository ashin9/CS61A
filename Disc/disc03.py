
def mul_recur(a, b) :
    # 递归边界
    if a == 1:
        return b
    # 递归体
    return b + mul_recur(a-1, b)

print(mul_recur(3, 5))


# 记录递归次数方法: 1, 传参记录; 2, 全局变量; 3, 触发器; 4,返回值记录
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

# 官方答案: 4, 返回值记录递归次数
def hailstone_recur(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone_recur(n//2)
    else:
        return 1 + hailstone_recur(n*3+1)

print(hailstone_recur(10))


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