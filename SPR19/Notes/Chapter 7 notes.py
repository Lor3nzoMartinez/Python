import turtle, random


wn = turtle.Screen()
alex = turtle.Turtle()
tess = turtle.Turtle()


# Problem 7_0

# def num_ints(n):
#     mah_nums = []
#     for i in range(1, n+1):
#         if i % 7 == 0 and i % 5 != 0:
#             mah_nums.append(i)
#     return mah_nums
#
#
# print(num_ints(500))
#

# Problem 7_1

# def sum_of_odds(n):
#     sum_acum = 0
#     for i in range(1, n+1):
#         if i % 2 != 0:
#             sum_acum += i
#     return sum_acum
#
#
# print(f'\n{sum_of_odds(10)}')


# Problem 7_2


# def sum_from_odds(a, b):
#     sum_acum = 0
#     for i in range(a, b):
#         if i % 2 != 0:
#             sum_acum += i
#     return sum_acum
#
#
# print(sum_from_odds(2, 6))


# Problem 7_2a


# def while_sum():
#     sum_acum = 0
#     i = 0
#     while sum_acum < 1000:
#         i += 1
#         sum_acum += i**2
#     return sum_acum, i
#
#
# print(while_sum())


# Problem 7_2b


# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
#
# def sum_while_prime():
#     sum_acum = 0
#     i = 0
#     while sum_acum < 1000:
#         i += 1
#         if is_prime(i):
#             sum_acum += i
#     return sum_acum
#
#
# print(sum_while_prime())
#

# Problem 7_3

#
# def random_walk(t, n, Dz):
#     for i in range(n):
#         trn_angle = random.randint(1, 360)
#         t.lt(trn_angle)
#         t.fd(Dz)
#
#
# random_walk(alex, 20, 25)
#
# wn.mainloop()


# Problem 7_4

# tess.speed(0)
#
#
# def draw_circle(t, R):
#     t.pu()
#     t.lt(90)
#     t.bk(R)
#     t.rt(90)
#     t.pd()
#     t.circle(R)
#     t.pu()
#     t.lt(90)
#     t.fd(R)
#     t.rt(90)
#     t.pd()
#
#
# def stop_when_circle_xd(t, Dz, R):
#     draw_circle(t, R)
#     x, y = t.xcor(), t.ycor()
#     while x**2 + y**2 <= R**2:
#         trn_ngl = random.randint(0, 359)
#         t.lt(trn_ngl)
#         t.fd(Dz)
#         x, y = t.xcor(), t.ycor()
#
#
# stop_when_circle_xd(tess, 15, 100)


# Problem 7_4_a


# def ran_walk(t, Dz, n):
#     for i in range(n):
#         trn_ngl = random.randint(0, 359)
#         t.lt(trn_ngl)
#         t.fd(Dz)
#
#
# def rectangle(t, W, H):
#     t.pu()
#     t.setpos(-W/2, -H/2)
#     t.pd()
#     for i in range(2):
#         t.fd(W)
#         t.lt(90)
#         t.fd(H)
#         t.lt(90)
#     t.pu()
#     t.setpos(0, 0)
#     t.pd()
#
#
# def stop_when_rect_xd(t, Dz, W, H):
#     rectangle(t, W, H)
#     x,y = t.xcor(), t.ycor()
#     num_moves = 0
#     while -W/2 <= x <= W/2 and -H/2 <= y <= H/2:
#         trn_ngl = random.randint(0, 359)
#         t.lt(trn_ngl)
#         t.fd(Dz)
#         x, y = t.xcor(), t.ycor()
#         num_moves += 1
#     print('total distance travelled:', num_moves * Dz)
#
#
# stop_when_rect_xd(tess, 10, 200, 100)


# Problem 7_5 and 7_6

# def seq3n(n):
#     while n != 1:
#         print(n, end=', ')
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#     print(n, end='.\n')
#
#
# def collatz(n):
#     col = []
#     while n != 1:
#         col.append(n)
#         if n % 2 == 0:
#             n = n // 2
#         else:
#             n = 3 * n + 1
#     col.append(n)
#     return col
#
#
# col_all = []
#
# for n in range(1, 50):
#     col_all.append(collatz(n))
#
# print(col_all)


# Problem 7_7


# def num_digit(n):
#     count = 0
#     while n != 0:
#         count = count + 1
#         n = n // 10
#     return count
#
#
# def num_digits(n):
#     string = str(n)
#     return len(string)
#
#
# for n in [123, 12, 3, 1234729]:
#     print(n, 'has', num_digits(n), 'digits')


# Problem 7_8


# def guess_num():
#     secret = random.randint(1, 128)
#     score = 100
#     bad_guesses = []
#     while True:
#         Guess = int(input('What is the secret number?'))
#         if Guess > secret:
#             print('Too high')
#             bad_guesses.append(Guess)
#             score -=2
#         elif Guess < secret:
#             print('Too low')
#             bad_guesses.append(Guess)
#             score -= 2
#         else:
#             break
#
#     print('Your final score is', score)
#     print('The secret number you finally guessed is', secret)
#     print('The incorrect guesses you made:', bad_guesses)
#     if len(bad_guesses) == 0:
#         print('Congrats dude, you guessed it on the first try!!!')
#
#
# guess_num()


# Problem 7_9


# fruit = [
#     ("apples", 250, 1.25),
#     ("peaches", 100, 0.95),
#     ("bananas", 75, 0.20),
#     ("oranges", 125, 0.50)
# ]
#
#
# totalItems = 0
# for (name, number, cost) in fruit:
#     totalItems += number
# print('The total pieces of fruit:', totalItems)
# print()
#
# totalValue = 0
#
#
# for(name, number, costs) in fruit:
#     totalValue += number * cost
# print('The total value of fruit:', totalValue)
# print()
#
#
# avg_cost = totalValue/totalItems
# print('The average cost of a piece of fruit:', avg_cost)
#
#
# Number_of_exp = 0
# for (name, number, cost) in fruit:
#     if cost > avg_cost:
#         Number_of_exp += number
#
#
# print(
#     'number of pieces of fruit that have a greater than avg cost is:',
#     Number_of_exp
# )
#

# Problem 7_11
# from math import pi
#
#
# def leibniz_sum(n):
#     sum_acum = 0
#     for i in range(n):
#         sum_acum += (-1)**i * 1/(2*i+1)
#     return sum_acum
#
#
# n = 1
#
# while abs(4 * leibniz_sum(n) - pi) > 0.001:
#     n += 1
#
#
# print('The number of terms needed is', n)
