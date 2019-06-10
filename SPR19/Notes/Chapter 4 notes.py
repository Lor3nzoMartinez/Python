# import turtle
# import math
#
#
# wn = turtle.Screen()
# alex = turtle.Turtle()
# alex.speed(0)
#
# alex.pu()
# alex.goto(-450, 0)
# alex.pd()
# for i in range(3):
#     alex.fd(100)
#     alex.lt(120)
#
# alex.stamp()
#
#
# def draw_rectangle(t, W, H):
#     t.pu()
#     t.fd(W/2)
#     t.lt(90)
#     t.fd(H/2)
#     t.lt(90)
#     t.pd()
#     for i in range(2):
#         t.fd(W)
#         t.lt(90)
#         t.fd(H)
#         t.lt(90)
#     t.pu()
#     t.fd(W / 2)
#     t.lt(90)
#     t.fd(H / 2)
#     t.lt(90)
#     t.pd()
#
#
# def draw_rects(t, W1, H1, W2, H2):
#     draw_rectangle(t, W1, H1)
#     draw_rectangle(t, W2, H2)
#
#
# draw_rects(alex, 200, 20, 25, 400)
#
#
# def factorial(num):
#     factorials = 1
#     for i in range(1, num+1):
#         factorials = factorials*i
#     return num, factorials
#
# print('n          !n')
# print('-------------')
# for i in range(1, 11):
#     x, y = factorial(i)
#     print(f'{x}          {y}')
#
#
# def f2c(num):
#     C = (num - 32)*(5/9)
#     return C
#
#
# def f2K(num):
#     K = f2c(num) + 273.15
#     return K
#
#
# print(f2c(1))
# print(f2K(1))
#
# def final_amt(p, r, n, t):
#     A = (1 + r/n)
#     A = A**(n*t)
#     A = p*A
#     return round(A, 2)
#
# print('year        $amt')
# for i in range(1, 21):
#     print(f'{i}          {final_amt(1000, 0.05, 1, i)}')
#
# Problem 4_7
#
# colr = ['pink', 'black', 'yellow']
#
# def rectangle(t, W, H):
#     for i in range(2):
#         t.fd(W)
#         t.lt(90)
#         t.fd(H)
#         t.lt(90)
#
#
# def turtle_refactor(colr, ttle):
#     W, H = 100, 50
#     for i in range(3):
#         rectangle(ttle, W + 50, H * 2)
#         ttle.lt(35)
#
# for i in [alex, tess, dave]:
#     turtle_refactor(colr, i)
#
#
# Problem 4_8
#
# def distance(x1, y1, x2, y2):
#     D = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
#     return D
#
# def trngl_perim(x1,y1,x2,y2,x3,y3):
#     P1 = distance(x1,y1,x2,y2)
#     P2 = distance(x2,y2,x3,y3)
#     P3 = distance(x3,y3,x1,y1)
#     return P1 + P2 +P3
#
# print(trngl_perim(1,2,3,-4,-4,5))
#
# Problem 4_9
#
# def e_to_the_x_series(x, n):
#     ans = 1
#     for i in range(n):
#         ans *= math.exp(x)/x
#
#     return ans
#
# print(e_to_the_x_series(5,10))
#
# Problem 4_10
#
# def square(t, s):
#     for i in range(4):
#         t.fd(s)
#         t.lt(90)
#     t.fd(s)
#
#
# def line_o_squares(t, s, spc, n):
#     for i in range(n):
#         square(t, s)
#         t.pu()
#         t.fd(spc)
#         t.pd()
#
# def line_o_squares2(t, s, spc, n):
#     for i in range(n):
#         square(t, s)
#         t.fd(spc)
#
#
# def square_o_squares(t, s, spc, n, n2):
#     for i in range(n2):
#         for j in range(4):
#             line_o_squares(t, s, spc, n)
#             t.pu()
#             t.fd(spc*2)
#             t.pd()
#             t.lt(90)
#         t.pu()
#         for i in range(2):
#             line_o_squares2(t, s, spc, n)
#         t.pd()
#
#
#
# square_o_squares(alex, 10, 5, 5, 5)
#
#
# wn.mainloop()
