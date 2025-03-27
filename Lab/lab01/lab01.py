def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    # 方法 1:递归
    # 递归边界
    if k==0:
        return 1
    # 递归体
    else:
        return n * falling(n-1, k-1)
    
    # 方法 2: 迭代
    # product = n
    # for _ in range(k-1):
    #     n = n - 1
    #     product *= n
    # return product

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"

    sum = 0
    while y:
        # 取余来取到末位数字, 然后累加
        # sum += y % 10
        # 整除来舍去末位数字
        # y = y // 10

        # 多重赋值表达式, 先计算完等号右边的再与左边名称绑定, 可看做两条语句同时执行, 因此不会动态事实更新值来计算另一条
        sum, y = sum + y % 10, y // 10
    return sum


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"

    # 方法 1: 转为字符串用切片处理
    # s = str(n)
    # for i in range(0, len(s) - 1):
    #     if s[i:i+2] == '88':
    #         return True
    # return False

    # 方法 2: 若不转换类型, 纯数字处理
    # while n:
    #     # 模, 来取末位数字
    #     n1 = n % 10
    #     # 先整除再取模, 来取倒数第二位数字
    #     n2 = (n // 10) % 10
    #     # 判断两位是否都为 8, 否则就整除 10 舍去末位数字
    #     if n1 == 8 and n2 == 8:
    #         return True
    #     else:
    #         n = n // 10
    # return False

    # 官方方法: 记录前一位是否为 8
    prev = False
    while n > 0:
        last = n % 10
        # 判断是否有连 8
        if last == 8 and prev:
            return True
        
        # 记录前一位是否为 8
        elif last == 8:
            prev = True
        else:
            prev = False
        
        n = n // 10
    return False