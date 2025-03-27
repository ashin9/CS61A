# 必答题

## Trees

### Q1: Prune Min ✅

编写一个函数 `prune_min`，对树 `t` 进行原地修剪。`t` 及其分支始终具有零个或两个子分支。对于具有两个分支的树，将分支数量从两个减少到一个，保留标签值较小的分支。不对没有子分支的树进行任何操作。

可以选择自顶向下或自底向上的方向进行修剪。最终结果应为一棵线性树。

```python
def prune_min(t):
    """从底向上原地修剪树。

    >>> t1 = Tree(6)
    >>> prune_min(t1)
    >>> t1
    Tree(6)
    >>> t2 = Tree(6, [Tree(3), Tree(4)])
    >>> prune_min(t2)
    >>> t2
    Tree(6, [Tree(3)])
    >>> t3 = Tree(6, [Tree(3, [Tree(1), Tree(2)]), Tree(5, [Tree(3), Tree(4)])])
    >>> prune_min(t3)
    >>> t3
    Tree(6, [Tree(3, [Tree(1)])])
    """
    "*** YOUR CODE HERE ***"
```



## Scheme

### Q2: Split ❎ 如何记录前 n 个

实现 `split-at`，该函数接受一个列表 `lst` 和一个**正整数 `n`** 作为输入，并返回一个对 `new`，使得 `(car new)` 是 `lst` 的前 `n` 个元素，而 `(cdr new)` 是 `lst` 剩余的部分。如果 `n` 大于 `lst` 的长度，则 `(car new)` 应为 `lst`，而 `(cdr new)` 应为 `nil`。

```scheme
(define (split-at lst n)
  'YOUR-CODE-HERE
)
```



### Q3: Compose All ❎ 如何递归

实现 `compose-all`，该函数接受一个仅包含一元函数的列表，并返回一个一元函数，该函数依次对其参数应用列表中的每个函数。例如，如果 `func` 是对 `(f g h)` 这个函数列表调用 `compose-all` 的结果，那么 `(func x)` 应等价于 `(h (g (f x)))` 的计算结果。

```scheme
(define (compose-all funcs)
  'YOUR-CODE-HERE
)
```



## Tree Recursion

### Q4: Num Splits ❎ 

给定一个数字列表 `s` 和一个目标差值 `d`，计算有**多少种不同的方法**可以将 `s` 拆分为两个子集，使得第一个子集的和与第二个子集的和之差在 `d` 以内。两个子集中的元素个数可以不同。

可以假设 `s` 中的元素是唯一的，并且 `d` 始终为非负数。

请注意，子集内的元素顺序无关紧要，子集之间的顺序也不重要。例如，对于列表 `[1, 2, 3]`，`[1, 2], [3]` 和 `[3], [1, 2]` 只应计算一次，而不是两次。

**提示**：
 如果返回的数字过大，可能存在重复计算的情况。如果返回的结果与正确答案相差一个常数因子，最简单的修正方式可能是直接除去或减去该因子。

```python
def num_splits(s, d):
    """返回将 s 拆分为两个子列表，使它们的和相差不超过 d 的方法数。

    >>> num_splits([1, 5, 4], 0)  # 可拆分为 [1, 4] 和 [5]
    1
    >>> num_splits([6, 1, 3], 1)  # 无法找到合适的拆分
    0
    >>> num_splits([-2, 1, 3], 2) # 可拆分为 [-2, 3], [1] 和 [-2, 1, 3], []
    2
    >>> num_splits([1, 4, 6, 8, 2, 9, 5], 3)
    12
    """
    "*** YOUR CODE HERE ***"
```



# 选做题

## Objects

### Q5: Checking account ✅

我们希望能够**兑现支票**，因此需要在 `CheckingAccount` 类中添加一个 `deposit_check` 方法。该方法会接收一个 `Check` 对象作为参数，并检查 `Check` 对象的 `payable_to` 属性是否与 `CheckingAccount` 的 `holder` 匹配。如果匹配，则将该 `Check` 标记为已存入，并将指定金额添加到 `CheckingAccount` 的余额中。

请编写合适的 `Check` 类，并在 `CheckingAccount` 类中添加 `deposit_check` 方法。请确保不要复制粘贴代码，而是尽可能使用继承。

请参考以下 doctests 了解代码应如何工作：

```python
class CheckingAccount(Account):
    """一个收取手续费的银行账户。

    >>> check = Check("Steven", 42)  # 一张支付给 Steven 的 42 美元支票
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # 试图盗取 Steven 的钱
    The police have been notified.
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # 不能重复兑现支票
    The police have been notified.
    """
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    "*** YOUR CODE HERE ***"

class Check(object):
    "*** YOUR CODE HERE ***"
```



## Tree Recursion

### Q6: Align Skeleton ❓⭐️

实现 `align_skeleton` 函数，该函数通过**最小化编辑距离**来对齐给定的 `skeleton` 和 `code`。`skeleton` 和 `code` 都被假设为有效的单行代码字符串。

在 `align_skeleton` 中，使用递归辅助函数 `helper_align`，它接收 `skeleton_idx` 和 `code_idx` 作为参数，分别表示当前正在比较的 `skeleton` 和 `code` 中的字符索引。`helper_align` 返回两个值：

- `match`：表示所有编辑操作的字符串序列。
- `cost`：执行的编辑操作的数量。

### 基本情况：

1. 如果 `skeleton_idx` 和 `code_idx` 都到达了字符串的末尾，则不需要任何操作。
2. 如果 `skeleton` 还未遍历完，而 `code` 已遍历完，则需要删除 `skeleton` 剩余的所有字符。
3. 如果 `code` 还未遍历完，而 `skeleton` 已遍历完，则需要添加 `code` 剩余的所有字符。

### 递归步骤：

- 如果当前字符相同，则跳过，继续比较下一个字符。
- 如果当前字符不同：
  - **插入** `code` 的字符到 `skeleton`，并递归处理 `code` 的下一个字符。
  - **删除** `skeleton` 的当前字符，并递归处理 `skeleton` 的下一个字符。

最终，`helper_align` 选择最小编辑代价的方案，返回对应的 `match` 和 `cost`。



### 问题理解

这道题目要求我们实现 `align_skeleton` 函数，它的目标是**计算从 `skeleton` 变成 `code` 需要的最少编辑操作**，并返回一个描述这些操作的字符串。

**编辑操作包括：**

1. **插入（Insert）**: 在 `skeleton` 中增加字符，使其与 `code` 匹配，表示为 `+[x]`。
2. **删除（Delete）**: 从 `skeleton` 中删除字符，使其与 `code` 匹配，表示为 `-[x]`。
3. **匹配（Match）**: 如果 `skeleton` 和 `code` 的当前字符相同，则直接保留。

### 我们先来看几个例子：

```python
>>> align_skeleton(skeleton = "x=5", code = "x=6")
'x=+[6]-[5]'
```

解释：

- `skeleton` 是 `"x=5"`，而 `code` 是 `"x=6"`。
- 为了让 `skeleton` 变成 `code`：
  - 先删除 `5`，即 `-[5]`
  - 再插入 `6`，即 `+[6]`
  - `"x="` 是相同的部分，直接保留。

------

```python
>>> align_skeleton(skeleton = "while x<y", code = "for x<y")
'+[f]+[o]+[r]-[w]-[h]-[i]-[l]-[e]x<y'
```

解释：

- `skeleton = "while x<y"`，`code = "for x<y"`
- 需要**删除** `"while"`（`-[w]`, `-[h]`, `-[i]`, `-[l]`, `-[e]`）
- 需要**插入** `"for"`（`+[f]`, `+[o]`, `+[r]`）
- `"x<y"` 这部分匹配，保留不变。

### 任务拆解：

1. **去掉空格**（因为空格不影响代码逻辑）
2. **使用递归算法**：
   - 从 `skeleton` 和 `code` 的开头开始比较字符
   - 如果相等，继续比较下一个字符
   - 如果不相等，我们有两个选择：
     - 插入 `code` 的字符
     - 删除 `skeleton` 的字符
   - 选择**最少编辑次数**的方案

### **第一步：实现基本框架**

先创建函数 `align_skeleton`，并去掉空格：

```python
def align_skeleton(skeleton, code):
    skeleton, code = skeleton.replace(" ", ""), code.replace(" ", "")

    def helper_align(skeleton_idx, code_idx):
        # 这里是递归逻辑，我们稍后补充
        pass  

    result, cost = helper_align(0, 0)  # 从索引 0 开始
    return result
```

### **第二步：实现基本情况（Base Cases）**

**三种情况：**

1. `skeleton` 和 `code` 都匹配完成（递归终止）
2. `skeleton` 还有字符，`code` 用完了（必须删除 `skeleton` 剩下的字符）
3. `code` 还有字符，`skeleton` 用完了（必须插入 `code` 剩下的字符）

```python
def helper_align(skeleton_idx, code_idx):
    # Case 1: 两个字符串都匹配完成
    if skeleton_idx == len(skeleton) and code_idx == len(code):
        return "", 0

    # Case 2: skeleton 还有剩余字符，但 code 没有了
    if skeleton_idx < len(skeleton) and code_idx == len(code):
        edits = "".join(["-[" + c + "]" for c in skeleton[skeleton_idx:]])
        return edits, len(skeleton) - skeleton_idx

    # Case 3: code 还有剩余字符，但 skeleton 没有了
    if skeleton_idx == len(skeleton) and code_idx < len(code):
        edits = "".join(["+[" + c + "]" for c in code[code_idx:]])
        return edits, len(code) - code_idx
```

### **第三步：递归处理匹配、插入、删除**

#### 1. **匹配**（两个字符相同，继续递归）

```python
if skeleton[skeleton_idx] == code[code_idx]:
    next_match, next_cost = helper_align(skeleton_idx + 1, code_idx + 1)
    possibilities.append((skeleton[skeleton_idx] + next_match, next_cost))
```

#### 2. **插入**（`code` 多了一个字符，需要在 `skeleton` 里加上它）

```python
insert_match, insert_cost = helper_align(skeleton_idx, code_idx + 1)
possibilities.append(("+[" + code[code_idx] + "]" + insert_match, insert_cost + 1))
```

#### 3. **删除**（`skeleton` 多了一个字符，需要删掉它）

```python
delete_match, delete_cost = helper_align(skeleton_idx + 1, code_idx)
possibilities.append(("-[" + skeleton[skeleton_idx] + "]" + delete_match, delete_cost + 1))
```



## Linked Lists

### Q7: Fold Left ✅

**实现左折叠函数（left fold）**，它的作用是**按照从左到右的顺序**，用 `fn` 依次作用于链表的元素，并累积计算结果。



### Q8: Filter With Fold ✅ ❎ ⭐️

`filterl` 需要遍历 `lst` 并**筛选出所有满足 `pred`（谓词函数）**的元素，返回一个新的 `Link` 链表。

使用 fordr 才能保证顺序



### Q9: Reverse With Fold ✅ ⭐️

请注意，`mapl` 和 `filterl` 不再是递归函数！我们使用 `foldl` 和 `foldr` 来实现实际的递归：只需要提供递归步骤和基准情况给 `fold` 即可。

使用 `foldl` 来编写 `reverse`，它接受一个递归列表并将其反转。提示：它只需要一行代码！

**额外挑战（提高经验值）：** 编写一个不使用 `Link` 构造函数的 `reverse` 版本。你不必使用 `foldl` 或 `foldr`。



### Q10: Fold With Fold ✅ ⭐️

注意，`mapl` 和 `filterl` 不再是递归函数！使用 `foldl` 和 `foldr` 来实现实际的递归：只需要提供递归步骤和基准情况给 `fold` 即可。

使用 `foldl` 来编写 `reverse`，它接受一个递归列表并将其反转。提示：它只需要一行代码！

**额外挑战（提高经验值）：** 编写一个不使用 `Link` 构造函数的 `reverse` 版本。你不必使用 `foldl` 或 `foldr`。



### Q10: Fold With Fold ❎

使用 fodlr 编写 foldl