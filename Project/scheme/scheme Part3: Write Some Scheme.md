你的 Scheme 解释器本身是一个树递归程序，但它也足够灵活，可以用来执行其他递归程序。在 `questions.scm` 文件中，实现以下 Scheme 过程。

此外，在完成本项目这一部分时，如果你对某个内建 Scheme 过程（比如 `pair?` 和 `list?` 的区别）有疑问，可以参考内建过程文档（built-in procedure reference），这会非常有帮助。

解释器的自动评分测试（autograder）并不全面，因此，你的实现中可能存在尚未发现的 Bug。建议在你编写 Scheme 代码时，先在 **工作人员提供的解释器** 或 **网页版编辑器** 中测试，确认工作正常后，再在你自己实现的解释器中测试。

------

### Scheme 编辑器

在编写代码时，你可以使用 **Scheme 编辑器** 来调试。你的 `scheme` 文件夹里有一个新的编辑器。
 运行编辑器的方法是：

```bash
python3 editor
```

运行后，会在浏览器中弹出一个窗口。如果没有自动弹出，请在浏览器中手动访问 `localhost:31415`，你应该可以看到编辑器界面。

⚠️ 注意：
 记得在 **单独的终端标签页或窗口** 中运行

```bash
python3 ok
```

这样编辑器才能持续保持运行状态。



### Problem 15 (2 pt) ❎ 想不出如何实现 0 1 2 3，可以用函数嵌套调用传递参数

实现 `enumerate` 过程。该过程接受一个值的列表作为输入，返回一个由二元列表组成的列表。每个二元列表的第一个元素是该值的索引，第二个元素是该值本身。

示例：

```scss
scm> (enumerate '(3 4 5 6))
((0 3) (1 4) (2 5) (3 6))

scm> (enumerate '())
()
```



### Problem 16 (2 pt) ❎ 漏掉了 if 为 False 情况，分支控制情况

实现 `merge` 过程。该过程接受一个比较器（comparator）和两个已排序的列表作为输入，并将它们合并为一个有序列表。比较器是一个用于比较两个值的函数。这里的“已排序”是指按照比较器的顺序进行排序。

例如：

```shell
scm> (merge < '(1 4 6) '(2 5 8))
(1 2 4 5 6 8)

scm> (merge > '(6 4 1) '(8 5 2))
(8 6 5 4 2 1)
```

当遇到相等的值时，你可以任选一种方式处理（打破平局的方式可以任意）。



### 错误处：**没有统一的 if-else 分支结构**。

Scheme 不会像 Python 那样顺序执行 `if`，
 你只是在分别写表达式，没有 return，

最终 `merge` 会返回什么取决于“最后一个 `if`”。



### Problem 17 (2 pt) ❎ ❎ 比较难理解顺序情况的递归构造

定义一个函数 `nondecreaselist`，它接收一个 Scheme 数字列表作为输入，并输出一个列表，列表中的每个子列表都是非递减（non-decreasing）序列。

比如，输入是如下元素的列表：

```scss
(1 2 3 4 1 2 3 4 1 1 1 2 1 1 0 4 3 2 1)
```

那么输出应该是按顺序分组后的多个非递减子列表：

```scss
((1 2 3 4) (1 2 3 4) (1 1 1 2) (1 1) (0 4) (3) (2) (1))
```



### Extra Credit (2 pt) ❎ 太麻烦直接放弃看答案顺思路

我们可以编写操作其他程序的过程，就像我们编写操作列表的过程一样。

重写程序非常有用：我们可以编写一个只处理语言核心部分的解释器，然后再写一个过程，把其他特殊形式转换为核心语言，在程序传递给解释器之前完成转换。

例如，`let` 特殊形式就等价于一个以 `lambda` 表达式开头的调用表达式。两者都会创建一个新的环境框架（frame），扩展当前环境，然后在新的环境中求值表达式体（body）。

来看这个例子：

```scheme
(let ((a 1) (b 2)) (+ a b))
```

等价于：

```scheme
((lambda (a b) (+ a b)) 1 2)
```

这两个表达式可以用下图来表示（这里是提示你在教材或网页中会有图表说明它们的结构差异）：

![image-20250320223645276](/Users/ashing/Study/2语言框架/0SICP(CS61A)/Project/scheme/Pic/scheme Part3: Write Some Scheme.Pic/image-20250320223645276.png)

使用这个规则实现一个过程，叫做 `let-to-lambda`，它将所有的 `let` 特殊形式重写为 `lambda` 表达式。如果我们对一个 `let` 表达式加上 `quote` 并传入这个过程，它应该返回一个等价的 `lambda` 表达式：

```scheme
scm> (let-to-lambda '(let ((a 1) (b 2)) (+ a b)))
((lambda (a b) (+ a b)) 1 2)

scm> (let-to-lambda '(let ((a 1)) (let ((b a)) b)))
((lambda (a) ((lambda (b) b) a)) 1)
```

为了处理所有程序，`let-to-lambda` 必须理解 Scheme 的语法。由于 Scheme 表达式是递归嵌套的，`let-to-lambda` 也必须是递归的。事实上，`let-to-lambda` 的结构有点类似于 `scheme_eval` —— 但它是用 Scheme 写的！
 作为提示，原子（atoms）包括数字、布尔值、nil 和符号。你不需要考虑包含 quasiquotation（准引用）的代码。

```scheme
(define (let-to-lambda expr)
  (cond ((atom?   expr) <重写原子>)
        ((quoted? expr) <重写引用表达式>)
        ((lambda? expr) <重写 lambda 表达式>)
        ((define? expr) <重写 define 表达式>)
        ((let?    expr) <重写 let 表达式>)
        (else           <重写其他表达式>)))
```

提示：你可能需要在 `questions.scm` 顶部实现 `zip`，同时也可以使用内置的 `map` 过程。

```scheme
scm> (zip '((1 2) (3 4) (5 6)))
((1 3 5) (2 4 6))

scm> (zip '((1 2)))
((1) (2))

scm> (zip '())
(() ())
```

测试你的实现：

```css
python3 ok -q EC
```

注意：我们在定义 `let-to-lambda` 时用到了 `let`。
 如果我们想在一个不支持 `let` 的解释器里运行 `let-to-lambda` 呢？
 可以将 `let-to-lambda` 传给它自己，重写为不含 `let` 的等价程序：

```scheme
;; let-to-lambda 过程
(define (let-to-lambda expr)
  ...)

;; 一个表示 let-to-lambda 的表达式
(define let-to-lambda-code
  '(define (let-to-lambda expr)
     ...))

;; 一个不使用 'let' 的 let-to-lambda！
(define let-to-lambda-without-let
  (let-to-lambda let-to-lambda-code))
```



