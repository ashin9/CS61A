## 1 Calculator

解释器是一个理解其他程序的程序



表示 Scheme Lists：Pair 类，first，rest



## Questions

### 1.1

写出与以下 `Pair` 构造函数调用对应的计算器表达式（Calculator expression），并为每个输入绘制相应的盒子和指针图（box and pointer diagram）。



```shell
>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
(+ 1 2 3 4)
|'+'|->|1|->|2|->|3|->|4|->|nil|

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))
|'+'|->|1|
					->|*|->|2|->|3|->|nil|
					->|nil|
```

![image-20250321211253674](/Users/ashing/Study/2语言框架/0SICP(CS61A)/Disc/Pic/disc11.Pic/image-20250321211253674.png)



### 1.2 回答以下关于表示计算器表达式 `(+ (- 2 4) 6 8)` 的 `Pair` 实例的问题。

i. 写出返回一个表示该表达式的 `Pair` 的 Python 表达式，并画出对应的盒子和指针图。

```shell
Pair('+', Pair(Pair('-', Pair(2, Pair(4, nil)))), Pair(6, Pair(8, nil)))

|'+'|
		->|'-'|->|2|->|4|->|nil|
		->|6|->|8|->|nil|
```



ii. 该调用表达式的运算符（operator）是什么？如果你在上一个部分构建的 `Pair` 绑定到了名字 `p`，你如何获取这个运算符？

```shell
+
p.first
```





iii. 该调用表达式的操作数（operands）是什么？如果你在第 (i) 部分构建的 `Pair` 绑定到了名字 `p`，你如何获取包含所有操作数的列表？你如何仅获取第一个操作数？

```shell
(- 2 4) 6 8
p.rest
p.rest.first
```



## 2 Evaluation

evaluation rules for the three types

- Numbers
- Names
- Call expressions
  - operator
  - operands
  - apply

calc eval is recursive! In order to evaluate call expressions, we must call calc eval on the operator and each of the operands.



## Questions

### 2.1

假设我们希望为计算器解释器添加对比较运算符 `>`、`<` 和 `=` 以及 `and` 表达式的处理。这些操作应当和它们在 Scheme 中的表现相同。

```scss
calc> (and (= 1 1) 3)
3

calc> (and (+ 1 0) (< 1 0) (/ 1 0))
#f
```

------

i. 我们是否能够使用现有的 `calc_eval` 实现来处理包含比较运算符（比如 `<`、`>` 或 `=`）的表达式？为什么？

能，初始 `OPERATORS` 字典有操作符 `+`



ii. 我们是否能够使用现有的 `calc_eval` 实现来处理 `and` 表达式？为什么？

不能，初始 `OPERATORS` 字典没有操作符 `and`，特殊处理短路等规则



iii. 现在，完成下面的实现以处理 `and` 表达式。你可以假设条件运算符（例如 `<`、`>`、`=` 等）已经为你实现好了。

```python
def calc_eval(exp):
  if isinstance(exp, Pair):
    if exp.first == "and": # and expressions 
      return eval_and(exp.rest) 
    else: # Call expressions 
      return calc_apply(calc_eval(exp.first), list(exp.rest.map(calc_eval))) 
   elif exp in OPERATORS: # Names 
    return OPERATORS[exp] 
   else: # Numbers 
      return exp

def eval_and(operands):
  while operands:
    if not calc_eval(oprands.first):
      return False
    oprands = oprands.rest
  return True
```

