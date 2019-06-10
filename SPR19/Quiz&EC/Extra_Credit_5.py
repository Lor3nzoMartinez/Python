import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
alex.pu()
alex.goto(-400, 0)
alex.pd()


def triangle(t, sz):
    for i in range(3):
        t.fd(sz)
        t.lt(-120)


def inv_triangle(t, sz):
    for i in range(3):
        t.fd(sz)
        t.lt(120)


def test_me():
    triangle(alex, 100)
    alex.rt(60)
    alex.fd(100)
    alex.lt(60)
    inv_triangle(alex, 100)
    alex.rt(60)
    inv_triangle(alex, 100)
    alex.fd(100)
    alex.rt(60)
    triangle(alex, 100)
    alex.rt(120)
    inv_triangle(alex, 100)
    alex.rt(120)
    inv_triangle(alex, 100)
    alex.fd(100)
    alex.lt(120)
    triangle(alex, 100)


for i in range(4):
    test_me()
    alex.rt(90)
    alex.fd(-173)
    alex.seth(60)
    test_me()


wn.mainloop()
