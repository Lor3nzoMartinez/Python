import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


def square(t, sz):
    for i in range(4):
        t.fd(sz)
        t.lt(90)
    t.fd(sz)


def design(t, n, sz):
    for i in range(n):
        square(t, sz)
        t.pu()
        t.rt(90)
        t.fd(sz/2)
        t.lt(90)
        t.fd(sz/2)
        t.lt(90)
        t.pd()
        sz = sz*2

    # for i in range(n):
    #     square(t, sz)
    #     t.fd(sz / 2)
    #     sz = sz * 2


# square(alex, 20)
design(alex, 8, 20)

wn.mainloop()