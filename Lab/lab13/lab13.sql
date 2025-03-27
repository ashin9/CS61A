.read data.sql


CREATE TABLE average_prices AS
  SELECT category, AVG(MSRP) AS average_price 
  FROM products
  GROUP BY category
  ;


CREATE TABLE lowest_prices AS
  SELECT store, item, price
  FROM inventory
  GROUP BY item
  HAVING MIN(price)
  ;


CREATE TABLE shopping_list AS
  SELECT p.name, l.store
  FROM products p, lowest_prices l
  WHERE p.name = l.item
  GROUP BY p.category
  HAVING MIN(p.MSRP / p.rating)
  ;


CREATE TABLE total_bandwidth AS
  SELECT SUM(s.Mbs)
  FROM shopping_list sl, stores s
  WHERE sl.store = s.store
  ;

