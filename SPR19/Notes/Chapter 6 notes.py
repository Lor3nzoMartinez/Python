import math

# Problem 6_0


# def circle_area(Radius):
#     ans = math.pi * Radius **2
#     return ans
#
# print(circle_area(12))

# Problem 6_1


# def avg_2_nums(x, y):
#     ans = x + y
#     ans = ans/2
#     return ans
#
# print(avg_2_nums(2,4))

# Problem 6_2


# def distance(x1, y1, x2, y2):
#     D1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     return D1
#
#
# def area_o_triangle(x1, y1, x2, y2, x3, y3):
#     D1 = distance(x1, y1, x2, y2)
#     D2 = distance(x2, y2, x3, y3)
#     D3 = distance(x3, y3, x1, y1)
#     s = (D1 + D2 + D3)/2
#     A = math.sqrt(s * (s - D1) * (s - D2) * (s - D3))
#     return A
#
#
# print(area_o_triangle(72, 98, 15, 32, 91, -7))


# Problem 6_3

#
# def quadratic(a, b, c):
#     f = ax^2 + bx + c
    # ans = -c
    # ans = ans / b
    # ans = ans / a


# Problem 6_4

# def isEven(n):
#     if n % 2 == 0:
#         return 'Even'
#
#
# def isOdd(n):
#     if n % 2 != 0:
#         return 'Odd'
#     else:
#         return isEven(n)
#
#
# for i in range(1, 21):
#     print(f'{i} is {isOdd(i)}')


# Problem 6_5


# def fact_fact(n):
#     prodAcum = -1
#     if n > 0:
#         return 1
#     else:
#         for i in range(-2, n-1, -2):
#             prodAcum *= i
#         return prodAcum
#
#
# for i in range(-8, -1):
#     print(f'{i} {fact_fact(i)}')


# Problem 6_6


# def func(n):
#     if n == 4 or n == 3:
#         return n - 2
#     else:
#         return n + 2
#
# for i in range(1,7):
#     print(f'{i} = {func(i)}')


# Problem 6_7

def isFactor(f, n):
    if f % n == 0:
        return True
    else:
        return False
#
# for i in range(1,61):
#     print(i, isFactor(60, i))


# Problem 6_8


def listOfFactors(n):
    factors = []
    if n > 2:
        for i in range(2, n+1):
            if isFactor(n, i) == True:
                factors.append(i)
    return factors


# for i in range(1, 21):
#     print(listOfFactors(i))


# Problem 6_9


def isPrime(n):
    if len(listOfFactors(n)) < 2 and n > 2:
        return f'{n} is Prime'

for i in range (1,21):
    print(isPrime(i))







