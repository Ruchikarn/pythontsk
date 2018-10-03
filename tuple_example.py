# def my_sum(*args):
#     total = 0
#     for no in args:
#         total += no
#     return total
#
#
# print(my_sum(4, 5, 6, 7))
#
#
# def another_func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# another_func(1, 2, 3, 'ram', name='hari', roll_no=45)
# another_func()

A = [3, 4, 5, 6]
B = A

C = [3, 4, 5, 6]

print(B == C)
print(A == C)
print(A is B)
print(A is C)

