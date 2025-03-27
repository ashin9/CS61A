# Topics

 如果你需要复习本次实验的相关内容，或者在你的计算机上运行 SQL 或 SQLite 时遇到了问题，可以查阅本节内容。
 当然，你也可以直接跳到问题部分，在遇到困难时再回来看这里。

## SQL Basics

你可以通过从零开始或基于已有表格创建 SQL 表。

下面这个语句展示了如何通过直接指定列名和数据值（而不引用其他表格）来创建表格。每一个 `SELECT` 子句表示一行数据，`UNION` 将多行合并成一个完整的表格。`AS` 子句为每一列指定名称，后续的 `SELECT` 子句可以省略列名，只需要提供对应的值即可。

```sql
CREATE TABLE [表名] AS
  SELECT [值1] AS [列1], [值2] AS [列2], ... UNION
  SELECT [值3],          [值4],          ... UNION
  SELECT [值5],          [值6],          ...;
```

比如，我们想创建一个 `big_game` 表，记录每一年加州大学伯克利和斯坦福大学的比赛得分情况。这个表包含三列：`berkeley`（伯克利得分）、`stanford`（斯坦福得分）和 `year`（年份）。

可以使用如下 `CREATE TABLE` 语句创建：

```sql
CREATE TABLE big_game AS
  SELECT 30 AS berkeley, 7 AS stanford, 2002 AS year UNION
  SELECT 28,             16,           2003         UNION
  SELECT 17,             38,           2014;
```

------

### 从表格中查询数据

更常见的情况是，我们通过 `SELECT` 语句，从已有的表中选择我们需要的列和数据，创建新的结果表或获取查询结果。

基本的查询语法如下：

```sql
SELECT [列名] FROM [表名] WHERE [条件] ORDER BY [列名] LIMIT [限制行数];
```

具体说明如下：

- `SELECT [列名]`：告诉 SQL 我们需要哪些列的数据。`列名` 之间用逗号分隔，如果需要选择全部列，可以使用 `*`。
- `FROM [表名]`：告诉 SQL 从哪个表查询数据。如果需要跨多个表查询，可以参考“连接（joins）”部分。
- `WHERE [条件]`：对返回的行进行条件筛选，只返回满足 `条件` 的行。`条件` 是一个布尔表达式。
- `ORDER BY [列名]`：对结果按照指定列排序，列名可以是多个，用逗号分隔。
- `LIMIT [数量]`：限制返回结果的行数。

> 注意：SQL 关键字（如 `SELECT`、`FROM` 等）通常会大写，这是一种风格约定，可以提高代码的可读性。不过即使不用大写，SQL 语句也是可以正常执行的。

------

### 示例

1. 查询 `big_game` 表中伯克利得分大于 2002 年的比赛得分：

```sql
sqlite> SELECT berkeley FROM big_game WHERE year > 2002;
28
17
```

1. 查询伯克利赢得比赛的年份两校的得分：

```sql
sqlite> SELECT berkeley, stanford FROM big_game WHERE berkeley > stanford;
30|7
28|16
```

1. 查询斯坦福得分超过 15 分的年份：

```sql
sqlite> SELECT year FROM big_game WHERE stanford > 15;
2003
2014
```

------

### SQL 运算符

在 `SELECT`、`WHERE` 和 `ORDER BY` 子句中，可以使用各种运算符来编写表达式：

- 比较运算符：`=`, `>`, `<`, `<=`, `>=`, `<>` 或 `!=`（不等于）
- 布尔运算符：`AND`, `OR`
- 算术运算符：`+`, `-`, `*`, `/`
- 字符串拼接运算符：`||`

------

### 运算符示例

1. 每一年伯克利得分与斯坦福得分的比值：

```sql
sqlite> SELECT berkeley * 1.0 / stanford FROM big_game;
0.447368421052632
1.75
4.28571428571429
```

1. 查询伯克利和斯坦福得分都大于 10 分时，两队总分之和：

```sql
sqlite> SELECT berkeley + stanford FROM big_game WHERE berkeley > 10 AND stanford > 10;
55
44
```

1. 查询返回单行单列的文本 `hello world`：

```sql
sqlite> SELECT "hello" || " " || "world";
hello world
```

------

## 连接（Joins）

如果要从多个表中查询数据，我们可以使用 **连接（join）**。连接有很多种类型，但这里只需要关注 **内连接（inner join）**。要在两个或多个表上执行内连接，只需在 `SELECT` 语句的 `FROM` 子句中列出所有表：

```sql
SELECT [列名] FROM [表1], [表2], ... WHERE [条件] ORDER BY [列名] LIMIT [限制行数];
```

我们既可以从不同的表中查询，也可以在同一个表中多次引用查询。

------

### 例子

假设有一个 `coaches` 表，记录了从 2002 年以来加州大学伯克利橄榄球队的主教练信息：

```sql
CREATE TABLE coaches AS
  SELECT "Jeff Tedford" AS name, 2002 AS start, 2012 AS end UNION
  SELECT "Sonny Dykes"         , 2013         , 2016        UNION
  SELECT "Justin Wilcox"       , 2017         , null;
```

如果我们直接把 `big_game` 表和 `coaches` 表连接，不加任何条件，默认返回的是 **笛卡尔积（Cartesian product）**。也就是说，每一行 `big_game` 的记录会和 `coaches` 表的每一行进行组合。

------

### 条件连接

如果我们希望在每场比赛中匹配出对应赛季的教练，就需要通过 `WHERE` 子句比较两个表中的列值：

```sql
sqlite> SELECT * FROM big_game, coaches WHERE year >= start AND year <= end;
```

结果：

```
复制编辑
17|38|2014|Sonny Dykes|2013|2016
28|16|2003|Jeff Tedford|2002|2012
30|7|2002|Jeff Tedford|2002|2012
```

------

### 查询获胜场次

以下查询输出了在 `big_game` 表中伯克利取胜时的教练姓名和年份：

```sql
sqlite> SELECT name, year FROM big_game, coaches
...>        WHERE berkeley > stanford AND year >= start AND year <= end;
```

结果：

```nginx
Jeff Tedford|2003
Jeff Tedford|2002
```

------

### 别名（Aliases）

上面的查询中，列名没有歧义。比如 `name` 字段只在 `coaches` 表中出现，所以不需要特别说明它属于哪个表。

但是，如果在连接的表中有重复列名（比如 `year`），或者我们对同一个表进行多次引用时，就必须使用别名来区分不同的表来源。

------

### 自连接（Self-Join）示例

比如，我们想比较 `big_game` 中某一场比赛与之前所有比赛的分差。由于 `big_game` 中每一行代表一场比赛，我们需要将 `big_game` 表与自身连接：

```sql
sqlite> SELECT b.berkeley - a.berkeley, b.stanford - a.stanford, a.year, b.year
...>        FROM big_game AS a, big_game AS b WHERE a.year < b.year;
```

结果：

```diff
-11|22|2003|2014
-13|21|2002|2014
-2|9|2002|2003
```

在这个查询中：

- `a` 是 `big_game` 表的一个别名，表示第一场比赛。
- `b` 是 `big_game` 表的另一个别名，表示另一场比赛。
- 通过 `a.year < b.year` 这个条件，我们只比较早于 `b` 的 `a` 比赛。
- 使用 `a.berkeley`、`a.stanford` 这样的点符号（dot notation）可以清晰表示列是从哪个别名对应的表中来的。

------

### 总结

- 多表查询时，`FROM` 中列出多个表，`WHERE` 中写好连接条件。
- 如果有重名列或者要引用同一张表的不同实例，记得加别名（`AS`）。
- 多表连接默认产生的是笛卡尔积，需要 `WHERE` 子句来筛选有意义的结果。

如果还想了解 `LEFT JOIN`、`RIGHT JOIN` 等高级连接，咱们也可以继续聊！



# The Survey Data!

在周二，我们邀请你和其他同学完成了一个简短的在线问卷调查（通过 Google Forms），题目都是一些相对随机但有趣的问题。本次实验中，我们将通过编写 SQL 查询来分析这份问卷调查的结果，看看能否从数据中发现一些有趣的内容。

------

### 数据结构说明

首先，查看 `data.sql` 文件，了解里面定义的表结构。你将主要操作以下两个表：

#### `students` 表

这是问卷调查的主要结果表。每一列代表了问卷中的一个问题，除了第一列 `time`，它记录提交问卷的时间，也是每一行的唯一标识符。

| 列名         | 问题                                                         |
| ------------ | ------------------------------------------------------------ |
| `time`       | 记录提交时间的唯一时间戳，用于标识每一条提交记录             |
| `number`     | What's your favorite number between 1 and 100?（你最喜欢的 1 到 100 之间的数字是？） |
| `color`      | What is your favorite color?（你最喜欢的颜色是？）           |
| `seven`      | Choose the number 7 below.（选择下面的数字 7）               |
| `song`       | If you could listen to only one of these songs for the rest of your life, which would it be?（如果你此生只能听一首歌，你会选哪首？） |
| `date`       | Pick a day of the year!（选一年中的某一天）                  |
| `pet`        | If you could have any animal in the world as a pet, what would it be?（如果可以拥有任何一种动物做宠物，你会选什么？） |
| `instructor` | Choose your favorite photo of John DeNero（选择你最喜欢的 John DeNero 老师的照片） |
| `smallest`   | Try to guess the smallest unique positive INTEGER that anyone will put!（尝试猜出别人会填的最小唯一正整数！） |

------

#### `numbers` 表

这个表记录了学生在某个问题中选择的数字结果。该问题允许学生选择多个数字，选项从 `0` 到 `10`，另外还包括 `2018`、`9000` 和 `9001`。
 每一行有一个 `time` 字段（与 `students` 表中的时间相对应，是唯一标识符），然后每一列表示学生是否选择了对应的数字：

- 选中为 `'True'`
- 未选中为 `'False'`

表的列名包括：

```bash
'0', '1', '2', '4', '5', '6', '7', '8', '9', '10', '2018', '9000', '9001'
```

------

### 关键点

由于这次调查是匿名的，我们用提交表单的时间戳作为唯一标识符。
 `students` 表中的 `time` 和 `numbers` 表中的 `time` 是相对应的，代表同一个学生的提交。
 例如：

```lua
students 表中 time = "2019/08/06 4:19:18 PM CDT"
对应 numbers 表中 time = "2019/08/06 4:19:18 PM CDT"
```

------

### 数据清洗说明

如果你在数据里找自己的回答，可能会发现有些答案和你输入的不完全一致。
 为了让 SQLite 能接受这些数据，并且提高连接（join）操作时的匹配率，我们对数据做了以下清洗处理：

- `color` 和 `pet` 列的字符串全部转为小写。
- 某些 "自由发挥" 类型的答案，我们转义（escape）了特殊字符，以确保数据能被正确解析。

------

### 操作指南

你需要在提供的 `lab12.sql` 文件中编写所有 SQL 查询。
 和之前的实验一样，你可以通过 OK 工具测试你的代码。

额外的，你可以用以下命令运行你的 SQL 文件：

```bash
python3 sqlite_shell.py < lab12.sql
```

或者：

```bash
python3 sqlite_shell.py --init lab12.sql
```

------



# Questions

### Q1: What Would SQL print? ✅

注意：本题不需要提交。

首先，将表格加载到 `sqlite3` 中。

```bash
$ python3 sqlite_shell.py --init lab12.sql
```

在开始之前，先查看我们为你创建的表的结构。

```sql
sqlite> .schema
```

这个命令会显示所有表的名字以及它们的字段信息。

然后，我们可以查看一下表里的部分数据。由于数据量较大，我们先只看前 20 条记录：

```sql
sqlite> SELECT * FROM students LIMIT 20;
```

如果你对同学们在 Google 表单中填写的答案感兴趣，可以在你喜欢的文本编辑器中打开 `data.sql` 文件看看！

接下来是几个 SQL 查询练习。试着想一想每个查询想要找出什么样的信息，然后自己动手执行这些查询看看结果吧。

```sql
sqlite> SELECT * FROM students LIMIT 30; -- 这是一条注释。* 表示选择所有列！

sqlite> SELECT color FROM students WHERE number = 7;

sqlite> SELECT song, pet FROM students WHERE color = "blue" AND date = "12-25";
```

记得每条 SQL 语句要以分号（`;`）结尾！
 退出 SQLite 有几种方式：输入 `.exit`、`.quit`，或者直接按下 `Ctrl-C`。



### Q2: Go Bears! (And Dogs?) ✅

现在我们已经学会了如何从 SQL 表中选择列，接下来让我们通过筛选结果来发现一些更有趣的信息！

事实证明，61A 的同学们拥有强烈的校友精神：最受欢迎的颜色是 'blue'（蓝色）。你可能会以为这种精神会延续到宠物的选择上，大家都会想要一只 'bear'（熊）作为宠物！然而，事实并非如此，大多数同学选择了更为理智的宠物——'dog'（狗）。我想，这确实是个更明智的选择……

现在，请你写一条 SQL 查询语句，创建一个包含 color 和 pet 两列的表。使用 `WHERE` 关键词来筛选结果，使得 color 为 'blue' 且 pet 为 'dog'。
 最终，你应该能看到如下的输出：

```python-repl
sqlite> SELECT * FROM bluedog;
blue|dog
blue|dog
blue|dog
...
```

表结构的创建语句如下：

```sql
CREATE TABLE bluedog AS
  SELECT "在这里填写你的解决方案";
```

这个表看起来并不是很有趣。虽然每一行代表一位不同的学生，但这个表只展示了有多少同学既喜欢蓝色又想要狗作为宠物，因为我们并没有选择其他能区分每个学生的特征。

所以，我们来创建另一个表 `bluedog_songs`，它和 `bluedog` 很像，不过它还会展示这些学生在歌曲问题上的回答。

你应该能看到如下的输出：

```sql
sqlite> SELECT * FROM bluedog_songs;
blue|dog|Smells like Teen Spirit
blue|dog|The Middle
blue|dog|Clair De Lune
...
```

创建表的 SQL 语句如下：

```sql
CREATE TABLE bluedog_songs AS
  SELECT "在这里填写你的解决方案";
```

从这些歌曲的分布来看，大致反映了所有学生在歌曲选择上的总体分布。也就是说，也许我们并没有发现学生的喜欢颜色、想要的宠物，以及他们愿意听一辈子的歌曲之间有任何关联。不过，即使是展示“没有关联”，也能从数据中得出有意义的结论！

完成之后，使用 Ok 来测试你的代码：

```bash
python3 ok -q bluedog
```



### Q3: The Smallest Unique Positive Integer ✅

谁成功猜中了最小的唯一正整数呢？让我们来查一查！

虽然我们可以通过聚合函数（aggregation）来找出最小的唯一整数，但目前我们先尝试通过人工观察数据来完成任务。一位匿名的小精灵告诉我们，这个最小的唯一正整数比 2 大。

现在你需要编写一条 SQL 查询语句，创建一个包含 `time` 和 `smallest` 两列的表格，方便我们观察和判断哪个数值是最小的唯一整数。为了让我们更方便地检查这些值，你需要使用 `WHERE` 子句筛选出大于 2 的数值，用 `ORDER BY` 对这些数值进行升序排序，再使用 `LIMIT` 限制只显示前 20 条记录。

**提示**
 不幸的是，最小的唯一正整数并不在前 20 个大于 2 的值当中。不过，出于好奇，你可以尝试不同的 SQL 查询（比如筛选大于 10 的值），看看是否能发现最小的唯一整数！

基本语法示例（供参考）：

```sql
CREATE TABLE smallest_int AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

完成后，你可以通过 Ok 来测试代码是否正确：

```bash
python3 ok -q smallest-int
```

当你通过 Ok 测试后，查看你刚创建的 `smallest_int` 表，并手动找出最小的唯一正整数值！

答案：20

在终端中执行以下操作：

```bash
$ python3 sqlite_shell.py --init lab12.sql
sqlite> SELECT * FROM smallest_int;  -- 这次不加 LIMIT！
```

这样你就能看到所有符合条件的记录了，接下来动动手，看看谁给出的数字是最小的唯一值！

### Q4: Matchmaker, Matchmaker ✅

你是因为希望在 61A 找到隔离期间的浪漫邂逅才选的课吗？好消息！现在有了这份数据，我们可以帮你找到完美的灵魂伴侣啦！只要两位学生想要养同样的宠物，并且有相同的音乐品味，那他们肯定天生一对！当然，为了给未来的情侣们提供更多话题，我们还要展示两位同学各自最喜欢的颜色。

### 你的任务

为了把学生们配对，你需要对 `students` 表进行自连接（join 它自己）。当你进行 join 操作时，SQLite 会将每一行和其他所有行都匹配一次。所以你必须确保：

1. 不要把某人和自己匹配（避免自己和自己成为情侣😅）。
2. 不要重复配对（比如 A 和 B、B 和 A 是同一个组合，只需要一个就行）。

⚠️ **重点提醒**
 匹配第一人和第二人时，请确保第一个人填写的时间在前（也就是说，`time` 更早）。这样你输出的结果才能和我们的测试用例一致。

------

### 小提示

当你 join 两张表时，表里字段名是一样的，容易混淆。所以你要用「点号（dot notation）」区分来自不同表的列，格式是：

```css
[表名].[列名]
```

但这样写太啰嗦了，为了简洁，通常给表取别名（alias）。用 `AS` 关键字就可以做到，比如这样：

```sql
SELECT a.color, b.color
  FROM students AS a, students AS b
```

上面例子里，`a` 代表第一张表，`b` 代表第二张表。

------

### 你要写的查询

创建一个名叫 `matchmaker` 的表，包含四列数据：

1. 两个人共同想要的宠物（`pet`）
2. 两个人共同喜欢的歌曲（`song`）
3. 第一个人的喜欢的颜色（`color`）
4. 第二个人的喜欢的颜色（`color`）

表的结构就像这样👇

```markdown
pet       | song                     | color1 | color2
-----------------------------------------------------
dog       | Smells Like Teen Spirit  | blue   | red
cat       | Clair de Lune            | green  | purple
```

------

### 查询语句模板（别忘了填充正确条件！）

```sql
CREATE TABLE matchmaker AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

✅ 上面解释一下：

- `a.pet = b.pet`：两人都想养同样的宠物
- `a.song = b.song`：两人喜欢听同一首歌
- `a.time < b.time`：第一个人填写表单的时间更早，避免配对重复 & 自己和自己配对

------

### 测试代码是否正确

完成后，运行 OK 来检查：

```bash
python3 ok -q matchmaker
```



### Q5: Sevens ✅

让我们同时查看 `students` 和 `numbers` 这两张表的数据，来研究一下那些「真的很喜欢数字 7」的同学。他们是否也在「选择数字 7」的问题（`students` 表中的 `seven` 列）中选择了「7」呢？

### 条件

我们只关注满足以下两个条件的学生：

1. 他们在 `students` 表里表示自己最喜欢的数字（`number` 列）是 **7**。
2. 他们在 `numbers` 表中勾选了 `7`（即 `numbers` 表中的 `7` 列是 `True`）。

------

### 如何做到这一点？

要在两张表之间关联信息，我们需要进行 `JOIN` 操作。
 但是要特别注意：
 **必须**在 `WHERE` 子句中确保 `students` 和 `numbers` 表中的记录是对应的同一个学生！
 怎么做？
 通过两张表的 `time` 列关联，因为 `time` 是每份提交的唯一标识。

------

### 重点提醒

在 `numbers` 表中，列名是数字字符串（例如 `7`、`9001`），所以查询时必须加上引号。
 比如如果你给 `numbers` 表取了别名 `n`，要引用 `7` 列时应该写成：

```sql
n.'7'
```

------

### 你的目标

写一个 SQL 查询，创建一个名叫 `sevens` 的表，只包含 `students` 表中的 `seven` 列。
 但前提是满足以下两个筛选条件：

- `students.number = 7`
- `numbers.'7' = 'True'`

------

### 查询语句模板

```sql
CREATE TABLE sevens AS
	SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

------

### 测试你的查询

完成后，可以使用 `ok` 测试：

```bash
python3 ok -q sevens
```