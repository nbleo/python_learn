# 1. 通过set方法进行去重

# a = [1, 2, 3, 1, 1, 1, 7, 9, 5]
# print(list(set(a)))

# 2. 通过fromkeys方法创建新的字典

# a = [1, 2, 3, 1, 1, 1, 7, 9, 5]
# b = {}

# fromkeys 创建一个新的字典，已a中的元素作为字典的键

# b = b.fromkeys(a)
# print(b)
# c = list(b.keys())
# print(c)

# 3. 逻辑判断

a = [1, 2, 3, 1, 1, 1, 7, 9, 5]
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)