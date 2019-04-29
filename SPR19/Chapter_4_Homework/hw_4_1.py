import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


def square(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(90)
    t.fd(sz)


def line_of_squares(t, sz, spc, n):
    for i in range(n):
        square(t, sz)
        t.pu()
        t.fd(spc)
        t.pd()


line_of_squares(alex, 20, 20, 5)
# square(alex, 20)

wn.mainloop()