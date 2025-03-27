# 1.1
def memory(n):
  def f(g):
    nonlocal n
    n = g(n)
    return n
  return f

# 2.1
# s1 -> [1,2,3]
# s2 ->

# s1 is s2
# True

# s2.extend([5,6])
# s1 -> [1,2,3,5,6]
# s2 ->

# s1[4]
# 6

# s1.append([-1,0,1])
# s1 -> [1,2,3,5,6,[-1,0,1]]
# s2 ->

# s2[5]
# [-1,0,1]

# s3 = s2[:]
# s3 -> [1,2,3,5,6,[-1,0,1]]
# s3.insert(3, s2.pop(3))

# s2.pop(3) = 5
# s1 -> [1,2,3,6,[-1,0,1]]
# s2 ->

# s3 -> [1,2,3,5,5,6,[-1,0,1]]

# len(s1)
# 5

# s1[4] -> [-1,0,1]
# s3[6] ->
# True

# s3[s2[4][1]]
# s3[0]
# 1

# s1[:3] is s2[:3]
# s1[:3] -> [1,2,3,6]
# s2[:3] -> [1,2,3,6]
# False

# s1[:3] == s2[:3]
# True

# 2.2
def mystery(p, q):
  p[1].extend(q[:])
  q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)

# 2.3
def group_by(s, fn):
  grouped = {}
  for e in s:
    key = fn(e)
    # 如何判断 key 是否存在于 dict, 做题时自己没想到方法
    if key in grouped:
      grouped[key].append(e)
    else:
      grouped[key] = [e]
  return grouped


# 2.4
def add_this_many(x, el, s):
  # 注意：考虑死循环
  # for i in s:
  #   if i == x:
  #     s.append(el)
  
  # 注意：在尾部插入，而不是中间插入
  # i = 0
  # while i < len(s):
  #   if s[i] == x:
  #     s.append(el)
  #     i += 1
  #   i += 1
    
  # 
  n = 0
  for i in s:
    if i == x:
      n += 1
  
  for i in range(n):
    s.append(el)


# 3.1
# >>> s = [[1, 2]]
# >>> i = iter(s)
# >>> j = iter(next(i))
# >>> next(j)
# 1
# >>> s.append(3)

# >>> next(i)
# 3
# >>> next(j)
# 2
# >>> next(i)
# StopIteration


# 4.1
def filter(iterable, fn):
  for x in iterable:
    if fn(x):
      yield x


# 4.2
# 只有一个，而不是无限的
# def merge(a, b):
#   a = next(a)
#   b = next(b)
  
#   if a < b:
#     yield a
#   else:
#     yield b
    
def merge(a, b):
  a = next(a)
  b = next(b)
  
  while True:
    if a < b:
      yield a
      a = next(a)
    elif a > b:
      yield b
      b = next(b)
    else:
      yield a
      a, b = next(a), next(b)