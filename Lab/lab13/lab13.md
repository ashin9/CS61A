## Cyber Monday

### Q1: Price Check ✅

在你吃饱感恩节晚餐后，你意识到你还需要在假期为你所有的亲人购买礼物。不过，你也希望花尽可能少的钱（你不是小气，只是想找个好折扣！）。

让我们从调查可选项开始。使用 products 表，编写一个查询，创建一个名为 average_prices 的表，该表列出每个类别和该类别商品的平均价格（使用 MSRP 作为价格）。

你应该得到如下输出：

```sql
sqlite> SELECT category, ROUND(average_price) FROM average_prices;
computer|109.0
games|350.0
phone|90.0

CREATE TABLE average_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```



### Q2: The Price is Right ✅

现在，你想要找出每个商店在售产品中，哪个商店以最低价格销售每件商品。编写一个 SQL 查询，使用 `inventory` 表创建一个名为 `lowest_prices` 的表。这个表应列出商品名、以最低价格销售该商品的商店，以及该商店的售价。

你应该期望看到如下输出：

```sql
sqlite> SELECT * FROM lowest_prices;
Hallmart|GameStation|298.98
Targive|QBox|390.98
Targive|iBook|110.99
RestBuy|kBook|94.99
Hallmart|qPhone|85.99
Hallmart|rPhone|69.99
RestBuy|uPhone|89.99
RestBuy|wBook|114.29

CREATE TABLE lowest_prices AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```



### Q3: Bang for your Buck ✅

你想要列一份购物清单，选择每个类别中性价比最高的商品。例如，对于 "phone" 类别，uPhone 是最划算的选择，因为它的 MSRP 价格除以评分（ratings）后的值是所有手机中最低的。这意味着 uPhone 在每个评分点上的价格最低。注意，MSRP 价格最低的商品不一定是最划算的。

编写一个查询，创建一个名为 `shopping_list` 的表，列出你打算从每个类别中购买的商品。

在确定你要买的商品之后，再加上一列，显示哪个商店以最低价格销售该商品。

你应该期望如下输出：

```sql
sqlite> SELECT * FROM shopping_list;
GameStation|Hallmart
uPhone|RestBuy
wBook|RestBuy

CREATE TABLE shopping_list AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

提示：你应该使用前面问题中创建的 `lowest_prices` 表。

提示 2：一种方法是先创建一个中间表，然后再从该表中选择数据来创建 `shopping_list`。



### Q4: Driving the Cyber Highways ✅

使用 `stores` 表中的 Mb（兆比特）列，编写一个查询来计算获取你购物清单（shopping_list）中所有商品所需的总带宽。

```sql
CREATE TABLE total_bandwidth AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";
```

提示：你应该使用在上一个问题中创建的 `shopping_list` 表。