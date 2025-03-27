## 1 Object Oriented Programming

- **类（class）**：用于创建对象的模板。
- **实例（instance）**：从类创建的单个对象。
- **实例属性（instance attribute）**：对象的属性，特定于某个实例。
- **类属性（class attribute）**：对象的属性，由类的所有实例共享。
- **方法（method）**：类的所有实例都可以执行的操作（函数）。



### Questions

### 1.1

下面我们定义了 Professor 和 Student 类，实现了上面描述的一些内容。请记住，在使用点表示法时，我们将 self 参数隐式传递给实例方法。下一页还有更多问题。

```python
>>> callahan = Professor("Callahan")
>>> elle = Student("Elle", callahan)
name = "Elle"
statff = callahan

"There are now 1 students"

>>> elle.visit_office_hours(callahan)
callahan, student.understanding = 1
"Thanks Callahan"

>>> elle.visit_office_hours(Professor("Paulette"))
Paulette, student.understanding = 2
"Thanks Paulette"

>>> elle.understanding
2

>>> [name for name in callahan.students]
[{"Elle": elle}] ❎，没有{}
["Elle": elle]

>>> x = Student("Vivian", Professor("Stromwell")).name
"There are now 2 students"

>>> x
"Vivian"

>>> [name for name in callahan.students]
[{"Elle": elle}] ❎，没有{}
["Elle": elle]
```



### 1.2

实现特殊 list，MinList

可以 append 和 pop，但只能 pop 最小的值

class MinList 包含一下几个方法

- 1，append(self, item)，追加元素
- 2，pop(self)，移除并返回最小元素

每个实例包含 size 属性，表示有多少元素，append 和 pop 后，更新 size

提示：实际上，将 Python 列表作为每个 MinList 的实例属性包含在内可能会有所帮助，以跟踪我们拥有的项目。



```python

```



### 1.3

我们现在要编写三个不同的类——`Server`（服务器）、`Client`（客户端）和 `Email`（电子邮件），以模拟电子邮件的发送和接收。请完成以下定义，完成整个实现！在下一页还有更多方法需要填写。

我们建议按照以下步骤完成此问题：

1. **首先完成 `Email` 类**，确保它可以正确存储和表示邮件信息。
2. **然后实现 `Server` 类中的 `register_client` 方法**，以便客户端可以注册到服务器。
3. **接着实现 `Client` 类**，让客户端能够通过服务器发送和接收邮件。
4. **最后完成 `Server` 类中的 `send` 方法**，使服务器能够处理邮件的传输。



## 2 Inheritance

抽离相似类的相同代码，抽象为单独类，减少代码重复量



### Questions

### 2.1

### 2.2

教程：更多的猫！填写一个名为 NoisyCat 的类的实现，它就像一个普通的 Cat。然而，NoisyCat 说话很多——是普通猫的两倍！确保同时填写 NoisyCat 的 repr 方法，这样我们就知道如何构建它了！提示：您可以使用多种字符串格式化方法来简化此作。

