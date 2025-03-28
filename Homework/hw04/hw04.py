def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message == 'deposit':
            balance += amount
            return balance
        elif message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            else:
                balance -= amount
                return balance
        else:
            return 'Invalid message'
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Frozen account. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    # error_time 可以用 error_pass 长度来计算
    # error_pass = []
    # error_time = 0
    # def withdraw(amount, inpass):
    #     nonlocal balance, password, error_pass, error_time
        
    #     if len(error_pass) >= 3:
    #         return "Frozen account. Attempts: " + str(error_pass)

    #     if inpass != password:
    #         error_time += 1
    #         error_pass.append(inpass)
    #         return 'Incorrect password'
        
    #     if amount > balance:
    #         return 'Insufficient funds'
    #     else:
    #         balance -= amount
    #         return balance
    # return withdraw

    error_pass = []
    def withdraw(amount, inpass):
        nonlocal balance, password, error_pass
        
        if len(error_pass) >= 3:
            return "Frozen account. Attempts: " + str(error_pass)

        if inpass != password:
            error_pass.append(inpass)
            return 'Incorrect password'
        
        if amount > balance:
            return 'Insufficient funds'
        else:
            balance -= amount
            return balance
    return withdraw


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> s = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s, 2)
    9
    >>> s2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(s2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    # 不是连续出现的情况
    # dict = {}
    # for i in t:
    #     if i in dict.keys():
    #         dict[i] += 1
    #     else:
    #         dict[i] = 0
        
    #     if dict[i] == 2:
    #         return i

    # 双指针思路, 用 pre 记录前面的值
    count = 1
    pre = None

    for i in t:
        if i == pre:
            count += 1
        # 更新 pre, 并更新 count
        else:
            pre = i
            count = 1
        
        if count == k:
            return i

        

def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order.

    >>> perms = permutations([100])
    >>> type(perms)
    <class 'generator'>
    >>> next(perms)
    [100]
    >>> try: #this piece of code prints "No more permutations!" if calling next would cause an error
    ...     next(perms)
    ... except StopIteration:
    ...     print('No more permutations!')
    No more permutations!
    >>> sorted(permutations([1, 2, 3])) # Returns a sorted list containing elements of the generator
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    >>> sorted(permutations((10, 20, 30)))
    [[10, 20, 30], [10, 30, 20], [20, 10, 30], [20, 30, 10], [30, 10, 20], [30, 20, 10]]
    >>> sorted(permutations("ab"))
    [['a', 'b'], ['b', 'a']]
    """
    "*** YOUR CODE HERE ***"
    if not seq:
        yield []
    else:
        # 首个和剩余
        first, last = seq[0], seq[1:]
        # 递归全排列剩余部分
        for last_seq in permutations(last):
            # 每个空插入第一个元素
            for i in range(len(seq)):
                # insert 方法修改原 list 下次循环可能被更改, 导致后续排列不正确, 并且 insert 返回 None, 而不是返回 list 
                # yield last_seq.insert(i, first)
                # 构建并返回新 list
                yield last_seq[:i] + [first] + last_seq[i:]


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Frozen account. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    # 尝试用 old_pass 访问账户, 保存返回值, 看返回值是否为字符(或数字)? 是数字说明密码正确, 否则密码错误或冻结了
    re = withdraw(0, old_pass)
    # if not isinstance(re, (int)):
    if type(re) == str:
        return re
    else:
        def join_withdraw(amount, password):
            if password == new_pass:
                return withdraw(amount, old_pass)
            else:
                return withdraw(amount, password)
        return join_withdraw

def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    # for i in range(m):
    #     yield next(naturals()) % m == i

    # 两个生成器函数嵌套

    # 每个生成器安装特定模式生成
    def gen(i):
        for e in naturals():
            if e % m == i:
                yield e
    
    # 生成 m 个生成器
    for i in range(m):
        yield gen(i)


def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

