import turtle
'''
bg = input("What's your favorite color? (red, green, blue, pink):")
tc = input("What color would you like the turtle to be?")
ps = input("How thick would you like the lines?")
'''

wn = turtle.Screen()

wn.bgcolor('white')

alex = turtle.Turtle()
alex.pensize(3)
alex.color('black')


def rectangle(t, h, w):
    for i in range(2):
        t.fd(h)
        t.rt(90)
        t.fd(w)
        t.rt(90)


def pinwheel_1(t, h, w, n):
    rot = 360 / n
    for i in range(n):
        rectangle(t, h, w)
        t.rt(rot)


def plus (t, sz):
    for i in range(4):
        t.fd(sz)
        t.fd(-sz)
        t.rt(90)

def lineOfPlus(t, sz, sp, n):
    t.pu()
    t.fd(-400)
    for i in range(n):
        t.pd()
        plus(t, sz)
        t.pu()
        t.fd((sz*2)+sp)
        t.pd()


#pinwheel_1(alex, 25, 50, 7)


lineOfPlus(alex, 50, 100, 10)


wn.mainloop()
