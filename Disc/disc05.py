
def tree(label, branches=[]):
    return [label] + branches

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_leaf(t):
    return not branches(t)

# 求树的高度，最长的 root 到 leaf 的路径长度
def height(t):
    """Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t) 
    2
    """
    if is_leaf(t):
        return 0
    else:
        # 生成每条子树的高度, 求最值
        return max([1 + height(b) for b in branches(t)])

# 编写一个函数，该函数接受一棵树作为输入，并返回树中**从根到任意叶子节点的路径**上的**最大值总和**。请记住，路径是从树的根到任意叶子节点的序列。
def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])

    >>> max_path_sum(t) 
    11
    """

    if is_leaf(t):
        return label(t)
    else:
        return max([label(t) + max_path_sum(b) for b in branches(t)])


def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    if branches(t):
        for b in branches(t):
            print_tree(b, indent + 1)

# 编写一个函数，该函数接受一棵树并将树中每个节点的值平方。它应返回一棵新的树。你可以假设树中的每个值都是数字。
def square_tree(t):
    """Return a tree with the square of every element in t

    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                         [tree(3),
    ...                         tree(4)]),
    ...                 tree(5,
    ...                         [tree(6,
    ...                                 [tree(7)]),
    ...                         tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
     4
      9
      16
     25
      36
       49
      64
    """
    # 自己思路不对, 错误地使用了 list.append() 来构造树，而 tree() 这个构造函数期望的是 一个标签和一个列表形式的子树，而不是直接向列表中添加子树。
    # square_tree = []  # square_tree = [] 只是一个普通的列表，不是树的结构
    # square_tree.append(tree(label(t) ** 2))
    # if branches(t):
          # 使得 square_tree 变成了嵌套列表，而不是一棵符合 tree() 结构的树。
    #     square_tree.append([square_tree(b) for b in branches(t)])
    # return square_tree

    # sol
    sq_b = [square_tree(b) for b in branches(t)]
    return tree(label(t) ** 2, sq_b)

# 编写一个函数，该函数接收一棵 **树** 和一个值 `x`，返回从 **根节点** 到 **值为 x 的节点** 之间的所有节点（按照路径顺序）的列表。
# 如果 `x` **不在树中**，则返回 `None`。假设树中的所有值是**唯一的**。
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """

    if label(tree) == x:
        return [x]
    
    for b in branches(tree):
        # 无法判断是否找到
        # return [label(tree)] + find_path(b, x)

        path = find_path(b, x)
        # 如果找到了路径
        if path:
            return [label(tree)] + path
    
    # 所有子树都找不到 x, 返回 None
    return None 


# 编写一个函数，该函数接受一个**仅由 '0' 和 '1' 组成的树** `t`，以及一个**二进制数列表** `nums`，返回一个**新树**，其中仅包含 `nums` 中**存在于 `t` 的二进制数**。
def prune_binary(t, nums):
    # 递归边界, 单节点
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    # 递归体, 递归遍历子树
    else:
        # 所有二进制数去掉第一个 bit
        next_vaild_nums = [n[1:] for n in nums if n[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_vaild_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [prune_binary]
        if not new_branches:
            return None
        return tree(label(t), new_branches)


import doctest 
doctest.testmod()