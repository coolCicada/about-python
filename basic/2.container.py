# 元组
"""
tup = tuple([[1, 2], 3])
tup[0].append(3)
print(tup)
a, b = 0, "aaa"; print(id(a), id(b))
b, a = a, b; print(id(a), id(b))
"""

# 字典
cnter = { 'a': 1, 'b': 2 }
print(cnter['a'])
cnter['a'] += 1

try:
    cnter['d'] += 1
except KeyError:
    cnter['d'] = 1
  
print(cnter)