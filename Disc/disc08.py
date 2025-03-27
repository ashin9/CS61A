# 1.1 
class A():
    def __init__(self, x):
        self.x = x 
        
        def __repr__(self):
            return self.x 
        def __str__(self):
            return self.x * 2

class B():
    def __init__(self):
        print("boo!") 
        self.a = [] 
    
    def add_a(self, a):
        self.a.append(a) 
    
    def __repr__(self):
        print(len(self.a))
        ret = ""
        for a in self.a:
            ret += str(a) 
        return ret


class Link:
    empty = () 
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link) 
        self.first = first 
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest) 
        else:
            rest_str = '' 
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<' 
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest 
        return string + str(self.first) + '>'

# 2.1 ✅ 编写函数，输入 linked list，返回元素和，假设所有元素为整数
def sum_nums(lnk):
    num = 0
    while lnk is not Link.empty:
      num += lnk.first
      lnk = lnk.rest
    return num

# 2.2 ❎ ⭐️ 输入 linked list 的 list，返回元素对应乘积，返回新 linked list
# 如果并非所有的 Link 对象长度相等，则返回一个长度与最短链表相同的链表。你可以假设这些 Link 对象是浅层链表，并且 `lst of lnks` 至少包含一个链表。
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """ 
    # Note: you might not need all lines in this skeleton code


    # 想不出如何构建 link
    # new_lnk = Link(1)
    # cur = new_lnk

    # for l in lst_of_lnks:
    #     if l.first:
    #         cur.first *= l.first
    #     else:
    #         break
    #     cur.rest = Link(1)
    #     cur = cur.rest

    #     l = l.rest

    product = 1
    for l in lst_of_lnks:
        if l is Link.empty:
            return Link.empty
        product *= l.first
    lst_of_lnks_rest = [l.rest for l in lst_of_lnks]

    # 递归构建方法, 不熟悉!
    return Link(product, multiply_lnks(lst_of_lnks_rest))


# 2.3 ✅ 编写一个递归函数 `flip_two`，该函数接受一个链表 `lnk` 作为输入，并修改 `lnk`，使得每一对相邻的元素互换位置。
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk.rest is not Link.empty:
        lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
        flip_two(lnk.rest.rest)

# 2.4 ✅ ❎ 实现 `filter_link`，该函数接受一个链表 `link` 和一个函数 `f`，返回一个生成器，该生成器会产生 `link` 中所有使 `f` 返回 `True` 的值。
# 尝试使用 `while` 循环和不使用任何形式的迭代两种方法来实现此函数。
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    # 迭代
    # while link is not Link.empty:
    #     if f(link.first):
    #         yield link.first
    #     link = link.rest

    # 非迭代, 递归实现
    # 递归边界
    if link is Link.empty:
        return 
    # 递归体
    if f(link.first):
        # link.first 不是可迭代类型, 不能 yield from link.first
        yield link.first
    # 为什么最后要 yeld from ? yield from 可以简化递归生成器的写法，相当于递归调用 filter_link，把后续所有符合条件的值直接交给上层生成器 yield
    yield from filter_link(link.rest, f)


# 3 请注意，通过 Class 实现，可以使用 attribute assignment 来改变一棵树，这在前面的 lists 实现中是不可能的。
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    
    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

# 3.1 ✅ 定义一个函数 `make_even`，该函数接收一棵值为整数的树 `t`，并对这棵树进行原地修改（mutate）。使得树中所有奇数值加 1（变成偶数），而所有偶数值保持不变。
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    # 递归边界, 树 Tree 并不使用 Link.empty 这种表示空的结构，这里的递归终止条件是不必要的，甚至是错误的。Tree 的递归结构是通过 branches，如果 branches 为空，它就自然不会再递归了。
    # if t is Link.empty:
    #     return 

    # 操作
    if t.label % 2 == 1:
        t.label += 1
    # 递归所有节点
    for b in t.branches:
        make_even(b)


# 3.2 ✅ 定义一个函数 square_tree(t)，它会将非空树 t 中的每个值都平方。你可以假设树中每个值都是数字。
def square_tree(t):
    """
    Mutates a Tree t by squaring all its elements.
    """
    t.label *= t.label
    
    for b in t.branches:
        square_tree(b)

# 3.3 ❎ ⭐️⭐️ 定义一个过程 `find_paths`，它接收一棵树 `t` 和一个值 `entry`，返回一个“路径列表的列表”。每个路径是一个列表，包含从树 `t` 的根节点到值为 `entry` 的节点所经过的所有节点。你可以按任意顺序返回这些路径。
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = [] 
    
    # 递归边界
    if t.label == entry:
        paths.append([t.label])
    # 递归体
    for b in t.branches:
        for path in find_paths(b, entry):
            # paths.append([b.label] + path)
            # 应该是 t.label
            paths.append([t.label] + path)

    return paths

# 3.4 编写一个函数，将两棵树 `t1` 和 `t2` 中对应节点的值通过 `combiner` 函数进行合并。假设 `t1` 和 `t2` 具有相同的结构。这个函数应该返回一棵新的树。
# 提示：可以考虑使用 `zip()` 函数。`zip()` 返回一个迭代器，它将传入的可迭代对象中的第一个元素配对组成第一个元组，第二个元素配对组成第二个元组，依此类推。
from operator import mul
def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    # 思路: 递归合并
    # 递归边界, 一个节点
    # if t1.is_leaf() and t2.is_leaf():
    #     return Tree(combiner(t1.label, t2.label))
    # 递归体, 合并子树
    combined = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), combined)

# 3.5 实现一个交替树映射函数，该函数接收一个函数和一个树作为输入，从根节点开始，将该函数应用于树的每一层交替层级上的所有数据。
# 用闭包传递参数控制奇偶数, 实现 __repr__ 方法
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)]) 
    """
    
    # 在原数据修改
    # def tree_map(t, map_fn, need_map=True):
    #     if need_map:
    #         t.label = map_fn(t.label)
    #     for b in t.branches:
    #         tree_map(b, map_fn, not need_map)
    # tree_map(t, map_fn)

    # 构造新的 tree
    def tree_map(t, map_fn, need_map=True):
        if need_map:
            t.label = map_fn(t.label)
        # new_label = map_fn(t.label) if need_map else t.label
        return Tree(t.label, [tree_map(b, map_fn, not need_map) for b in t.branches])
    
    return tree_map(t, map_fn)