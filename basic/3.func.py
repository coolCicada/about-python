def add(a, b):
    return a + b

print(add(1, 2))

def add_no_swap(a, b):
    # print(id(a), id(b))
    # a += b
    b, a = a, b
    # c = a
    # a = b
    # b = c
    # print(id(a), id(b))
    return a, b

# a = 1
# b = 2
# add_no_swap(a, b)
# print(a, b)

lst1 = [1, 2]; lst2 = [3, 4]
print(lst1, lst2)
print(id(lst1), id(lst2))
add_no_swap(lst1, lst2)
print(id(lst1), id(lst2))
print(lst1, lst2)


# 默认参数
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to


print(append_to(1))
print(append_to(2))