this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def adder(b):
        nonlocal a
        result = a + b
        a += 1
        return result
    return adder


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"

    cur = 0
    next = 1
    def fib():
        nonlocal cur, next
        re = cur
        # 更新 cur next
        cur, next = next, cur + next
        return re
    return fib


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    # def replace(l, i, elem):
    #     l.pop(i)
    #     l.insert(i, elem)

    # 不返回 new list
    # return [lst.insert(i, elem) for i in range(len(lst)) if lst[i] == entry]

    # for index, value in enumerate(lst):
    #     if value == entry:
    #         if lst[index] == lst[index-1]:
    #             pass
    #         else:
    #             lst.insert(index, elem)
    # return lst

    # 每次重新计算 index
    i = 0
    while i < len(lst):
        if lst[i] == entry:
            # insert 是向 index 前面插入数据
            lst.insert(i + 1, elem)
            if entry == elem:
                i += 1
        i += 1
    return lst

