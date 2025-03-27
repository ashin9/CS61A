class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.stock = 0
        self.balance = 0

    # 出售    
    def vend(self):
        if self.stock == 0:
            return 'Inventory empty. Restocking required.'
        elif self.balance < self.price:
            return 'You must add ${} more funds.'.format(self.price - self.balance)
        else:
            if self.balance == self.price:
                info = 'Here is your {}.'.format(self.name) 
            else:
                info =  'Here is your {} and ${} change.'.format(self.name, self.balance - self.price)
            # 卖出商品后, 库存减一, 并退出余额
            self.stock -= 1
            self.balance = 0
            return info
    # 投钱
    def add_funds(self, money):
        if self.stock == 0:
            return 'Inventory empty. Restocking required. Here is your ${}.'.format(money)
        else:
            self.balance += money
            return 'Current balance: ${}'.format(self.balance)

    # 进货
    def restock(self, stock):
        self.stock += stock
        return 'Current {} stock: {}'.format(self.name, self.stock)

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2020
    >>> dime = mint.create(Dime)
    >>> dime.year
    2020
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2020
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    current_year = 2020

    def __init__(self):
        self.year = 0
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        return kind(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        if Mint.current_year - self.year > 50:
            # (Mint.current_year - self.year) 是超过了多少年, 再 -50 才是超过 50 多少
            return self.cents + Mint.current_year - self.year - 50
        else:
            return self.cents

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


import math

def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    """
    "*** YOUR CODE HERE ***"

    # 递归方案
    # if n == 0:
    #     return Link.empty
    # elif n < 10:
    #     return Link(n) 
    # else: 
    #     # log10 向下去整, 得到位数
    #     first = n // 10 ** int((math.log10(n)))
    #     last = n - first * 10 ** int((math.log10(n)))
    #     return Link(first, store_digits(last))

    # 非递归方案, 没想到, 其实更简单的思路
    result = Link.empty
    while n > 0:
        result = Link(n % 10, result)
        n = n // 10
    return result


# 搜索二叉树的最小值
# def bst_min(t):
#     if t is None:
#         return None
#     while t.branches:
#         t = t.branches[0]
#     return t.label

# # 搜索二叉树的最大值
# def bst_max(t):
#     if t is None:
#         return None
#     while t.branches:
#         t = t.branches[1]
#     return t.label

def bst_min(t):
        """Return the min value of the tree t"""
        if t.is_leaf():
            return t.label
        sub_branch_min = min([bst_min(b) for b in t.branches])
        return min(t.label, sub_branch_min)

def bst_max(t):
    """Return the max value of the tree t"""
    if t.is_leaf():
        return t.label
    sub_branch_max = max([bst_max(b) for b in t.branches])
    return max(t.label, sub_branch_max)

# 普通树的最小值
def tree_min(t):
    if t is None:
        return float('inf')
    min_v = t.label 
    for b in t.branches:
        min_v = min(min_v, tree_min(b))
    return min_v

# 普通树的最大值
def tree_max(t):
    if t is None:
        return 0
    max_v = t.label
    for b in t.branches:
        max_v = max(max_v, tree_max(b))
    return max_v

def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    "*** YOUR CODE HERE ***"
    # 只有叶子节点
    if t.is_leaf():
        return True
    
    # > 2 分支
    if len(t.branches) > 2:
        return False

    # 1 分支
    if len(t.branches) == 1:
        return is_bst(t.branches[0]) and (bst_max(t.branches[0]) < t.label or bst_min(t.branches[0]) > t.label)

    # 2 分支    
    left_max = bst_max(t.branches[0])
    right_min = bst_min(t.branches[1])
    return left_max <= t.label < right_min and is_bst(t.branches[0]) and is_bst(t.branches[1])
    
    
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(Tree(2, [Tree(4, [Tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return [t.label]
    else:
        # 1, 先存储根节点
        prelist = [t.label]
        # 2, 递归遍历子树
        for b in t.branches:
            prelist += preorder(b)
        return prelist


def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(path_yielder(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = path_yielder(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = path_yielder(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """

    "*** YOUR CODE HERE ***"
    if t.label == value:
        yield [t.label]
    for b in t.branches:
        # 递归遍历子树
        # 对于每个子树 b，递归调用 path_yielder(b, value)，生成从子树 b 到目标节点的所有路径。
        for path in path_yielder(b, value):
            # 对于每一条从子树 b 生成的路径 path，将当前节点的标签 [t.label] 与路径 path 拼接，形成一条完整的路径。
            # 由后向前添加生成发的
            yield [t.label] + path

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

