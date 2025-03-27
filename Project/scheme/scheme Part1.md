## Introduction

这个 Scheme 项目需要你编写一个 Scheme 语言的解释器，这可不是一个小工程！请尽早动手完成项目，因为整个项目部分繁多，很多同学在做题过程中会遇到卡壳的情况，而尽早开始则能给自己留出充裕的时间解决这些问题。记得可以在实验课（lab）和答疑时间（office hours）寻求帮助。

我们为这个项目编写了 CS 61A 子集 Scheme 的语言规范以及内建过程的参考文档。虽然没有必要通篇阅读这些文档，但在项目说明中，我们会为你指出某些特别有帮助的章节，供你参考。

在这个项目中，你将开发一个用于解释 Scheme 语言子集的解释器。在实现过程中，不妨思考编程语言设计中遇到的各种问题。**许多语言的“奇怪设计”实际上都是解释器或编译器实现决策的产物。**我们这次实现的 Scheme 语言子集描述在《Composing Programs》的函数式编程部分。由于我们只实现了 Scheme 的一个子集，所以你写的解释器行为可能不会和其他现有的 Scheme 解释器完全一致。

此外，你还需要用 Scheme 实现一些小程序。Scheme 是一种简单但功能强大的函数式编程语言。你应该会发现，之前在 Python 中学到的知识能够很好地**迁移**到 Scheme 以及其他编程语言中。

本项目还提供了一个挑战版（challenge version）。该版本的项目说明更为简略，起始代码也更加精简。它适合有扎实编程经验，并且希望挑战高难度的同学。需要注意的是，挑战版的评分与普通版相同，你可以选择做挑战版来代替普通版，以获得项目的全部分数。

之后我们还将发布一个开放式的图形竞赛。这个竞赛挑战你用极少的 Scheme 代码实现递归图形。比如，图中展示了使用美元硬币组成 50 美分的所有可能组合。每一朵花出现在长度为 50 的树枝末端，小角度的分支表示增加了一枚硬币，大角度的分支表示使用了新的货币单位。在竞赛中，你也将有机会发挥想象力，**成为一名递归艺术家！**

## Download starter files

你可以将整个项目代码打包下载为一个 ZIP 压缩文件。本项目包含多个文件，但你只需要修改以下四个文件：`scheme.py`、`scheme_reader.py`、`questions.scm` 和 `tests.scm`。以下是压缩包内包含的所有文件：

- **scheme.py**：实现 REPL（交互式解释器）以及 Scheme 表达式的求值器。
- **scheme_reader.py**：实现 Scheme 输入的读取器。其中包含 `Pair` 类以及 `nil` 的定义。
- **scheme_tokens.py**：实现 Scheme 输入的词法分析器（tokenizer）。
- **scheme_builtins.py**：使用 Python 实现 Scheme 语言的内置过程。
- **buffer.py**：实现 `Buffer` 类，该类在 `scheme_reader.py` 中被使用。
- **ucb.py**：61A 课程项目中的一些实用函数。
- **questions.scm**：包含 **Phase III** 的代码框架。
- **tests.scm**：包含一系列用 Scheme 编写的测试用例。
- **ok**：自动评分脚本。
- **tests**：存放 `ok` 评分脚本使用的测试文件。
- **mytests.rst**：一个用于添加你自己测试用例的文件。

## Logistics

本项目为期 **15 天**，你可以与 **一名伙伴** 共同完成。请注意，你 **不能** 与非合作伙伴的同学分享代码，也 **不能** 复制其他人的解答。最终，你和你的合作伙伴只需提交 **一份** 共同完成的项目。

我们 **强烈建议** 你们 **一起** 完成所有部分，而不是将任务拆分开来。可以轮流编写代码，而非编写代码的一方应该通过查看代码、提供改进建议以及帮助发现错误来积极参与。



### 评分标准

本项目总分 **30 分**，其中 **28 分** 用于评估代码的正确性，包括：

- **1 分**：通过 `tests.scm` 的所有测试
- **1 分**：在第一个检查点前提交 **问题 1-6**
- **1 分**：在第二个检查点前提交 **Part I 和 Part II**



### 提交要求

你需要提交以下 **四个文件**：

- `scheme_reader.py`
- `scheme.py`
- `questions.scm`
- `tests.scm`

你**不需要**修改或提交任何其他文件。要提交项目，请运行以下命令：

```
python3 ok --submit
```

你可以在 **Ok dashboard** 上查看你的提交记录。



### 代码编写规则

对于需要你完成的函数，我们可能会提供一些初始代码。如果你不想使用它，可以**删除并从头编写**。同时，你也可以**添加新的函数**，以便更好地实现功能。

但是，请 **不要修改** 其他已有函数，否则可能会导致你的代码在自动评分器（autograder）测试中失败。此外，请 **不要更改** 任何函数的**签名**（包括函数名、参数顺序或参数数量）。



### 代码测试与调试

在整个项目过程中，你应该经常测试代码的正确性。良好的实践是 **定期测试**，这样可以更容易地定位问题。然而，不要**过于频繁地测试**，以确保你有足够的时间思考解决方案。

我们提供了一个 **自动评分器（autograder）`ok`** 来帮助你测试代码并跟踪进度。第一次运行 `ok` 时，你需要在浏览器中登录 **Ok 账户**，请务必完成此步骤。每次运行 `ok` 时，它都会自动备份你的代码和进度到我们的服务器。

`ok` 的主要作用是测试你的实现。我们建议你在完成**每个问题**后进行一次提交。**最终只会对你最后一次提交的版本进行评分**。同时，如果你在提交时遇到问题，我们也可以通过你的备份记录来帮助你恢复代码。

如果你忘记提交，**系统会自动将你的最后一次备份转换为提交**，确保你的工作不会丢失。

如果你不希望我们记录你的代码备份或进度信息，你可以使用以下命令 **本地运行 `ok`**，这样不会向服务器发送任何信息：

```
python3 ok --local
```

如果你想 **交互式** 测试某个具体问题，可以使用以下命令：

```
python3 ok -q [问题编号] -i
```

例如，测试 **问题 1**：

```
python3 ok -q 01 -i
```

这样会运行该问题的测试，直到第一个失败的测试，并提供一个交互式环境，让你手动测试编写的函数。

如果你需要 **打印调试信息**，可以使用 `print` 语句，如下所示：

```
print("DEBUG:", x)
```

这样会在终端中输出调试信息，但不会影响 `ok` 评分器的运行，不会因为额外的输出导致测试失败。



## Interpreter details

### Scheme features

#### 读-求值-输出（Read-Eval-Print）

解释器的功能是读取 Scheme 表达式，进行求值，然后显示结果。

例如：

```
scm> 2
2
scm> (+ 2 3)
5
scm> ((lambda (x) (* x x)) 5)
25
```

你目前的 `scheme.py` 文件中提供的初始代码，已经可以成功求值第一个表达式（因为它只是一个单独的数字）。但第二个（调用内置过程）和第三个（计算 5 的平方）还无法正常工作，这需要你在项目中继续完成实现。

------

#### 加载（Load）

你可以通过传入文件名的符号来加载文件。例如，要加载 `tests.scm` 文件，可以输入以下调用表达式：

```
scm> (load 'tests)
```

------

#### 符号（Symbols）

不同的 Scheme 方言对于 **标识符**（也就是符号和变量名）允许的形式有不同的规定。

我们这个项目中采用的规则是：

- 标识符可以由 字母（a-z 和 A-Z）、数字，以及以下特殊字符组成：

  ```
  !$%&*/:<=>?@^_~-+.
  ```

- 但是，**不能** 形成有效的 **整数** 或 **浮点数**，也不能是已存在的 **特殊形式简写**。

我们的 Scheme 是 **大小写不敏感** 的。也就是说，只要字母相同，大小写不同也算是同一个标识符。解释器内部会统一用小写表示和打印：

```
scm> 'Hello
hello
```

------

#### 海龟图形（Turtle Graphics）

除了标准的 Scheme 过程，我们还支持调用 Python 的 `turtle` 包来画图。这对于后续的图形竞赛（contest）会很有用。

你可以在线查看 Python `turtle` 模块的官方文档来了解具体使用方法。

**注意**：

- Python 的 `turtle` 模块在你的个人电脑上可能默认没有安装。
- 不过，在学校的教学用计算机上，`turtle` 模块是已经安装好的。
- 如果你希望在自己的电脑上做 `turtle` 绘图（比如为参加图形竞赛做准备），需要自行安装并配置好 `turtle` 模块，或者直接使用学校的计算机来完成。

### Implementation overview

#### **Read（读取）**

这一阶段的作用是将用户输入的字符串（Scheme 代码）**解析**成解释器内部使用的 Python 表示形式（例如 `Pair` 对象）。

- **词法分析（Lexical analysis）**
   已经为你实现好了！
   相关代码在 `scheme_tokens.py` 文件中的 `tokenize_lines` 函数。
   它会返回一个 `Buffer`（定义在 `buffer.py` 中），用来保存分析得到的 **token**。
   ➤ 你**不需要**阅读或理解这部分代码。
- **语法分析（Syntactic analysis）**
   发生在 `scheme_reader.py` 中的 `scheme_read` 和 `read_tail` 函数里。
   这两个函数是互相递归的，作用是将 Scheme 的 token 序列解析为我们解释器内部的 Python 对象。
   ➤ 你需要**完成**这两个函数。

#### **Eval（求值）**

这一阶段的作用是对内部的 Python 表示的 Scheme 表达式进行求值，得到结果值。
 相关代码主要在 `scheme.py` 文件中。

- **求值（Eval）**
   发生在 `scheme_eval` 函数中。
  - 如果表达式是一个 **调用表达式**，会按照调用表达式的求值规则进行求值（这部分需要你来实现）。
  - 如果表达式是一个 **特殊形式（special form）**，则会调用对应的 `do_?_form` 函数（你需要完成若干 `do_?_form` 函数）。
- **应用（Apply）**
   发生在 `scheme_apply` 函数中。
  - 如果要调用的函数是内置过程（built-in procedure），`scheme_apply` 会调用 `BuiltInProcedure` 实例的 `apply` 方法。
  - 如果是用户自定义过程（user-defined procedure），`scheme_apply` 会创建一个新的调用帧（call frame），并对函数体（body）调用 `eval_all`，从而形成互相递归的 eval-apply 循环。

#### **Print（输出）**

这一阶段的作用是输出求值得到的值。
 具体做法是打印结果值的 `__str__` 表示。

#### **Loop（循环）**

循环的逻辑由 `scheme.py` 文件中的 `read_eval_print_loop` 函数负责。
 ➤ 你**不需要**理解完整的实现细节。

#### **异常处理（Exceptions）**

在开发 Scheme 解释器的过程中，你可能会遇到 Python 抛出的各种未捕获异常，导致解释器停止运行。

- 有些异常是由于你代码中的**bug**引起的，这部分需要通过**调试**解决。
- 但还有些异常来源于用户写的 Scheme 程序出错，这部分需要你的代码去**处理**。
   ➤ 通常需要通过抛出 `SchemeError` 异常来处理用户程序中的错误。

所有的 `SchemeError` 异常都会被 `read_eval_print_loop` 函数捕获，并显示为错误信息。
 理想状态下，你的解释器在处理任何输入时，都不应该有未处理的 Python 异常。



### Running the interpreter



## Part 0: Testing Your Interpreter

## Part I: The Reader

在这个部分中，所有的更改都应该写在 `scheme_reader.py` 文件中。

------

在 **第一部分** 和 **第二部分** 中，你将分阶段开发一个 Scheme 解释器，主要包括以下内容：

1. 读取 Scheme 表达式
2. **符号求值**
3. 调用内建过程
4. 定义语句
5. Lambda 表达式和过程定义
6. 调用用户定义的过程
7. 特殊形式（special forms）的求值

------

### 第一部分的任务是：

**读取和解析用户输入（Reading Scheme expressions）**

我们的阅读器（reader）会将 Scheme 代码解析为 Python 内部表示。具体映射关系如下：

| 输入示例       | Scheme 表达式类型        | 我们的内部表示                               |
| -------------- | ------------------------ | -------------------------------------------- |
| `scm> 1`       | 数字（Numbers）          | Python 内建的 `int` 和 `float` 类型          |
| `scm> x`       | 符号（Symbols）          | Python 内建的 `str` 类型                     |
| `scm> #t`      | 布尔值（Booleans #t/#f） | Python 内建的 `True` / `False`               |
| `scm> (+ 2 3)` | 组合（Combinations）     | `Pair` 类的实例（定义在 `scheme_reader.py`） |
| `scm> nil`     | nil                      | `nil` 对象（定义在 `scheme_reader.py`）      |

在本项目中，**组合（combinations）** 既可以表示函数调用表达式，也可以表示特殊形式（special forms）。

------

如果你还没有阅读过项目文档中的 **Implementation overview（实现概述）**，请务必先去看一下！这样你才能更好地理解阅读器（reader）是如何分工实现的。

------

### 关于 Buffer

我们在实现中使用 `Buffer` 实例来保存已准备好解析的 token（词法单元）。

举个例子，一个包含 `(+ (2 3))` 的 `Buffer` 对象会依次存放这些 token：
 `'('`、`'+'`、`'('`、`2`、`3`、`')'`、`')'`。

可以参考 `buffer.py` 文件里的 doctests（文档测试示例），了解更多用法。
 你不需要深入理解 `buffer.py` 的具体实现，只需要知道它的接口如何使用。

------

### 你要实现的解析函数

你需要完成两个递归调用的函数：

- `scheme_read(src)`
- `read_tail(src)`

这两个函数都接受一个参数 `src`，它是 `Buffer` 类的实例。

------

### 与 `Buffer` 交互的方法

- `src.pop_first()`
   修改 `src`，删除并返回第一个 token。
   例如，`src` 当前为 `[4, 3, ')']`，调用 `src.pop_first()` 会返回 `4`，`src` 剩下 `[3, ')']`。
- `src.current()`
   返回 `src` 当前的第一个 token，但**不**删除。
   例如，`src` 当前为 `[4, 3, ')']`，调用 `src.current()` 会返回 `4`，`src` 不变。

⚠️ 注意：`Buffer` 不支持通过下标访问（即 `buffer[1]` 是非法的）。

如果需要一些指导帮助你完成 **第1到第6题**，可以观看项目文档中的提示视频（hint video）。

### Problem 1 (2 pt) ✅

#### 实现 `scheme_read` 和 `read_tail`

首先，你需要实现 `scheme_read` 和 `read_tail` 函数，使它们能够解析组合表达式（combinations）和原子表达式（atomic expressions）。

### ✅ 目标行为如下：

#### `scheme_read`

- 需要从 `src`（类型为 `Buffer`）中移除足够多的 token（词法单元），从而组成一个完整的表达式，并返回这个表达式的**内部表示**（参见之前那张表）。

#### `read_tail`

- 需要读取一个**表（list）或对（pair）**的剩余部分，前提是它假设 `scheme_read` 已经移除了该表/对的开括号 `(`。
- `read_tail` 会不断读取表达式（也就是说不断从 `src` 中移除 token），直到遇到配对的右括号 `)` 为止。
- 这些表达式将被封装成 `Pair` 的链表形式，并作为返回值返回。

------

### 🔧 简单总结

- `scheme_read` 返回 `src` 中的**下一个完整的单一表达式**。
- `read_tail` 返回 `src` 中一个表或对的**剩余元素**。
- 两个函数都会**改变（mutate）** `src`，因为它们会移除已经处理的 token。

------

### ✅ 两个函数的具体实现逻辑如下：

------

#### `scheme_read` 的处理逻辑

根据 `src` 的当前 token（`src.current()`）来判断：

1. **如果当前 token 是字符串 "nil"**
    → 返回 `nil` 对象。
2. **如果当前 token 是左括号 `(`**
    → 说明表达式是一个表或对。
    → 调用 `read_tail` 处理 `src` 的剩余部分，并返回结果。
3. **如果当前 token 是单引号 `'`**
    → 这是 `quote` 表达式的开头。
    → 不用着急处理！这是第 6 题的内容。
4. **如果当前 token 不是分隔符（delimiter）**
    → 说明是一个基本表达式（数字、布尔值等）。
    → 返回这个值（项目模板已提供处理）。
5. **如果都不符合，抛出错误**
    → 项目模板已经帮你写好了。

------

#### `read_tail` 的处理逻辑

根据 `src` 的当前 token（`src.current()`）来判断：

1. **如果已经没有更多 token（`src.current()` 是 None）**
    → 说明缺少右括号 `)`。
    → 抛出错误（模板已提供）。
2. **如果当前 token 是右括号 `)`**
    → 说明表或对的结尾到了。
    → 移除这个 token，然后返回 `nil`。
3. **如果都不是**
    → 处理剩余组合（combination）：
   - 第一步：用 `scheme_read` 读取 `src` 中下一个完整的表达式。
   - 第二步：递归调用 `read_tail`，读取表/对的其余部分，直到遇到 `)`。
   - 返回一个 `Pair` 实例，第一个元素是 `scheme_read` 得到的表达式，第二个元素是 `read_tail` 得到的剩余部分。

------

### 🔨 开发提示

- 想清楚**递归结构**！
   `read_tail` 每处理一个元素，就递归去处理剩余的表元素。
   每次都会封装在 `Pair` 结构中，直到遇到 `nil` 终止。
- 可以去看看课程讲义/视频讲解，特别是关于递归解析器的实现。

------

### 示例：输入 → 内部表示

```scss
(+ 2 3)
```

1. `scheme_read` 读到 `(`，于是进入 `read_tail`
2. `read_tail` 读到 `+`，用 `scheme_read` 解析为符号 `+`
3. `read_tail` 递归继续，读到 `2`，解析为数字 `2`
4. `read_tail` 继续，读到 `3`，解析为数字 `3`
5. `read_tail` 继续，读到 `)`，结束，返回 `nil`
6. 整体递归返回：

```less
Pair('+', Pair(2, Pair(3, nil)))
```



```shell
➜  scheme py3 ok -q 01 -u                         
=====================================================================
Assignment: Project 4: Scheme Interpreter
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 2
(cases remaining: 7)

>>> from scheme_reader import *
>>> tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
>>> src = Buffer(tokens)
>>> src.current()
? (
-- Not quite. Try again! --

? "("
-- OK! --

>>> src.pop_first()
? "("
-- OK! --

>>> src.current()
? "+"
-- OK! --

>>> src.pop_first()
? "+"
-- OK! --

>>> src.pop_first()
? 1
-- OK! --

❎
>>> scheme_read(src)  # Removes the next complete expression in src and returns it as a Pair
? nil
-- Not quite. Try again! --

? Pair(2, Piar(3, nil))
-- Not quite. Try again! --

? unexpected end of file
-- Not quite. Try again! --

? Pair(23, Piar(4, nil))
-- Not quite. Try again! --

? unexpected token: )
-- Not quite. Try again! --

? Pair(23, Pair(4, nil))
-- OK! --

>>> src.current()
? ")"
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 3
(cases remaining: 6)

>>> from scheme_reader import *
>>> scheme_read(Buffer(tokenize_lines(['(18 6)']))) # Type SyntaxError if you think this errors
? Pair(18, Pair(6, nil))
-- OK! --

>>> read_line('(18 6)')  # Shorter version of above!
? Pair(18, Pair(6, nil))
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 4
(cases remaining: 5)

>>> from scheme_reader import *
>>> read_tail(Buffer(tokenize_lines([')'])))
? SntaxError
-- Not quite. Try again! --

? SyntaxError
-- Not quite. Try again! --

? SyntaxError
-- Not quite. Try again! --

? nil
-- OK! --

>>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
? nil
-- Not quite. Try again! --

? Pair(1, Pair(2, Pair(3, nil)))
-- OK! --

❎
# 看到 (，递归进入 scheme_read 解析子表达式
# ➡️ scheme_read 调用 read_tail，处理 3 4)，得到 Pair(3, Pair(4, nil))，scheme_read 返回 Pair(3, Pair(4, nil))
# 3️⃣ 再递归回上一层，回到 Buffer，剩下 [')']，read_tail 看到 )，返回 nil
>>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
? Pair(2, Pari(3, Pair(4, nil), nil)
-- Not quite. Try again! --

? Pair(2, Pair(Pair(3, Pair(4, nil)))
-- Not quite. Try again! --

? Pair(2, Pair(Pair(3, Pair(4, nil), nil))
-- Not quite. Try again! --

? Pair(2, Pair(Pair(3, Pair(4, nil)), nil)
-- Not quite. Try again! --

? Pair(2, Pair(Pair(3, Pair(4, nil)), nil))
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 5
(cases remaining: 4)

❎？为什么 SynaxError? 
# read_tail 是专门用来处理剩余的 list 部分的
# 但它的前提条件是： 左括号 ( 已经被 scheme_read 弹出来了！
>>> from scheme_reader import *
>>> read_tail(Buffer(tokenize_lines(['(1 2 3)']))) # Type SyntaxError if you think this errors
? Pair(1, Pair(2, Pair(3, nil)))
-- Not quite. Try again! --

? Pair(1, Pair(2, Pair(3, nil)))
-- Not quite. Try again! --

? SyntaxError
-- OK! --

>>> read_line('((1 2 3)') # Type SyntaxError if you think this errors
? SyntaxError
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 6
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 7
(cases remaining: 2)

❎？为什么这样可以作为输入？难道不要先分词？
# 注意是 read_line() 不是 read_tail()
>>> from scheme_reader import *
>>> read_line("(+ (- 2 3) 1)")
Choose the number of the correct choice:
0) Pair('+', Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil))
1) Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
2) Pair('+', Pair('-', Pair(2, Pair(3, Pair(1, nil)))))
? 1
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 8
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem 1 unlocked.

Performing authentication
Please enter your school email (.edu): ^C% 
```



