from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)


def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # 计算各种情况, 再求最小值
    # return min(x**2 + y**2, x**2 + z**2, y**2 + z**2)
    # 计算三者平方和, 再减最大的平方和
    return x**2 + y**2 + z**2 - max(x, y, z)**2


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    # 最大因子, 最少因子 2 * x, x 最大是原数一半. 因此从一半开始倒序找, 第一个就是最大的
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    # if_function 调用, 初始化形参, 并指向三个 function
    # 三个 function 从左向右初始化, 初始化即执行 print
    # print 返回值为 None 
    return if_function(cond(), true_func(), false_func())

# 总结: 
#   1, 从逻辑上 if_statement 和 if_function 一样
#   2, 但是从解释器角度不同. if_function 所有操作树子表达式在应用与结果参数前都会被计算, 因此即使 cond 为 false, true_func 仍然会调用. 相比之下，如果返回 False，if_statement则永远不会调用

def cond():
    "*** YOUR CODE HERE ***"
    return False

def true_func():
    "*** YOUR CODE HERE ***"
    print(42)

def false_func():
    "*** YOUR CODE HERE ***"
    print(47)


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    # 打印冰雹序列
    num = 1
    while n != 1:
        print(n)
        # 若偶数则除2
        if n % 2 == 0:
            n = n // 2
        # 若奇数则乘3加1
        else:
            n = n * 3 + 1
        # 计数
        num = num + 1
    print(n)        # 此时 n 为 1
    return num
