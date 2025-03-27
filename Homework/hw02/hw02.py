HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    # 递归边界 / base case
    if x == 0 :
        return 0
    # 递归体, 分情况, 通过传参数使得规模减小
    elif x % 10 == 8 :
        return 1 + num_eights( x // 10)
    else:
        return num_eights( x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(result, i, step):
        if i == n:
            return result
        # 改变方向
        elif i % 8 == 0 or num_eights(i) != 0:
            #  step = 1（增加）时，改为 step = -1（减少），result - step 就变成了 result - (-1)，相当于 result + 1，但可以看作是方向发生了反转，递归时开始减少 result。
            return helper(result - step, i + 1, -step)
        # 继续前进
        else:
            return helper(result + step, i + 1, step)
    return helper(1, 1, 1)


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    ############## 自己思路
    # # base case, 递归边界
    # if n < 10:
    #     return 0
    # # 递归体, 递归树
    # # 1, 最后第 1,2 位差值为 1 或 0, 直接缩小规模
    # elif (n%10) - ((n//10)%10) == 1 or (n%10) - ((n//10)%10) == 0:
    #     return missing_digits(n//10)
    # # 1, 最后第 1,2 位差值大于 1, 缩小规模并加上差值-1(中间差的数字个数)
    # else:
    #     return (n%10) - ((n//10)%10) - 1 + missing_digits(n//10)
    
    ############## 优化思路, 精简代码
    last, secd_last = n % 10, (n // 10) % 10

    if n < 10:
        return 0
    else:
        return max(last - secd_last - 1, 0) + missing_digits(n//10)


def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"
    # 利用 Counting Partitions 思路, next_largest_coin 取下个分割数
    def partitions(total, coin):
        if total < 0:
            return 0
        elif total == 0:
            return 1
        elif coin == None:
            return 0
        else:
            with_coin = partitions(total - coin, coin)
            without_coin = partitions(total, next_largest_coin(coin))
            return with_coin + without_coin
    return partitions(total, 1)

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    # Y 组合子是一种技巧，用匿名函数模拟递归调用, 通过将函数自身作为参数传递，匿名函数可以间接调用自己。
    # 外层 (lambda f: lambda k: f(f, k)) 是一个高阶函数，接受一个函数 f，并返回另一个函数 lambda k: ...，这个返回的函数计算阶乘。
    # 内层的 lambda f, k: ... 是用于实现递归计算阶乘的函数逻辑。
    # 外层用于自己调用自己, 内层用于递归计算, 内层作为外层的参数实现递归
    return (lambda f: 
                lambda k: f(f, k))(
            lambda f, k: 
                k if k == 1 else mul(k, f(f, sub(k, 1)))
    )

    # Alternate solution:
    # return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))

