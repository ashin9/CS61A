## 目标：编写程序测试打字速度并自动纠正错误拼写



# Phase 1: Typing

### Problem 1 (1 pt)

Implement choose，用于选择用户将键入的段落。它需要一个段落（字符串）列表、一个为可以选择的段落返回 True 的 select 函数，以及一个非负索引 k。choose 函数返回第 k 个 select 返回 True段落。如果不存在此类段落（因为 k 太大），则 choose 返回空字符串。



理解解锁：

应该翻译为：choose 函数返回第 k 个 select 返回 True段落

```shell
➜  cats py3 ok -q 01 -u                 
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 1 > Suite 1 > Case 1
(cases remaining: 101)

>>> from cats import choose
>>> ps = ['short', 'really long', 'tiny']
>>> s = lambda p: len(p) <= 5
>>> choose(ps, s, 0)
? short
-- Not quite. Try again! --

? 'short'
-- OK! --

>>> choose(ps, s, 1)
? 'really long'
-- Not quite. Try again! --

? ''
-- Not quite. Try again! --

? null
-- Not quite. Try again! --

? -
-- Not quite. Try again! --

? 0
-- Not quite. Try again! --

? false
-- Not quite. Try again! --

? 'tiny'
-- OK! --

>>> choose(ps, s, 2)
? ''
-- OK! --

---------------------------------------------------------------------
Problem 1 > Suite 2 > Case 1
(cases remaining: 100)

-- Already unlocked --
```



### Problem 2 (2 pt)

实现 about，它接受主题词列表。它返回一个函数，该函数接受一个段落并返回一个布尔值，指示该段落是否包含 topic 中的任何单词。可以将返回的函数作为 select 参数传递给 choose。

为了准确地进行这种比较，您需要忽略段落中的大小写（即，假设大写和小写字母不会改变单词）和标点符号。

假设主题列表中的所有单词都已小写且不包含标点符号。



解锁，注意用 True 和 False，首字母大写

```shell
➜  cats py3 ok -q 02 -u          
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 2 > Suite 1 > Case 1
(cases remaining: 101)

>>> from cats import about
>>> dogs = about(['dogs', 'hounds'])
>>> dogs('A paragraph about cats.')
? true
-- Not quite. Try again! --

? false
-- Not quite. Try again! --

? TRUE
-- Not quite. Try again! --

? FALSE
-- Not quite. Try again! --

? false
-- Not quite. Try again! --

? False
-- OK! --

>>> dogs('A paragraph about dogs.')
? True
-- OK! --

>>> dogs('Release the Hounds!')
? True
-- OK! --

>>> dogs('"DOGS" stands for Department Of Geophysical Science.')
? True
-- OK! --

>>> dogs('Do gs and ho unds don\'t count')
? False
-- OK! --

---------------------------------------------------------------------
Problem 2 > Suite 2 > Case 1
(cases remaining: 100)

-- Already unlocked --
```



### Problem 3 (1 pt)

实现 accuracy，它采用键入的段落和引用段落。它返回 typed 中与 reference 中的相应单词完全匹配的单词的百分比。大小写和标点符号也必须匹配。

在此上下文中，单词是用空格与其他单词分隔的任何字符序列，因此请将 “dog;” 视为一个单词。

如果 typed 单词在引用中没有对应的单词是因为 typed 单词比 reference 长，那么 typed 中的额外单词都是不正确的。

如果 typed 为空，则准确率为零。



解锁，从左向右一个一个对应匹配大小写敏感包含标点，\t等制表符不计入单词

```shell
➜  cats py3 ok -q 03 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import accuracy
>>> accuracy("12345", "12345") # Returns 100.0
? True
-- Not quite. Try again! --

? 100.0
-- OK! --

>>> accuracy("a b c", "a b c")
? 100.0
-- OK! --

>>> accuracy("a  b  c  d", "b  a  c  d")
? 0.0
-- Not quite. Try again! --

? 75.0
-- Not quite. Try again! --

? 100.0
-- Not quite. Try again! --

? 50.0
-- OK! --

>>> accuracy("a b", "c d e")
? 0.0
-- OK! --

>>> accuracy("Cat", "cat") # the function is case-sensitive
? 0.0
-- OK! --

>>> accuracy("a b c d", " a d ")
? 100.0
-- Not quite. Try again! --

? 25.0
-- OK! --

>>> accuracy("abc", " ")
? 0.0
-- OK! --

>>> accuracy(" a b \tc" , "a b c") # Tabs don't count as words
? 67.7
-- Not quite. Try again! --

? 66.7
-- Not quite. Try again! --

? 66.6
-- Not quite. Try again! --

? 100.0
-- OK! --

>>> accuracy("abc", "")
? 0.0
-- OK! --

>>> accuracy("", "abc")
? 0.0
-- OK! --

>>> accuracy("cats.", "cats") # punctuation counts
? 0.0
-- OK! --

---------------------------------------------------------------------
Problem 3 > Suite 1 > Case 2
(cases remaining: 101)

-- Already unlocked --
```



### Problem 4 (1 pt)

实施 wpm，它计算每分钟的单词数，这是键入速度的度量，给定键入的字符串和运行时间（以秒为单位）。尽管名称如此，但每分钟的单词数不是基于键入的单词数，而是基于字符数，因此键入测试不会因单词长度而产生偏差。每分钟单词数的公式是键入的字符数（包括空格）除以 5（典型单词长度）与运行时间（以分钟为单位）的比率。



例如，字符串 “I am glad！” 包含 3 个单词和 10 个字符（不包括引号）。每分钟单词数计算使用 2 作为键入的单词数（因为 10 / 5 = 2）。如果有人在 30 秒（半分钟）内输入此字符串，他们的速度将是每分钟 4 个单词。



```shell
➜  cats py3 ok -q 04 -u          
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import wpm
>>> wpm("12345", 3) # Note: wpm returns a float (with a decimal point)
? 20
-- Not quite. Try again! --

? 20.0
-- OK! --

>>> wpm("a b c", 20)
? 3
-- Not quite. Try again! --

? 3.0
-- OK! --

>>> wpm("", 10)
? 0.0
-- OK! --

---------------------------------------------------------------------
Problem 4 > Suite 1 > Case 2
(cases remaining: 102)

-- Already unlocked --
```



# Phase 2: Autocorrect

在基于 Web 的 GUI 中，有一个自动更正按钮，但现在它不执行任何作。让我们实现拼写错误的自动更正。每当用户按下空格键时，如果他们键入的最后一个单词与字典中的单词不匹配，但接近一个单词，则该相似的单词将被替换他们键入的单词。

### Problem 5 (2 pt)

如果user_word包含在 valid_words 列表中，则 autocorrect 将返回该单词。否则，自动更正会返回与基于diff_function提供的user_word差异最小的valid_words单词。但是，如果 user_word 与任何valid_words之间的最小差值大于 limit，则改为返回 user_word。

一个 diff 函数接受三个参数。前两个参数是要比较的两个字符串（user_word和valid_words中的一个单词），第三个参数是 limit。diff_function 的输出是一个数字，表示两个字符串之间的差值。

如果多个字符串根据diff_function具有相同的最小差异，则 AutoCorrect 应返回valid_words中首先出现的字符串。



```shell
➜  cats py3 ok -q 05 -u             
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 1
(cases remaining: 103)

>>> from cats import autocorrect, lines_from_file
>>> abs_diff = lambda w1, w2, limit: abs(len(w2) - len(w1))
>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 10)
? cult
-- Not quite. Try again! --

? "cult"
-- OK! --

>>> autocorrect("cul", ["culture", "cult", "cultivate"], abs_diff, 0)
? "cul"
-- OK! --

>>> autocorrect("wor", ["worry", "car", "part"], abs_diff, 10)
? "car"
-- OK! --

>>> first_diff = lambda w1, w2, limit: 1 if w1[0] != w2[0] else 0
>>> autocorrect("wrod", ["word", "rod"], first_diff, 1)
? word
-- Not quite. Try again! --

? "word"
-- OK! --

>>> autocorrect("inside", ["idea", "inside"], first_diff, 0.5)
? "inside"
-- OK! --

>>> autocorrect("inside", ["idea", "insider"], first_diff, 0.5)
? "insider"
-- Not quite. Try again! --

? "inside"
-- Not quite. Try again! --

? "idea"
-- OK! --
# 两个 diff 都符合，返回第一个

>>> autocorrect("outside", ["idea", "insider"], first_diff, 0.5)
? "outside"
-- OK! --

---------------------------------------------------------------------
Problem 5 > Suite 1 > Case 2
(cases remaining: 102)

-- Already unlocked --
```



### Problem 6 (2 pts)

实现 `shifty_shifts`，这是一个计算差异的函数，它接收两个字符串作为输入。该函数返回将起始单词转换为目标单词所需修改的最小字符数。如果两个字符串的长度不相等，则长度差也应计入总修改次数。

使用递归，不能使用迭代

如果需要更改的字符数大于 `limit`，则 `shifty_shifts` 应返回一个大于 `limit` 的数，并且应尽量减少计算量。



```shell
➜  cats py3 ok -q 06 -u          
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 1
(cases remaining: 104)

>>> from cats import shifty_shifts, autocorrect
>>> import tests.construct_check as test
>>> big_limit = 10
>>> shifty_shifts("car", "cad", big_limit)
? 1
-- OK! --

>>> shifty_shifts("this", "that", big_limit)
? 2
-- OK! --

>>> shifty_shifts("one", "two", big_limit)
? 3
-- OK! --

>>> shifty_shifts("from", "form", big_limit)
? 2
-- OK! --

>>> shifty_shifts("awe", "awesome", big_limit)
? 4
-- OK! --

>>> shifty_shifts("someawe", "awesome", big_limit)
? 7
-- Not quite. Try again! --

? 6
-- OK! --

>>> shifty_shifts("awful", "awesome", big_limit)
? 5
-- OK! --

>>> shifty_shifts("awful", "awesome", 3) > 3
? 4
-- Not quite. Try again! --

? 5
-- Not quite. Try again! --

? True
-- OK! --

>>> shifty_shifts("awful", "awesome", 4) > 4
? Trur
-- Not quite. Try again! --

? True
-- OK! --

>>> shifty_shifts("awful", "awesome", 5) > 5
? False
-- OK! --

---------------------------------------------------------------------
Problem 6 > Suite 1 > Case 2
(cases remaining: 103)

-- Already unlocked --
```



如果需要更改的字符数大于 `limit`，则 `shifty_shifts` 应返回一个大于 `limit` 的数，并且应尽量减少计算量。

如何理解？最多更改 limit+1 个字符



### Problem 7 (3 pt)

实现 `pawssible_patches`，这是一个计算差异的函数，它返回将起始单词转换为目标单词所需的最小编辑操作次数。

编辑操作共有三种：

1. 在 `start` 中添加一个字母。
2. 从 `start` 中删除一个字母。
3. 将 `start` 中的某个字母替换为另一个字母。

每个编辑操作都会使两个单词之间的差异增加 1。

我们在 `cats.py` 中提供了一个实现模板。该函数是一个递归函数，其中包含三个递归调用。其中一个递归调用与 `shifty_shifts` 中的递归调用类似。

你可以随意修改该模板，或者完全删除它。

如果所需的编辑次数大于 `limit`，则 `pawssible_patches` 应返回一个大于 `limit` 的数，并且应尽量减少计算量。





扩展：你可以选择设计自己的 `diff` 函数，命名为 `final_diff`。以下是一些可以提高校正准确性的思路：

- 考虑某些添加和删除操作的可能性比其他情况更高。例如，如果一个字母连续出现两次，那么更可能会被误删。
- 将相邻字母位置互换视为一次修改，而不是两次。
- 尝试结合常见的拼写错误进行优化。





# Phase 3: Multiplayer

打字与朋友一起玩更有趣！现在，你将实现多人游戏功能，这样当你在自己的计算机上运行 `gui.py` 时，它会连接到课程服务器 `cats.cs61a.org`，并寻找对手进行比赛。

要与朋友比赛，将会运行 5 个不同的程序：

1. **你的 GUI**——一个处理网页浏览器中所有文本着色和显示的程序。
2. **你的 `gui.py`**——一个 Web 服务器，它使用你在 `cats.py` 中编写的代码与 GUI 进行通信。
3. **你的对手的 `gui.py`**。
4. **你的对手的 GUI**。
5. **CS 61A 多人服务器**——用于匹配玩家并传递消息。

当你输入时，你的 GUI 会将输入内容发送到你的 `gui.py` 服务器，该服务器计算你的进度并返回一个进度更新。同时，它还会将进度更新发送到多人服务器，以便你的对手的 GUI 可以显示你的进度。

与此同时，你的 GUI 始终尝试保持最新状态，它会向 `gui.py` 请求进度更新，而 `gui.py` 又会向多人服务器请求该信息。

每位玩家都有一个 ID 号码，服务器会使用该 ID 来跟踪打字进度。

### Problem 8 (2 pt)

实现 `report_progress`，该函数在用户输入完一个单词时调用。它接收以下参数：

- **`typed`**：用户已经输入的单词列表。
- **`prompt`**：提示文本中的单词列表。
- **`user_id`**：用户的 ID。
- **`send`**：一个用于向多人服务器发送进度报告的函数。

需要注意的是，`typed` 中的单词数量不会超过 `prompt` 中的单词数量。

你的进度计算方式如下：在 `prompt` 中，从头开始，正确输入的单词数量（直到遇到第一个错误单词为止），除以 `prompt` 的总单词数。例如，以下情况的进度为 `0.25`：



调用 `report_progress(["Hello", "ths", "is"], ["Hello", "this", "is", "wrong"], ...)` 时，`report_progress` 函数应返回该进度值。

在返回之前，函数应向多人服务器发送一条消息，该消息是一个包含两个键的字典：

- **`id`**：用户的 `user_id`（由 GUI 传入 `report_progress`）。
- **`progress`**：计算得到的进度比例。

使用 `send` 函数发送此字典，以将进度信息传递给多人服务器。





```shell
➜  cats py3 ok -q 08 -u
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 1
(cases remaining: 101)

>>> from cats import report_progress
>>> print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
>>> typed = ['I', 'have', 'begun']
>>> prompt = ['I', 'have', 'begun', 'to', 'type']
>>> print_progress({'id': 1, 'progress': 0.6})
ID: 1 Progress: 0.6
>>> report_progress(typed, prompt, 1, print_progress) # print_progress is called on the report
ID: 1 Progress: 0.6
0.6
>>> report_progress(['I', 'begun'], prompt, 2, print_progress)
(line 1)? ID: 2 Progress: 0.2
(line 2)? 0.2
-- OK! --

>>> report_progress(['I', 'hve', 'begun', 'to', 'type'], prompt, 3, print_progress)
(line 1)? ID: 2 Progress: 0.2
-- Not quite. Try again! --

(line 1)? ID: 3 Progress: 0.2
(line 2)? 0.2
-- OK! --

---------------------------------------------------------------------
Problem 8 > Suite 1 > Case 2
(cases remaining: 100)

-- Already unlocked --
```



### Problem 9 (1 pt)

实现 `time_per_word`，该函数接收以下参数：

- **`times_per_player`**：一个列表，包含每位玩家的时间戳列表，表示每位玩家输入每个单词的完成时间。
- **`words`**：单词列表。

该函数返回一个包含给定信息的游戏数据。

游戏（`game`）是一个数据抽象，包含以下内容：

- **`words`**：单词列表。
- **`times`**：一个列表，存储每位玩家输入每个单词所花费的时间。`times[i][j]` 表示玩家 `i` 输入单词 `j` 所用的时间。



时间戳是累积的，并且始终递增，而 `times` 中的值表示相邻时间戳之间的差值。例如，假设：

```python
times_per_player = [[1, 3, 5], [2, 5, 6]]
```

则对应的 `times` 应为：

```python
[[2, 2], [3, 1]]  # 计算方式：(3-1), (5-3) 和 (5-2), (6-5)
```

需要注意的是，每个 `times_per_player` 的第一项表示玩家的起始时间，不应包含在 `times` 计算中。

在返回游戏数据时，务必使用 `game` 构造函数，而不是假设特定的数据格式。要了解 `game` 数据抽象的具体实现，请查阅 `cats.py` 中 `game` 相关的构造函数和选择器定义。



```shell
➜  cats py3 ok -q 09 -u          
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import game, game_string, time_per_word, all_words, all_times, word_at, time
>>> p = [[1, 4, 6, 7], [0, 4, 6, 9]]
>>> words = ['This', 'is', 'fun']
>>> game = time_per_word(p, words)
>>> all_words(game)
? ['This', 'is', 'fun']
-- OK! --

>>> all_times(game)
? [[3,2,1],[4,2,3]]
-- OK! --

>>> p = [[0, 2, 3], [2, 4, 7]]
>>> game = time_per_word(p, ['hello', 'world'])
>>> word_at(game, 1)
? 'world'
-- OK! --

>>> all_times(game)
? [[2,1],[2,3]]
-- OK! --

>>> time(game, 0, 1)
? 1
-- OK! --

---------------------------------------------------------------------
Problem 9 > Suite 1 > Case 2
(cases remaining: 101)

-- Already unlocked --
```



### Problem 10 (2 pt)

实现 `fastest_words`，该函数返回每位玩家输入最快的单词列表。该函数在所有玩家完成打字后调用，并接收一个 **`game`** 参数。

`game` 是一个数据抽象，类似于 **问题 9** 返回的 `game` 对象。你可以使用以下选择器访问 `game` 中的数据：

- **`word_at(game, word_index)`**：获取 `game` 中指定索引 `word_index` 处的单词。
- **`time(game, player_index, word_index)`**：获取玩家 `player_index` 输入 `word_index` 位置的单词所花费的时间。

### 返回值：

`fastest_words` 应返回一个列表，包含每位玩家的单词列表，每个列表中存放该玩家 **相较于其他玩家最快输入的单词**。

- **如果一个单词被多名玩家同时打出最快时间，则优先归属于索引最小的玩家（即最早出现在玩家列表中的玩家）。**
- **务必使用 `game` 数据抽象的访问函数，而不是假设特定的数据格式。**



包含每位玩家的单词列表，每个列表中存放该玩家 **相较于其他玩家最快输入的单词**。可能有多个单词

```shell
➜  cats py3 ok -q 10 -u          
=====================================================================
Assignment: Project 2: Cats
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 1
(cases remaining: 102)

>>> from cats import game, fastest_words
>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 2]
>>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
? ['What','great']
-- Not quite. Try again! --

? [['What'],['great']]
-- Not quite. Try again! --

? [['What'], ['great']]
-- Not quite. Try again! --

? [['What'], ['great', 'luck']]
-- OK! --

>>> p0 = [2, 2, 3]
>>> p1 = [6, 1, 3]
>>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))  # with a tie, choose the first player
? 
-- Not quite. Try again! --

? [['What', 'luck'], ['great']]
-- OK! --

>>> p2 = [4, 3, 1]
>>> fastest_words(game(['What', 'great', 'luck'], [p0, p1, p2]))
? [['What'],['great'],['luck']]
-- OK! --

---------------------------------------------------------------------
Problem 10 > Suite 1 > Case 2
(cases remaining: 101)

-- Already unlocked --
```

