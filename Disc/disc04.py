# 1.1
def count_stair_ways(n):
  if n < 0:
    return 0
  if n == 0:
    return 1
  else:
    return count_stair_ways(n-1) + count_stair_ways(n-2)

# 1.2 利用迭代, 多次递归
def count_k(n, k):
  if n < 0:
    return 0
  if n == 0:
    return 1
  else:
    sum = 0
    i = 1
    while i <= k:
      sum += count_k(n - i, k)
      i += 1
    return sum

# 2.1
# 1
# 3
# 5
# False
# True
# 2

# 2.2 关键是迭代 i, 而非迭代 s
def even_weighted(s):
  return [i * s[i] for i in range(len(s)) if i % 2 == 0]

def even_weighted(s):
  result = []
  for i in range(len(s)):
    if i % 2 == 0:
      result = result + [s[i] * i]
  return result


# 2.3 自己没想出来
def max_product(s):
  # 递归边界
  if s == []:
    return 0
  elif len(s) == 1:
    return s[0]
  # 树递归, 选择或不选择第一个元素
  else:
    return max(max_product(s[1:]), s[0] * max_product(s[2:]))