## Hog 游戏规则

在“猪”游戏中，两名玩家轮流进行回合，目标是第一个在回合结束时达到至少100总分。

在每个回合中，当前玩家选择一些骰子来掷，最多可以选择10个骰子。该玩家本回合的得分是骰子结果的总和。

### 普通游戏

掷太多骰子的玩家会面临以下风险：

- **猪叫（Pig out）**：如果任何一个骰子的结果是1，那么当前玩家本回合的得分就是1分。

### 特殊规则，增加趣味

- **免费培根（Free Bacon）**：选择不掷骰子的玩家得分为k+3分，其中k是圆周率小数点后第n位的数字，n是对手的总分数。作为一个特例，如果对手的得分是n=0，那么k=3（即圆周率小数点前的数字）。
- **猪对齐（Swine Align）**：在本回合得分加到当前玩家的总分后，如果两名玩家都有正分且当前玩家得分与对手得分的最大公约数(GCD)至少为10，那么当前玩家再进行一个回合。
- **更多猪（Pig Pass）**：在本回合得分加到当前玩家的总分后，如果当前玩家的得分低于对手的得分且两者之间的差值小于3分，那么当前玩家再进行一个回合。



## 流程

满分 25 分，22 分正确分，1 分截止时间分，2 分覆盖所有部分分



提交：`hog.py`，无需修改其他文件，也不要修改写好的函数



最好经常测试，便于隔离问题

本地测试



## GUI



```shell
$ python3 hog_gui.py
```





## Phase 1: Simulator

### Problem 0

`dice.py` 使用非纯零参数函数表示骰子

- 为什么非纯？每次调用返回可能具有不同的返回值

两种类型骰子

- 1，骰子是公平的，相等概率产生每种可能得结果
- 2，测试骰子函数，确定性测试骰子始终循环显示作为参数传递给 make_test_dice 函数的固定值序列。



理解检测

```shell
---------------------------------------------------------------------
Question 0 > Suite 1 > Case 1
(cases remaining: 2)

>>> from hog import *
>>> test_dice = make_test_dice(4, 1, 2)
>>> test_dice()
? 4
-- OK! --

>>> test_dice() # Second call
? 1
-- OK! --

>>> test_dice() # Third call
? 2
-- OK! --

>>> test_dice() # Fourth call
? 4
-- OK! --

---------------------------------------------------------------------
Question 0 > Suite 2 > Case 1
(cases remaining: 1)

Q: Which of the following is the correct way to "roll" a fair, six-sided die?
Choose the number of the correct choice:
0) six_sided()
1) make_fair_dice(6)
2) make_test_dice(6)
3) six_sided
? 0
-- OK! --

---------------------------------------------------------------------
OK! All cases for Question 0 unlocked.
```



make_test_dice 参数序列为骰子循环固定序列，返回值为函数

six_sided() 绑定新命名，调用



### Porblem 1

完成 `roll_dice` 函数

- 接受 2 参数，num_rolls 非负骰子数和 dice 函数
- 返回分数：1 或结果之和

```shell
---------------------------------------------------------------------
Question 1 > Suite 1 > Case 1
(cases remaining: 59)

>>> from hog import *
>>> roll_dice(2, make_test_dice(4, 6, 1))
? 8
-- Not quite. Try again! --

? 10
-- OK! --

---------------------------------------------------------------------
Question 1 > Suite 1 > Case 5
(cases remaining: 55)

>>> from hog import *
>>> counted_dice = make_test_dice(4, 1, 2, 6)
>>> roll_dice(3, counted_dice)
? 1
-- OK! --

>>> # Make sure you call dice exactly num_rolls times!
>>> # If you call it fewer or more than that, it won't be at the right spot in the cycle for the next roll
>>> # Note that a return statement within a loop ends the loop
>>> roll_dice(1, counted_dice)
? 4
-- Not quite. Try again! --

? 6
-- OK! --

---------------------------------------------------------------------
```



### Problem2

实施 free_bacon，



### Problem3

实施 take_turn 函数，掷出给定骰子返回一次得分



```shell
---------------------------------------------------------------------
Question 3 > Suite 1 > Case 1
(cases remaining: 10)

>>> from hog import *
>>> take_turn(2, 0, make_test_dice(4, 5, 1))
? 15
-- Not quite. Try again! --

? 9
-- OK! --

---------------------------------------------------------------------
Question 3 > Suite 1 > Case 2
(cases remaining: 9)

>>> from hog import *
>>> take_turn(3, 0, make_test_dice(4, 6, 1))
? 11
-- Not quite. Try again! --

? 1
-- OK! --
```

两类情况掷或不掷，思路同官方



### Problem 4a

实施 swine_align，

gcd 辗转相除法



### Problem4b

实施 pig_pass，

```shell
Question 4b > Suite 1 > Case 5
(cases remaining: 103)

>>> from hog import *
>>> pig_pass(23, 23)
? True
-- Not quite. Try again! --

? False
-- OK! --
```

作差，0<差<3即可



### Problem5

实施 play，模拟完整的游戏，玩家轮流掷骰子，直到其中一名玩家达到目标分数。

```shell
---------------------------------------------------------------------
Question 5 > Suite 2 > Case 1
(cases remaining: 108)

>>> import hog
>>> always_three = hog.make_test_dice(3)
>>> always = hog.always_roll
>>> #
>>> # Play function stops at goal
>>> s0, s1 = hog.play(always(5), always(3), score0=91, score1=10, dice=always_three)
>>> s0
? 106
-- OK! --

>>> s1
? 19
-- Not quite. Try again! --

? 10
-- OK! --

---------------------------------------------------------------------
```



```shell
---------------------------------------------------------------------
Question 5 > Suite 3 > Case 1
(cases remaining: 104)

>>> import hog
>>> always_three = hog.make_test_dice(3)
>>> always_seven = hog.make_test_dice(7)
>>> #
>>> # Use strategies
>>> # We recommend working this out turn-by-turn on a piece of paper (use Python for difficult calculations).
>>> strat0 = lambda score, opponent: opponent % 10
>>> strat1 = lambda score, opponent: max((score // 10) - 4, 0)
>>> s0, s1 = hog.play(strat0, strat1, score0=71, score1=80, dice=always_seven)
>>> s0
? 83
-- OK! --

>>> s1
? 108
-- OK! --

---------------------------------------------------------------------
```





## Phase 2: Commentary

实现注释函数

### Problem6

```shell
---------------------------------------------------------------------
Question 6 > Suite 2 > Case 4
(cases remaining: 3)

>>> from hog import play, always_roll
>>> from dice import make_test_dice
>>> #
>>> # Ensure that say is properly updated within the body of play.
>>> def total(s0, s1):
...     print(s0 + s1)
...     return echo
>>> def echo(s0, s1):
...     print(s0, s1)
...     return total
>>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=echo)
(line 1)? 2 0
(line 2)? 4
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 9
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14
(line 5)? 6 10
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14
(line 5)? 9 10
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7 
(line 3)? 4 5
(line 4)? 14
(line 5)? 6 10
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14
(line 5)? 9 7
(line 6)? 14 7
-- Not quite. Try again! --

(line 1)? 2 0
(line 2)? 7
(line 3)? 4 5
(line 4)? 14
(line 5)? 9 7
(line 6)? 21
-- OK! --

---------------------------------------------------------------------
```

两个人公用一个骰子的循环？



2 0

2 5 = 7

4 5  差值小于 3，多一轮

9 5 = 14

9 7

15 7 = 21



### Problem7

实现 announce_highest 函数，

每当特定玩家在回合中获得比以往更多的分数时，此评论功能就会宣布。



```shell
---------------------------------------------------------------------
Question 7 > Suite 1 > Case 3
(cases remaining: 3)

Q: What does the parameter last_score represent?
Choose the number of the correct choice:
0) The current player's score before this turn.
1) The opponent's score before this turn.
2) The last highest gain for the current player.
? 2
-- Not quite. Try again! --

Choose the number of the correct choice:
0) The current player's score before this turn.
1) The opponent's score before this turn.
2) The last highest gain for the current player.
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) The current player's score before this turn.
1) The opponent's score before this turn.
2) The last highest gain for the current player.
? 0
-- OK! --

---------------------------------------------------------------------
```



```
def say(score0, score1):
	
	return say
```



## Phase3: Strategies

### Problem8

实现 make_averaged 函数

```shell
---------------------------------------------------------------------
Question 8 > Suite 2 > Case 2
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(3, 1, 5, 6)
>>> averaged_roll_dice = make_averaged(roll_dice, 1000)
>>> # Average of calling roll_dice 1000 times
>>> # Enter a float (e.g. 1.0) instead of an integer
>>> averaged_roll_dice(2, dice)
? 2.0
-- Not quite. Try again! --

? 6.0
-- OK! --

---------------------------------------------------------------------

一次掷两个，两轮平均
第一轮：3 1，得分 1
第二轮：5 6，得分 11
平均 6.0
```



### Problem9

实现 max_scoring_num_rolls

```shell
---------------------------------------------------------------------
Question 9 > Suite 1 > Case 1
(cases remaining: 8)

Q: If multiple num_rolls are tied for the highest scoring
average, which should you return?
Choose the number of the correct choice:
0) The highest num_rolls
1) A random num_rolls
2) The lowest num_rolls
? 2
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 1
(cases remaining: 7)

>>> from hog import *
>>> dice = make_test_dice(3)   # dice always returns 3
>>> max_scoring_num_rolls(dice, trials_count=1000)
? 1
-- Not quite. Try again! --

? 0
-- Not quite. Try again! --

? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 2
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 2 > Case 3
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 1
(cases remaining: 4)

>>> from hog import *
>>> dice = make_test_dice(2)     # dice always rolls 2
>>> max_scoring_num_rolls(dice, trials_count=1000)
? 1
-- Not quite. Try again! --

? 2
-- Not quite. Try again! --

? 10
-- OK! --

---------------------------------------------------------------------
Question 9 > Suite 3 > Case 2
(cases remaining: 3)

>>> from hog import *
>>> dice = make_test_dice(1, 2)  # dice alternates 1 and 2
>>> max_scoring_num_rolls(dice, trials_count=1000)
? 2
-- Not quite. Try again! --

? 10
-- Not quite. Try again! --

? 3
-- Not quite. Try again! --

? 4
-- Not quite. Try again! --

? 5
-- Not quite. Try again! --

? 6
-- Not quite. Try again! --

? 7
-- Not quite. Try again! --

? 8
-- Not quite. Try again! --

? 9
-- Not quite. Try again! --

? 10
-- Not quite. Try again! --

? 0
-- Not quite. Try again! --

? 1
-- OK! --


每轮丢 1 个：
1
2
1
.....
平均 1.5

每轮丢 2 个：
1 2 得 1 分
1 2 得 1 分
....
平均 1 分
---------------------------------------------------------------------
```



### Problem10

利用 Free Bacon 规则，在最有利的时候掷出 0



### Problem 11

```shell
---------------------------------------------------------------------
Question 11 > Suite 1 > Case 1
(cases remaining: 105)

>>> from hog import *
>>> extra_turn_strategy(10, 19, cutoff=8, num_rolls=6)
? 6
-- Not quite. Try again! --

? 0
-- OK! --
10 + 第 19 位圆周率+3 = 17，与 19 差 2，多一轮，因此 0
---------------------------------------------------------------------
Question 11 > Suite 1 > Case 2
(cases remaining: 104)

>>> from hog import *
>>> extra_turn_strategy(30, 54, cutoff=7, num_rolls=6)
? 6
-- OK! --
30 + 第 54 位圆周率+3 = 33，不多一轮，bacon 策略
---------------------------------------------------------------------
Question 11 > Suite 1 > Case 3
(cases remaining: 103)

>>> from hog import *
>>> extra_turn_strategy(17, 36, cutoff=100, num_rolls=6)
? 6
-- Not quite. Try again! --

? 0
-- OK! --
30 + 第 36 位圆周率+3 = 24，公约数 12，多一轮，因此 0
---------------------------------------------------------------------
```

理解逻辑不对，应该

```python
if extra_turn(score+free_bacon(opponent_score), opponent_score):
    return 0
```



### Problem 12

实施 final_strategy

extra_turn_strategy 是一个很好的默认策略。 

得分超过 100 分是没有意义的。检查您是否可以通过掷 0、1 或 2 个骰子来获胜。如果您处于领先地位，您可能会承担更少的风险。 

尝试强制进行额外的回合。 

仔细选择 num_rolls 和 cutoff 参数。
