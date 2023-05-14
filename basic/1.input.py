# 读入
"""
4
1 3 3 
1 4 1 
2 3 4 
3 4 1 
"""
# N = int(input())
# mat = [[int(x) for x in input().split()] for i in range(N)]
# print(mat)
# u, v, w = map(list, zip(*mat))
# print(u, v, w)

# u, v, w = [], [], []
# s = input()
# while s:
#     u[len(u):], v[len(v):], w[len(w):] = [[int(x)] for x in s.split()]
#     s = input()

# print(u, v, w)
lst = []
while s:= input():
    a = [int(x) for x in s.split()]
    lst.append(a)
print(lst)
