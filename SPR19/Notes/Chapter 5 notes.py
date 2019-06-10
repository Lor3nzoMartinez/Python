
# Problem 5_1


# def is_20_div_by_2_3(x):
#     if x % 2 == 0 and x % 3 == 0:
#         return f"{x} is divisible by 2 and 3."
#     elif x % 2 == 0 or x % 3 == 0:
#         return f'{x} is divisible by 2 or 3'
#     else:
#         return f'{x} is not divisible by 2 or 3.'
#
#
# print(is_20_div_by_2_3(122))


# Problem 5_2


# Problem 5_3


# def negative_or_positive(num):
#     if num < 0:
#         status = 'negative'
#     elif num > 0:
#         status = 'positive'
#     else:
#         status = 'zero'
#     return status
#
#
# for num in range(-2,3):
#     print(negative_or_positive(num))

# Problem 5_4


# def factor_of_7(num):
#     if num % 7 == 0 and num % 5 == 1 and num % 3 == 1:
#         num = 'factor'
#     return num
#
#
# for i in range(2, 250):
#     ans = factor_of_7(i)
#     if ans == 'factor':
#         print(i, ans)

# Problem 5_5


# def tell_if_d3_and_not_d5(num):
#     if num % 3 == 0 and num % 5 != 0:
#         num = 'factor'
#     return num
#
#
# for i in range(2,20):
#     ans = tell_if_d3_and_not_d5(i)
#     if ans == 'factor':
#         print(i, ans)


# Problem 5_6


# Problem 5_7
#
# def sumSqrs_diffSqrs(x, y):
#     sumSqr = x**2 + y**2
#     diffSqr = x**2 - y**2
#     return sumSqr, diffSqr
#
#
# A, B = sumSqrs_diffSqrs(4, 2)
#
# print(f'4^2 + 2^2 is {A} and 4^2 - 2^2 is {B}')

# Problem 5_8

# sepMe = ['dog', 3, 7,2,'cat','5']
#
# def sepper(list):
#     ints = []
#     strs = []
#     for i in range(len(list) - 1):
#         if type(list[i]) == int:
#             ints.append(list[i])
#         elif type(list[i]) == str:
#             strs.append(list[i])
#     return ints, strs
#
#
#
# print(sepper(sepMe))













