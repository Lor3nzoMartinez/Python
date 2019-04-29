# YouTube: https://youtu.be/YqoFYgCn0o8

import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)


def spiral(t, sz, n):
    t.rt(90)
    t.fd(sz/4)
    for i in range(n):
        t.rt(90)
        t.fd(sz)
        sz += 2


def spiral_canted(t, sz, n):
    t.rt(90)
    t.fd(sz/4)
    for i in range(n):
        t.rt(91)
        t.fd(sz)
        sz += 2


alex.pu()
alex.goto(-250, 0)
alex.pd()

spiral(alex, 5, 150)


alex.pu()
alex.goto(250, 0)
alex.pd()

spiral_canted(alex, 5, 150)


wn.mainloop()

