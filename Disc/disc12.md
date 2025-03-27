## 1 Introduction

## 2 Creating Tables

### Questions ✅

2.1 编写一个查询，输出由 Oliver Warbucks 直接监督的员工的姓名。

```sql
select name from records where supervisor = "Oliver Warbucks";
```



2.2 编写一个查询，输出所有监督自己工作的员工的全部信息。

```sql
selct * from records where supervisor = name;
```



2.3 编写一个查询，按字母顺序输出所有薪资高于 50,000 的员工姓名。

```sql
select name from records where salary > 50000 order by name asc;
```



## 3 Joins

3.1 编写一个查询，输出由 Oliver Warbucks 直接监督的所有员工的会议日期和时间。✅

```sql
select m.day, m.time from records r, meetings m where r.division = m.division and r.supervisor = "Oliver Warbucks";
```



3.2 编写一个查询，输出所有在相同时间开会的员工对的姓名。确保如果 A|B 出现在输出中，B|A 不应再次出现（同时 A|A 和 B|B 也不应该出现）。 ❎ ✅自己又想出来了

```sql
select a.name, b.name from records a, records b, meetings m1, meetings m2 where a.division = m1.divrsion and b.division = m2.divrsion and m1.day = m2.dat and m1.time = m2.time and a.name < b.name;
```



3.3（附加问题）上述语句是否能在所有情况下过滤掉所有冗余输出？为什么或为什么不能？❎

能❎

不能。若一个部门有多个会议？那么该部门内所有员工的配对将会被列出多次。为了避免这种情况，我们可以使用 DISTINCT 关键字。



3.4 编写一个查询，输出那些其主管所在部门与自己不同的员工姓名。✅

```sql
select a.name from records a, records b where a.supervisor = b.name and a.division <> b.division;
```



## 4 Aggregation ⭐️ 有点难度了

MAX, MIN, COUNT, and SUM functions

GROUP BY

In contrast to the WHERE clause, which ﬁlters out rows, the HAVING clause ﬁlters out entire groups.



4.1 编写一个查询，输出每位主管的姓名，以及他们所管理的所有员工的工资总和。❎

```sql
select r2.name, sum(r1.salary) from records r1, records r2  where r1.supervisor = r2.name and group by r2.name; 

select supervisor, sum(salary) form records gourp by supervisor;
```



4.2 编写一个查询，输出每周中员工开会人数少于 5 人的那些天。你可以假设没有任何部门在同一天安排超过一次会议。⭐️

```sql
select m.day from meetings m, records r where m.division = r.division group by m.day having count(r.name) < 5; ❎能否 count(字段)?

select m.day from meetings m, records r where m.division = r.division group by m.day having count(*) < 5; ✅
```



4.3 编写一个查询，输出所有拥有超过一名员工的部门，以及该部门内所有员工对（组合），要求这两名员工的工资之和小于 100,000。⭐️

```sql
select division, r1.name, r2.name  from records r1, records r2 where r1.division = r2.division group by division having sum(r1.salary, r2.salary) < 100000; ❎ sum 用法应该不对，r1.name != r2.name 没考虑到

select r1.division from records r1, records r2 where r1.name != r2.name and r1.division = r2.division group by r1.division having max(r1.salary + r2.salary) < 100000;
```



## 5 Tutorial

15 rows ✅

5.1 创建一个名为 `num_taught` 的表，该表包含三列：教授（professor）、他们教授的课程（course），以及他们每门课教授的次数（number of times they taught each course）。

提示：在这个问题中，使用 `GROUP BY` 多列会有帮助。**`GROUP BY` 子句中可以包含多个列和完整表达式，系统会针对每一种唯一的值组合分组。**

```sql
create table num_taught as
	select professor, course, count(*) as numbers from courses group by course, semester; ❎

create table num_taught as
	select professor, course, count(*) as numbers from courses group by professor, course;
```

数据库会寻找每一个 **教授 + 课程** 的唯一组合，把 `courses` 里所有相同 `professor` 和 `course` 的记录聚合到一起，然后对这些记录执行 `count(*)`，就得到了 **每个教授教每门课的次数**。

按 `professor` 和 `course` 的组合来分组。

每一组里是某个教授教某门课的所有记录（比如不同学期）。

`count(*)` 就是这个教授一共教了这门课多少次。

`GROUP BY` 后面可以写多个列，数据库就会按“这些列组合唯一值”进行分组。



------

5.2 编写一个查询，输出两位教授以及某门课程，如果他们教授该课程的次数相同。你可以使用前一个问题中创建的 `num_taught` 表。

```sql
select n1.professor, n2.professor, course from num_taught n1, num_taught n2 where n1.course = n2.cours and n1.numbers = n2.numbers; ❎ 忘记去重

select n1.professor, n2.professor, course from num_taught n1, num_taught n2 where n1.course = n2.cours and n1.numbers = n2.numbers and n1.professor > n2.professor;  
```



------

5.3 编写一个查询，输出两位教授，如果他们曾共同教授（在相同时间教授相同课程）该课程超过一次。 ❓

```sql
select n1.professor, n2.professor from num_taught n1, num_taught n2 where n1.course = n2.course group by numbers having numbers > 1; ❎


select a.professor, b.professor from courses a, courses b where a.professor < b.professor and a.semester = b.semester and a.course = b.course group by a.course, a.professor, b.professor having count(*) > 1;
```

对同一个表 `courses` 做了 **自连接**，意味着把课程记录和自己比对，寻找满足条件的成对教授。

 a.professor < b.professor：只选取有顺序的教授组合，避免重复（比如张老师 & 李老师和李老师 & 张老师不需要各来一次）。



### `group by a.professor, b.professor`

- 把所有 **共同授课的记录** 分组，按教授对来统计。
- 比如张老师和李老师可能一起教过多门课，或者在多个学期一起教同一门课。

### `having count(*) > 1`

- 统计“他们共同教授课程”的次数，如果超过一次，就输出。





## 理解 **`GROUP BY` **

`GROUP BY` 子句中可以包含多个列和完整表达式，系统会针对每一种唯一的值组合分组。

### 作用

`GROUP BY` 是用来**把数据按某些条件分类、分组**，然后**每组执行聚合操作**（比如 `COUNT`、`SUM`、`AVG` 等）。

> 通俗点说，就是你告诉 SQL：“按照某个列（或列组合）的值来‘分堆’数据”。
>  每一堆数据内部就可以做统计计算。

假设你有个 `courses` 表👇：

| professor | course | semester |
| --------- | ------ | -------- |
| 张老师    | 数学   | 2023春   |
| 李老师    | 语文   | 2023春   |
| 张老师    | 数学   | 2023秋   |
| 张老师    | 物理   | 2023秋   |
| 李老师    | 数学   | 2023秋   |
| 张老师    | 数学   | 2024春   |

------

## **1. 单列分组**

### 需求

统计每个教授教了多少次课。

### 写法

```
sql


复制编辑
SELECT professor, COUNT(*) as teach_times
FROM courses
GROUP BY professor;
```

### 理解

- `GROUP BY professor` 把所有数据，按 `professor` 分组。
- 类似于：
  - 张老师 组 👉 把所有张老师的课都丢进来
  - 李老师 组 👉 把所有李老师的课都丢进来
- 每组分别 `COUNT(*)`，数他们教了多少次课。

| professor | teach_times |
| --------- | ----------- |
| 张老师    | 4           |
| 李老师    | 2           |

------

## **2. 多列分组**

### 需求

统计每个教授每门课分别教了多少次。

### 写法

```
sql


复制编辑
SELECT professor, course, COUNT(*) as teach_times
FROM courses
GROUP BY professor, course;
```

### 理解

- `GROUP BY professor, course` 👉 以“教授 + 课程”做一个组合来分组。
- 分组的逻辑就是：
  - 张老师 + 数学 👉 是一组
  - 张老师 + 物理 👉 是一组
  - 李老师 + 语文 👉 是一组
  - 李老师 + 数学 👉 是一组

### 最终结果👇

| professor | course | teach_times |
| --------- | ------ | ----------- |
| 张老师    | 数学   | 3           |
| 张老师    | 物理   | 1           |
| 李老师    | 数学   | 1           |
| 李老师    | 语文   | 1           |

------

## **关键理解点**

1. **你放在 `GROUP BY` 里的列，决定了怎么分类。**
2. 分组后，系统会把“相同组”的行“堆”在一起，每组都会单独执行聚合函数（`COUNT`、`SUM`等）。
3. `GROUP BY` 可以有一个列、两个列、甚至多个列，**组合起来作为分组的依据**。

## **举个生活中的例子**

想象一下👇

- 你在学校组织篮球赛，班级是分组依据。
- 你按 **班级** 分组，每组是不同班级的同学。
- 如果你按 **年级+班级** 分组，那就更细了。

| 年级 | 班级 | 学生名字 |
| ---- | ---- | -------- |
| 高一 | 1班  | 张三     |
| 高一 | 1班  | 李四     |
| 高一 | 2班  | 王五     |
| 高二 | 1班  | 赵六     |

- `GROUP BY 班级` 👉 1班分到一组（高一1班+高二1班混到一起），2班分到一组。
- `GROUP BY 年级, 班级` 👉 每个班都分到独立的组，不会混。