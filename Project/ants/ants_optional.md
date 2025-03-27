## Optional Problems

### Optional Problem 1

NinjaAnt 能**伤害所有经过它的蜜蜂**，但**它不会被蜜蜂攻击**。

NinjaAnt **不会阻挡**蜜蜂的前进路线。为了实现这一点，你需要完成以下步骤：

1. **修改 `Ant` 类**，添加一个新的**类属性** `blocks_path`，默认值为 `True`。
   - 这样，所有普通的蚂蚁都会阻挡蜜蜂的前进。
   - 在 **NinjaAnt** 类中，将 `blocks_path` 设置为 `False`，使其不会挡路。
2. **修改 `Bee` 类的 `blocked` 方法**，让蜜蜂检查它前方是否有蚂蚁：
   - 如果**没有蚂蚁**，蜜蜂可以继续移动。
   - 如果**有蚂蚁**，但它的 `blocks_path` 为 `False`（例如 NinjaAnt），蜜蜂仍然可以继续前进。
3. **实现 `NinjaAnt.action` 方法**，让它在每回合对自己所在位置的**所有蜜蜂**造成 `damage` 伤害：
   - **注意**：就像 **FireAnt** 一样，你需要遍历蜜蜂的列表，并确保循环不会因为蜜蜂死亡而出错。

------

### 💡 **提示**：

- 你可以尝试在**纸上画出测试案例**，以帮助理解 NinjaAnt 的行为。
- `self.place.bees[:]` 可以用于遍历蜜蜂的同时避免修改原列表导致的错误。





```python
➜  ants py3 ok -q optional1 -u          
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 1
(cases remaining: 15)

Q: Which Ant types have a blocks_path attribute?
Choose the number of the correct choice:
0) All Ant types except for NinjaAnt have a blocks_path attribute
1) Only the NinjaAnt has a blocks_path attribute
2) All Ant types have a blocks_path attribute that is inherited from
   the Ant superclass
3) None of the Ant subclasses have a blocks_path attribute
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 2
(cases remaining: 14)

Q: What is the value of blocks_path for each Ant subclass?
Choose the number of the correct choice:
0) blocks_path is False for all Ants
1) blocks_path is False for every Ant subclass except NinjaAnt
2) blocks_path is True for all Ants
3) blocks_path is True for every Ant subclass except NinjaAnt
? 3
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 3
(cases remaining: 13)

Q: When is the path of a Bee blocked?
Choose the number of the correct choice:
0) When there is not an NinjaAnt in the Bee's place
1) When there are no Ants in the Bee's place
2) When there is an Ant in the Bee's place
3) When there is an Ant whose blocks_path attribute is True in the
   Bee's place
? 3
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 1 > Case 4
(cases remaining: 12)

Q: What does a NinjaAnt do to each Bee that flies in its place?
Choose the number of the correct choice:
0) Nothing, the NinjaAnt doesn't damage Bees
1) Reduces the Bee's armor by the NinjaAnt's damage attribute
2) Blocks the Bee's path
3) Reduces the Bee's armor to 0
? 1
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 1
(cases remaining: 11)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing NinjaAnt parameters
>>> ninja = NinjaAnt()
>>> ninja.armor
? 1
-- OK! --

>>> NinjaAnt.food_cost
? 5
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 2
(cases remaining: 10)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing blocks_path
>>> NinjaAnt.blocks_path
? False
-- OK! --

>>> HungryAnt.blocks_path
? True
-- OK! --

>>> FireAnt.blocks_path
? True
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 3
(cases remaining: 9)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing NinjaAnts do not block bees
>>> p0 = gamestate.places["tunnel_0_0"]
>>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
>>> bee = Bee(2)
>>> ninja = NinjaAnt()
>>> thrower = ThrowerAnt()
>>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
>>> p1.add_insect(bee)
>>> p1.add_insect(ninja)              # Add the Bee and NinjaAnt to p1
>>> bee.action(gamestate)
>>> bee.place is ninja.place          # Did NinjaAnt block the Bee from moving?
? True
-- Not quite. Try again! --

? False
-- OK! --

>>> bee.place is p0
? True
-- OK! --

>>> ninja.armor
? 1
-- OK! --

>>> bee.action(gamestate)
>>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
? True
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 4
(cases remaining: 8)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing non-blocking ants do not block bees
>>> p0 = gamestate.places["tunnel_0_0"]
>>> p1 = gamestate.places["tunnel_0_1"]  # p0 is p1's exit
>>> bee = Bee(2)
>>> ninja_fire = FireAnt(1)
>>> ninja_fire.blocks_path = False
>>> thrower = ThrowerAnt()
>>> p0.add_insect(thrower)            # Add ThrowerAnt to p0
>>> p1.add_insect(bee)
>>> p1.add_insect(ninja_fire)              # Add the Bee and NinjaAnt to p1
>>> bee.action(gamestate)
>>> bee.place is ninja_fire.place          # Did the "ninjaish" FireAnt block the Bee from moving?
? True
-- Not quite. Try again! --

? False
-- OK! --

>>> bee.place is p0
? True
-- OK! --

>>> ninja_fire.armor
? 4
-- Not quite. Try again! --

? 3
-- Not quite. Try again! --

? 2
-- Not quite. Try again! --

? 1
-- OK! --

>>> bee.action(gamestate)
>>> bee.place is p0                   # Did ThrowerAnt block the Bee from moving?
? True
-- OK! --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 5
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 6
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 7
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 8
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 9
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 1 > Suite 2 > Case 10
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 1 > Suite 3 > Case 1
(cases remaining: 1)


>>> from ants import *
>>> NinjaAnt.implemented
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem Optional 1 unlocked.

Performing authentication
Please enter your school email (.edu): ^C%
```



### Optional Problem 2

### **加强蚂蚁的防御能力——BodyguardAnt（保镖蚂蚁）**

当前我们的蚂蚁**非常脆弱**，为了帮助它们在蜜蜂的攻击下存活更久，我们要引入**BodyguardAnt（保镖蚂蚁）**。

------

### **🌟 BodyguardAnt 的特点：**

1. **它是一个 ContainerAnt（容器蚂蚁）**：
   - 可以**容纳另一个蚂蚁**，并在**同一个 Place 里保护它**。
   - 当蜜蜂攻击时，**只有外层的容器蚂蚁（BodyguardAnt）会受到伤害**，而内部的蚂蚁不会受伤。
   - **如果容器蚂蚁死亡，内部的蚂蚁仍然留在原地**，并可以继续行动。
2. **每个 ContainerAnt 有一个 `contained_ant` 实例属性**：
   - 初始值为 `None`，表示**当前没有保护的蚂蚁**。
   - 需要实现 `contain_ant` 方法，将传入的 `ant` 赋值给 `contained_ant`。
3. **实现 `ContainerAnt.action` 方法**：
   - 如果 `contained_ant` 不为空，则调用 `contained_ant.action()` 让它执行原本的动作。

------

### **📌 需要修改的内容：**

1. **实现 `ContainerAnt.can_contain(other_ant)` 方法**，让它返回 `True` 当且仅当：`Ant.can_contain` 默认返回 `False`，**需要在 `ContainerAnt` 里重写这个方法**。
   - 该容器蚂蚁**当前未容纳其他蚂蚁**。
   - `other_ant` **不是一个容器蚂蚁**（容器不能嵌套容器）。
2. **修改 `Ant.add_to` 方法**，以支持**一个容器和一个普通蚂蚁共存**，具体规则如下：
   - **如果该位置已经有蚂蚁，并且它可以容纳当前蚂蚁，则让它容纳当前蚂蚁**。
   - **如果当前蚂蚁可以容纳该位置已有的蚂蚁，则让当前蚂蚁容纳它**。
   - **如果两个蚂蚁都无法容纳对方，抛出 `AssertionError`（与原代码一致）**。
3. **创建 `BodyguardAnt.__init__` 方法**：
   - 修改默认的 `armor` 值，使其更耐打。

------

### 💡 **提示**

- ```
  isinstance(obj, ClassName)
  ```

   可以用于检查对象 

  ```
  obj
  ```

   是否是 

  ```
  ClassName
  ```

   类的实例。例如：

  ```
  a = Foo()
  isinstance(a, Foo)  # 返回 True
  ```

- ```
  ContainerAnt.__init__
  ```

   方法的定义如下：

  ```
  def __init__(self, *args, **kwargs):
      Ant.__init__(self, *args, **kwargs)
      self.contained_ant = None
  ```

  - `*args` 代表**所有位置参数**，`**kwargs` 代表**所有关键字参数**，确保它们**都传递给 `Ant.__init__`**。
  - 这实际上等价于 `Ant.__init__`，只是额外初始化了 `self.contained_ant = None`。

### 

```python
  ants py3 ok -q optional2 -u                 
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem Optional 2 > Suite 1 > Case 1
(cases remaining: 18)

Q: Which Ant does a BodyguardAnt guard?
Choose the number of the correct choice:
0) All the Ant instances in the gamestate
1) The Ant instance in the place closest to its own place
2) The Ant instance that is in the same place as itself
3) A random Ant instance in the gamestate
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 2 > Suite 1 > Case 2
(cases remaining: 17)

Q: How does a BodyguardAnt guard its ant?
Choose the number of the correct choice:
0) By allowing Bees to pass without attacking
1) By attacking Bees that try to attack it
2) By increasing the ant's armor
3) By protecting the ant from Bees and allowing it to perform its original action
? 3
-- OK! --

---------------------------------------------------------------------
Problem Optional 2 > Suite 1 > Case 3
(cases remaining: 16)

Q: Where is the ant contained by a BodyguardAnt stored?
Choose the number of the correct choice:
0) In its place's ant instance attribute
1) Nowhere, a BodyguardAnt has no knowledge of the ant that it's protecting
2) In the BodyguardAnt's contained_ant instance attribute
3) In the BodyguardAnt's contained_ant class attribute
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 2 > Suite 1 > Case 4
(cases remaining: 15)

Q: When can a second Ant be added to a place that already contains an Ant?
Choose the number of the correct choice:
0) When both Ant instances are containers
1) When exactly one of the Ant instances is a container and the
   container ant does not already contain another ant
2) There can never be two Ant instances in the same place
3) When exactly one of the Ant instances is a container
? 1
-- OK! --

---------------------------------------------------------------------
Problem Optional 2 > Suite 1 > Case 5
(cases remaining: 14)

Q: If two Ants occupy the same Place, what is stored in that place's ant
instance attribute?
Choose the number of the correct choice:
0) The Ant being contained
1) Whichever Ant was placed there first
2) The container Ant
3) A list containing both Ants
? 1
-- Not quite. Try again! --

Choose the number of the correct choice:
0) The Ant being contained
1) Whichever Ant was placed there first
2) The container Ant
3) A list containing both Ants
? 0
-- Not quite. Try again! --

Choose the number of the correct choice:
0) The Ant being contained
1) Whichever Ant was placed there first
2) The container Ant
3) A list containing both Ants
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 2 > Suite 2 > Case 1
(cases remaining: 13)

>>> from ants import *
>>> # Testing BodyguardAnt parameters
>>> bodyguard = BodyguardAnt()
>>> BodyguardAnt.food_cost
? 4
-- OK! --

>>> bodyguard.armor
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 2 > Suite 2 > Case 2
(cases remaining: 12)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 1
(cases remaining: 11)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 2
(cases remaining: 10)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 3
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 4
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 5
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 6
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 7
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 8
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 9
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 3 > Case 10
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 2 > Suite 4 > Case 1
(cases remaining: 1)


>>> from ants import *
>>> BodyguardAnt.implemented
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem Optional 2 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Optional Problem 3

BodyguardAnt 提供了出色的防御，但有人说，最好的防御就是进攻。

TankAnt 是一种容器蚂蚁，它可以保护同一位置的另一只蚂蚁，同时每回合对该位置的所有蜜蜂造成 1 点伤害。

你不需要修改 **TankAnt** 以外的任何代码。如果你发现自己需要更改其他地方的代码，请尝试以更通用的方式编写前一个问题的代码，使其不仅适用于 **BodyguardAnt** 和 **TankAnt**，而是适用于所有“容器蚂蚁”（container ants）。

**在编写代码后，测试你的实现：**



```python
➜  ants py3 ok -q optional3 -u                 
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem Optional 3 > Suite 1 > Case 1
(cases remaining: 13)

Q: Besides costing more to deploy, what is the only difference between a
TankAnt and a BodyguardAnt?
Choose the number of the correct choice:
0) A TankAnt increases the damage of the ant it contains
1) A TankAnt has greater armor than a BodyguardAnt
2) A TankAnt does damage to all Bees in its place each turn
3) A TankAnt can contain multiple ants
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 3 > Suite 2 > Case 1
(cases remaining: 12)

>>> from ants_plans import *
>>> from ants import *
>>> beehive, layout = Hive(make_test_assault_plan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> #
>>> # Testing TankAnt parameters
>>> TankAnt.food_cost
? 6
-- OK! --

>>> TankAnt.damage
? 2
-- Not quite. Try again! --

? 1
-- OK! --

>>> tank = TankAnt()
>>> tank.armor
? 2
-- OK! --

---------------------------------------------------------------------
Problem Optional 3 > Suite 2 > Case 2
(cases remaining: 11)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 2 > Case 3
(cases remaining: 10)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 1
(cases remaining: 9)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 2
(cases remaining: 8)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 3
(cases remaining: 7)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 4
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 5
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 6
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 3 > Case 7
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 3 > Suite 4 > Case 1
(cases remaining: 2)


>>> from ants import *
>>> TankAnt.implemented
? True
-- OK! --

---------------------------------------------------------------------
Problem Optional 3 > Suite 4 > Case 2
(cases remaining: 1)

-- Already unlocked --

---------------------------------------------------------------------
OK! All cases for Problem Optional 3 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Optional Problem 4

实现两个最终的投掷蚂蚁（ThrowerAnt），它们的攻击力为 **0**，但会在攻击命中的蜜蜂（Bee）**临时施加一种“状态”**，影响该蜜蜂的 **action 方法**。这种状态会替代蜜蜂的默认行为，并持续 **一定回合数**（即 `gamestate.time` 的调用次数），之后蜜蜂的 `action` 会恢复到原来的行为。

------

### **需要实现的两种蚂蚁**

1. **SlowThrower**：向蜜蜂投掷粘稠的糖浆，使其进入 **“缓慢”状态**，持续 **3** 个回合。
2. **ScaryThrower**：恐吓附近的一只蜜蜂，使其后退而不是前进（如果蜜蜂已经在最靠近蜂巢的位置，且无法继续后退，则保持不动）。这种 “恐吓”状态持续 2个回合。
   - **一个蜜蜂只能被恐吓一次，之后不会再受影响**。

------

### **需要实现的 3 个函数**

#### **1. `make_slow`**

- 这是一个“状态”函数，它接收：
  - **`action` 方法（蜜蜂的原始行为）**
  - **`bee`（被施加状态的蜜蜂）**
- 返回一个新的 action方法：
  - 在偶数回合（`gamestate.time % 2 == 0`）执行原始 `action`
  - 在奇数回合不执行任何操作（`pass`）

#### **2. `make_scare`**

- 也是一个“状态”函数，接收：
  - **`action` 方法（蜜蜂的原始行为）**
  - **`bee`（被施加状态的蜜蜂）**
- 返回一个新的 action方法，使蜜蜂后退
  - 如果蜜蜂无法后退（已在最左端），则保持不动。

#### **3. `apply_status`**

- 该函数应用一个状态（`make_slow` 或 `make_scare`）到 **某只蜜蜂**，并让该状态持续 **特定回合数**。
- 状态的作用方式：
  1. **想象蜜蜂有一个“状态列表”**，其中每个状态都会修改 `action` 方法。
  2. 当状态的持续时间结束，它会**自动移除**，蜜蜂的 `action` 恢复为上一个状态。
  3. `apply_status` **将新状态加入到“状态列表”的末尾**，以便它在当前所有状态之后生效。
  4. **不一定要真的用一个“列表”存储状态**，但思维上可以这样理解。

------

### **提示**

1. **如何让蜜蜂后退？**

   - 你可以给蜜蜂对象增加一个变量，比如 `self.reversed = True/False`，用来表示它是否应该后退。
   - 当蜜蜂的 `action` 方法被 `make_scare` 修改时，应该让它向反方向移动。
   - 当 `make_scare` 作用结束后，需要恢复蜜蜂的默认方向。

2. **如何修改 `action` 方法？**

   - Python 允许你直接修改实例的方法：

     ```
     class X: pass
     def f(x): return x ** 3
     x = X()
     x.f = f  # 绑定新的方法
     print(x.f(2))  # 输出 8
     ```

   - 你可以利用这个机制，为蜜蜂创建一个新的 `action` 方法，并在 `apply_status` 结束时恢复它。

------

### **示例：蜜蜂在不同回合的行为**

假设一只蜜蜂被两只 `SlowThrower` 命中：

- **第一只 `SlowThrower` 作用 3 轮**

- **第二只 `SlowThrower` 作用 2 轮**

- 结果：

  | 时间 | 作用状态                      | 是否移动 |
  | ---- | ----------------------------- | -------- |
  | 1    | 被两次 `SlowThrower` 影响     | ❌        |
  | 2    | 被两次 `SlowThrower` 影响     | ✅        |
  | 3    | 被第一只 `SlowThrower` 影响   | ❌        |
  | 4    | 仅剩第二只 `SlowThrower` 影响 | ✅        |
  | 5    | 仅剩第二只 `SlowThrower` 影响 | ❌        |
  | 6    | 没有任何 `SlowThrower` 影响   | ✅        |

最终，蜜蜂会交替移动，并在所有状态结束后恢复正常。



```python
➜  ants py3 ok -q optional4 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 1
(cases remaining: 10)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Testing status parameters
>>> slow = SlowThrower()
>>> scary = ScaryThrower()
>>> SlowThrower.food_cost
? 4
-- OK! --

>>> ScaryThrower.food_cost
? 6
-- OK! --

>>> slow.armor
? 1
-- OK! --

>>> scary.armor
? 1
-- OK! --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 2
(cases remaining: 9)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Testing Slow
>>> slow = SlowThrower()
>>> bee = Bee(3)
>>> gamestate.places["tunnel_0_0"].add_insect(slow)
>>> gamestate.places["tunnel_0_4"].add_insect(bee)
>>> slow.action(gamestate)
>>> gamestate.time = 1
>>> bee.action(gamestate)
>>> bee.place.name # SlowThrower should cause slowness on odd turns
? tunnel_0_4
-- Not quite. Try again! --

? "tunnel_0_4"
-- OK! --

>>> gamestate.time += 1
>>> bee.action(gamestate)
>>> bee.place.name # SlowThrower should cause slowness on odd turns
? "tunnel_0_4"
-- Not quite. Try again! --

? "tunnel_0_3"
-- OK! --

>>> for _ in range(3):
...    gamestate.time += 1
...    bee.action(gamestate)
>>> bee.place.name
? "tunnel_0_2"
-- Not quite. Try again! --

? "tunnel_0_3"
-- Not quite. Try again! --

? "tunnel_0_1"
-- OK! --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 3
(cases remaining: 8)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Testing Scare
>>> scary = ScaryThrower()
>>> bee = Bee(3)
>>> gamestate.places["tunnel_0_0"].add_insect(scary)
>>> gamestate.places["tunnel_0_4"].add_insect(bee)
>>> scary.action(gamestate)
>>> bee.action(gamestate)
>>> bee.place.name # ScaryThrower should scare for two turns
? "tunnel_0_5"
-- OK! --

>>> bee.action(gamestate)
>>> bee.place.name # ScaryThrower should scare for two turns
? "tunnel_0_6"
-- OK! --

>>> bee.action(gamestate)
>>> bee.place.name
? "tunnel_0_5"
-- OK! --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 4
(cases remaining: 7)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> # Scary stings an ant
>>> scary = ScaryThrower()
>>> harvester = HarvesterAnt()
>>> bee = Bee(3)
>>> gamestate.places["tunnel_0_0"].add_insect(scary)
>>> gamestate.places["tunnel_0_4"].add_insect(bee)
>>> gamestate.places["tunnel_0_5"].add_insect(harvester)
>>> scary.action(gamestate)
>>> bee.action(gamestate)
>>> bee.place.name # ScaryThrower should scare for two turns
? "tunnel_0_5"
-- OK! --

>>> harvester.armor
? 1
-- OK! --

>>> bee.action(gamestate)
>>> harvester.armor
? 0
-- OK! --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 5
(cases remaining: 6)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 6
(cases remaining: 5)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 7
(cases remaining: 4)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 8
(cases remaining: 3)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 9
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 4 > Suite 1 > Case 10
(cases remaining: 1)

>>> from ants import *
>>> beehive, layout = Hive(AssaultPlan()), dry_layout
>>> dimensions = (1, 9)
>>> gamestate = GameState(None, beehive, ant_types(), layout, dimensions)
>>> ScaryThrower.implemented
? True
-- OK! --

>>> SlowThrower.implemented
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem Optional 4 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```



### Optional Problem 5

我们长期以来一直在秘密研发这种蚂蚁。它太危险了，以至于我们不得不将其锁在**CS61A 地下超级机密金库**中，但现在我们终于认为它可以投入战斗了。

在本题中，你需要实现最终形态的蚂蚁 —— **LaserAnt**，它是 **ThrowerAnt** 的一种**特殊变种**。

------

### **LaserAnt 的能力**

LaserAnt 使用强力**激光**攻击**所有站在它前进路径上的生物**。它的攻击范围包括：

- 它**所在的位置**（不包括自己，但包括其容器，如果有的话）
- 它**前方的所有位置**
- **不包括 Hive（蜂巢）**

LaserAnt **攻击所有生物**，无论是 **蜜蜂（Bees）** 还是 **蚂蚁（Ants）**，都可能被其波及。

------

### **限制机制**

LaserAnt 过于强大，因此它的激光有**两种削弱机制**：

1. 距离削弱
   - LaserAnt 的基础伤害值为 **2**。
   - **每前进一格**，伤害值会减少 **0.2**。
2. 电池能量限制
   - **每次成功命中一个生物**，LaserAnt 的**总伤害值减少 0.05**。
   - 如果伤害值变为负数，则伤害设为 **0**（不会对生物造成伤害）。

------

### **需要实现的函数**

为了完成 LaserAnt 的实现，你需要：

1. **`insects_in_front(self, beehive) -> dict`**
   - 这是一个实例方法，由 `action` 方法调用。返回一个字典，其中：
     - **键（key）：** `Insect`（生物实例，包括蜜蜂和蚂蚁）
     - **值（value）：** 该生物距离 LaserAnt 的**格数**（位置间隔）。
   - 该字典应该包含：
     - LaserAnt **所在位置**（不包括 LaserAnt 自己，但包括其容器）
     - LaserAnt **前方的所有位置**
     - **不包括 Hive（蜂巢）**
2. **`calculate_damage(self, distance: int) -> float`**
   - 这是一个实例方法，计算某个生物应该受到的伤害值。
   - 计算方式：
     - **基础伤害值**： `2`
     - **距离衰减**： `-0.2 * distance`
     - **电池消耗**： `-0.05 * self.insects_shot`
     - **如果伤害值变为负数，则返回 0**
   - `self.insects_shot` **记录了 LaserAnt 迄今为止攻击过的生物数量**。

------

### **你还可能需要**

- **适当地设置类属性和实例属性**，确保 LaserAnt 具有正确的伤害值、攻击方式等。

------

### **运行测试**

在实现完代码后，你可以运行提供的基本测试：

```
python3 ok -q optional5
```



```python
➜  ants py3 ok -q optional5 -u
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Problem Optional 5 > Suite 1 > Case 1
(cases remaining: 2)

-- Already unlocked --

---------------------------------------------------------------------
Problem Optional 5 > Suite 2 > Case 1
(cases remaining: 1)


>>> from ants import *
>>> LaserAnt.implemented
? True
-- OK! --

---------------------------------------------------------------------
OK! All cases for Problem Optional 5 unlocked.

Performing authentication
Please enter your school email (.edu): OK is up to date
```





```python
➜  ants py3 ok --score 
=====================================================================
Assignment: Project 3: Ants Vs. SomeBees
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Problem 0
    Passed: 1
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 1
    Passed: 3
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 2
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 3
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 4
    Passed: 4
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 5
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 6
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 7
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 8
    Passed: 2
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem 9
    Passed: 3
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Problem EC
    Passed: 4
    Failed: 0
[ooooooooook] 100.0% passed

---------------------------------------------------------------------
Point breakdown
    Problem 0: 0.0/0
    Problem 1: 1.0/1
    Problem 2: 3.0/3
    Problem 3: 3.0/3
    Problem 4: 3.0/3
    Problem 5: 3.0/3
    Problem 6: 3.0/3
    Problem 7: 2.0/2
    Problem 8: 2.0/2
    Problem 9: 2.0/2
    Problem EC: 2.0/2

Score:
    Total: 24.0

Performing authentication
Please enter your school email (.edu): OK is up to date
```

