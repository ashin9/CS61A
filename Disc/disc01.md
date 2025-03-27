## Control

If-elif-else，选择和跳过某部分

while，重复部分

### If

条件表达式（Condition Experssion） ，评估 True （True，非 0 整数）或 False（False，0，None，""，[] ）

- if / elif 的条件表达式为 True，下面才执行
- else 没有条件表达式为 True，执行 else 下面



### Boolean Operator

and

or

not

短路





### Questions

1.1 阿方索只有在低于 60 度或下雨时才会在外面穿夹克。 编写一个函数，该函数接受当前温度和一个布尔值，告诉它是否在下雨，如果 Alfonso 会穿夹克，则返回 True，否则返回 False。 首先，尝试使用 if 语句解决此问题。

```python
def wears_jacket_with_if(temp, raining):
  if temp < 60 or raining:
    return True
  else:
    return False
```

尝试使用单行编写此函数

```python
def wears_jacket_with_if(temp, raining):
  return temp < 60 or raining:
```





### while loops

只要 条件语句为 True，循环体不断执行

### Questions

1.2 说明值

死循环，因为 x 永远大于 0

1.3 若正整数为素数则返回 True，否则返回 False

```python
def is_prime(n):
  if n == 1:
    return False
  for i in range(n / 2):
    if n % i == 0:
      return False
  return True
```





## Environment Diagrams

追踪所有变量

### Assignment Statements

```python
---Global----
x | 4
y | 2
```

### def Statements

记录函数名字和绑定的函数对象

使用指针

```python
---Global---
double -> func <double>
triple -> func <triple>
hat -> func <double>
double -> func <triple>
```

### Call Expressions

调用表达式，对参数应用函数，创建新的 frame

```python
---Global---
double -> func double(x)
hmmm -> func double(x)

---double---
x | 3
return 6

---Global---
double -> func double(x)
hmmm -> func double(x)
wow | 6

---double---
x | 6
return 12
```



### 2.4

```python
---Global---
f -> func f(x)
g -> func g(x, y)
x | 3

---g(f,x)---
x | f
y | 3

---f(3)---
x | 3
return 3

---g(f,x)---
x | f
y | 3
return False

---Global---
f -> func f(x)
g -> func g(x, y)
x | False

---g(f,0)---
x | f
y | 0

---f(0)---
x | 0
return 0

---g(f,0)---
x | f
y | 0
return 0

---Global---
f -> func f(x)
g -> func g(x, y)
x | False
f | 0
```

