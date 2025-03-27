## Iterators and Generators

生成器还允许我们表示无限序列，例如下面函数所示的自然数序列 (1, 2, …)！

```python
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
```



### Q1: Scale ✅ ❎

实现生成器函数 `scale(it, multiplier)`，该函数对给定的可迭代对象 `it` 中的元素进行缩放（乘以 `multiplier`）后依次生成。

作为额外挑战，尝试使用 `yield from` 语句来编写此函数！



yield from 只能作用于可迭代对象，而 it 本身已经是可迭代对象，可以利用 map 构造一个新的可迭代对象

```python
yield from map(lambda x: x * multiplier, it)
```



### Q2: Hailstone ✅

编写一个生成器来输出 **Hailstone（冰雹）序列**，它的定义如下：

1. 选择一个正整数 `n` 作为起始值。
2. 如果 `n` 是偶数，则将其除以 `2`。
3. 如果 `n` 是奇数，则将其乘以 `3` 并加 `1`。
4. 继续这个过程，直到 `n` 变为 `1`。

**注意：**

- 强烈建议（但不是必须）使用 **递归** 来编写此函数，以进行额外的练习。
- 由于 `hailstone` 需要返回一个生成器，可以使用 `yield from` 来递归调用 `hailstone`！



## WWPD: Objects

### Q3: The Car class ❎

```python
➜  lab07 py3 ok -q wwpd-car -u                 
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Car > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.model
? Model S
-- Not quite. Try again! --

? 'Model S'
-- OK! --

>>> deneros_car.gas = 10
>>> deneros_car.drive()
? 'Tesla Model S goes vroom!'
-- OK! --

>>> deneros_car.drive()
? 'Connot drive!'
-- Not quite. Try again! --

? 'Tesla Model S goes vroom!'
-- Not quite. Try again! --

? 'Connot drive!'
-- Not quite. Try again! --

# 打错字，是 Can 不是 Con
? 'Cannot drive!'
-- OK! --

>>> deneros_car.fill_gas()
? 'Gas level: 20'
-- OK! --

>>> deneros_car.gas
? 20
-- OK! --

>>> Car.gas
? 30
-- OK! --
```



```python
---------------------------------------------------------------------
Car > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.wheels = 2
>>> deneros_car.wheels
? 2
-- OK! --

>>> Car.num_wheels
? 4
-- OK! --

>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? 'Cannot drive!'
-- OK! --

>>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
# wheels 不够
? 'Tesla Model S goes vroom!'
-- Not quite. Try again! --

? 'Cannot drive!'
-- OK! --
```



```python
---------------------------------------------------------------------
Car > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = MonsterTruck('Monster', 'Batmobile')
>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? 'Monster Batmobile goes vroom!'
-- Not quite. Try again! --

(line 1)? 'Vroom! This Monster Truck is huge!'
-- Not quite. Try again! --

(line 1)? Vroom! This Monster Truck is huge!
(line 2)? Monster Batmobile goes vroom!
-- Not quite. Try again! --

(line 1)? Monster Batmobile goes vroom!
-- Not quite. Try again! --

(line 1)? Vroom! This Monster Truck is huge!
(line 2)? Monster Batmobile goes vroom!
-- Not quite. Try again! --

(line 1)? Vroom! This Monster Truck is huge!
(line 2)? Cannot drive!
-- Not quite. Try again! --

# print 无 '', return 有 ''
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed

? Error
-- Not quite. Try again! --

? 'Cannot drive!'
-- Not quite. Try again! --

? 'Tesla Model S goes vroom!'
-- Not quite. Try again! --

? Nothing
-- Not quite. Try again! --

? 'Monster Batmobile goes vroom!'
-- OK! --

>>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

---------------------------------------------------------------------
OK! All cases for Car unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```





## Magic: The Lambda-ing  

在本实验的下一部分，我们将实现一个卡牌游戏！  

你可以通过输入以下命令来启动游戏：  

python3 cardgame.py

目前这个游戏还无法运行。如果你现在执行它，代码会报错，因为我们还没有实现任何内容。等到它运行正常后，你可以使用 `Ctrl-C` 或 `Ctrl-D` 退出游戏并返回到命令行。  

---

### 这个游戏使用了多个不同的文件：

- **所有需要实现的代码** 都在 `classes.py` 文件中。
- **一些游戏的工具代码** 位于 `cardgame.py`，但你不需要打开或阅读这个文件。 
  这个文件不会直接修改任何实例，而是调用不同类的方法，从而严格保持抽象层次。  
- **如果你想修改游戏**，比如添加自定义卡牌和牌组，可以查看 `cards.py` 文件。 
  这里包含所有标准卡牌以及默认的牌组，你可以在此添加新卡牌，或者更改你和对手使用的牌组。 
  这些卡牌的设计并未特别考虑游戏平衡，因此你可以随意调整它们的属性、增加或移除卡牌。  

---

###  **游戏规则**
这个游戏的规则相对复杂，但远不及它的同名游戏。规则如下：

1. 游戏有 **两名玩家**。  
2. 每个玩家都有一副 **手牌** 和一副 **牌库**。  
   - 每轮开始时，每个玩家 **从牌库抽一张牌** 到手牌中。  
   - 如果玩家 **尝试抽牌时牌库已空**，则该玩家 **自动输掉游戏**。  
3. **卡牌属性**：
   
   - 每张卡牌有 **名称**、**攻击力 (ATK)** 和 **防御力 (DEF)**。  
4. **战斗规则**：
   - 每回合，双方各自选择 **一张手牌** 进行对战。  
   - **战斗胜负由“卡牌战斗力”决定**：
     
     - **战斗力计算公式**：
       ```
       玩家卡牌的战斗力 = (卡牌的攻击力) - (对手卡牌的防御力 / 2)
       ```
     - 例如：
       - **玩家 1** 打出一张 **2000 ATK / 1000 DEF** 的卡牌  
       - **玩家 2** 打出一张 **1500 ATK / 3000 DEF** 的卡牌  
       - 计算战斗力：
         ```
         玩家 1:
         2000 - (3000 / 2) = 2000 - 1500 = 500
         ```
         ```
         玩家 2:
         1500 - (1000 / 2) = 1500 - 500 = 1000
         ```
         - **玩家 2 胜出**。  
5. **胜利条件**：
   
   - **最先赢得 8 轮的玩家获胜！**  

---

### **卡牌特殊效果**
我们还可以为游戏添加 **额外效果**（可选部分）。  
每张卡牌属于以下三种类型之一，并且 **在战斗力计算之前** 触发对应效果：

- **导师 (Tutor) 卡**：
  - **让对手弃掉** 并 **重新抽取** 他们手牌中的 **前三张卡牌**。
  
- **助教 (TA) 卡**：
  - **交换对手卡牌的攻击力和防御力**。
  
- **教授 (Professor) 卡**：
  - **将对手卡牌的攻击力和防御力**，**分别加到他们牌库中所有卡牌的攻击力和防御力**。
  - **移除牌库中所有与该教授卡攻击力或防御力相同的卡牌**。



### Q4: Making Cards ✅

要玩卡牌游戏，我们首先需要卡牌，所以让我们来创建一些吧！我们将先实现 **Card（卡牌）类** 的基础功能。

------

### **第一步：实现 `Card` 类的构造方法**（`classes.py` 文件）

请实现 `Card` 类的 **构造方法**，该方法接收 **三个参数**：

1. **`name`**（卡牌名称，字符串类型）
2. **`attack`**（攻击力，整数类型）
3. **`defense`**（防御力，整数类型）

每个 `Card` 实例都应通过 **实例属性** 记录这些值：

- `self.name` 记录 **卡牌名称**
- `self.attack` 记录 **攻击力**
- `self.defense` 记录 **防御力**

------

### **第二步：实现 `power` 方法**

你还需要实现 **`power` 方法**，该方法接收 **另一张卡牌** 作为输入，并计算当前卡牌的 **战斗力（power）**。

战斗力的计算规则可以参考 **游戏规则** 部分：

```
复制编辑
战斗力 = (当前卡牌的攻击力) - (对手卡牌的防御力 / 2)
```

如果对规则不太清楚，可以回顾 **规则部分** 以获取详细说明。



### Q5: Making a Player ✅

现在我们已经有了卡牌（Cards），接下来需要创建 **牌堆（Deck）**，但仍然缺少实际使用它们的 **玩家（Players）**。现在我们将完成 **`Player` 类** 的实现。

------

### **`Player` 类的实例属性**

一个 **`Player`（玩家）实例** 需要具有以下 **三个实例属性**：

1. **`name`**：玩家的名字。
   - 当你开始游戏时，你可以输入你的名字，**它会被转换为字符串并传递给构造方法**。
2. **`deck`**：一个 **`Deck` 类的实例**。
   - 你可以通过 `deck.draw()` 方法从牌堆中抽牌。
3. **`hand`**：一个包含 **`Card` 实例** 的 **列表**，表示玩家的手牌。
   - **每位玩家初始手牌应有 5 张卡**，这些卡需要 **从牌堆中抽取**。
   - 在游戏过程中，玩家可以通过 **索引** 选择手牌中的卡片。
   - 当玩家从牌堆中 **抽取新卡** 时，**新卡会被添加到手牌列表的末尾**。

------

### **第一步：实现 `__init__` 构造方法**

请完成 **`Player` 类的构造方法**，确保 `self.hand` 被正确 **初始化为 5 张从 `deck` 中抽取的卡**。

你可以使用 **`deck.draw()` 方法** 来抽取卡片，不需要关心其内部实现，**直接调用即可**。

------

### **第二步：实现 `draw` 和 `play` 方法**

1. **`draw` 方法**：
   - **从牌堆（`deck`）中抽取一张卡**，并 **将其添加到手牌（`hand`）的末尾**。
   - 你需要调用 `deck.draw()` 来完成抽牌。
2. **`play` 方法**：
   - **根据给定的索引 `index`**，从 **手牌中移除并返回** 一张卡片。
   - 你可以使用 `list.pop(index)` 来移除并返回该卡片。



# Optional Questions

接下来的 **代码编写题** 都将在 **`classes.py` 文件** 中完成。

在以下各个部分中，**不要覆盖** 代码中 **已有的行**。此外，请确保在实现每个方法后 **取消注释所有 `print` 语句**。

这些 `print` 语句用于 **向用户显示信息**，如果更改它们，可能会导致**原本可以通过的测试失败**。



### Q6: Tutors: Flummox ✅

为了让这款卡牌游戏更加有趣，我们的卡牌应该具备**特殊效果**！

我们将通过 **`effect` 方法** 来实现卡牌的效果。该方法接受以下三个参数：

- **`opponent_card`**：对手出的卡牌
- **`current_player`**：当前玩家
- **`opponent_player`**：对手玩家

### 任务：

**实现 `Tutor` 类型卡牌的 `effect` 方法**：

- 使**对手玩家**丢弃手牌中的 **前三张卡牌**。
- 然后，**从牌库中重新抽取 3 张新卡牌**。

**假设**：

- 对手的**手牌至少有 3 张卡**。
- 对手的**牌库至少有 3 张卡**。

### 重要提示：

- **请确保在完成实现后，取消注释 `print` 语句**！
  这些 `print` 语句用于**显示



### Q7: TAs: Shift ✅

现在来为 **TA 类型卡牌** 添加效果！

### 任务：

**实现 `TA` 类型卡牌的 `effect` 方法**：

- **交换** 对手卡牌 (`opponent_card`) 的 **攻击值（attack）** 和 **防御值（defense）**。

### 提示：

- 直接修改 `opponent_card` 的 `attack` 和 `defense` 属性，使它们的值互换。



### Q8: The Professor Arrives ❎

新的挑战者登场了！

### 任务：

**实现 `Professor` 类型卡牌的 `effect` 方法**：

1. **增强玩家卡组**：
   - 将 **对手卡牌 (`opponent_card`) 的攻击值和防御值** **分别加到** **玩家卡组 (`current_player.deck`) 中的所有卡牌上**。
2. **清理对手卡组**：
   - **移除** **所有攻击值或防御值与 `opponent_card` 相同的卡牌**（从 `opponent_player.deck` 中删除）。

### 注意：

- **不要直接遍历并修改列表**，否则可能会导致错误。
- **解决方案**：使用 **列表切片（`[:]`）创建副本** 来遍历，而修改原列表。

