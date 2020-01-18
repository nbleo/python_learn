# def add(x, y):
#     return x + y
#
#
# print(add(1, 3))
#
#
# # lambda_add = lambda x, y: x + y
#
# print(lambda_add(1, 3))
#

#
# m = lambda x : x ** x
#
# print(m(1))
# print(m(2))
# print(m(3))
#
# n = lambda x : 1
# print(n("abc"))
# print(n(2))
#
# lambda_sum = lambda *args: sum(args)
#
# print(lambda_sum(1, 2, 3, 4, 5, 6))

lambda_m = lambda x : x if x < 10 else "-"

print(lambda_m(1))
print(lambda_m(5))
print(lambda_m(11))