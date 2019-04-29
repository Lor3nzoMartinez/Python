import turtle

wn = turtle.Screen()
wn.bgcolor('white')

alex = turtle.Turtle()
alex.shape('turtle')

alex.lt(90)


def clock_stuff(s):
    alex.pu()
    alex.fd(s)
    alex.pd()
    alex.fd(s/4)
    alex.pu()
    alex.fd(s/5)
    alex.stamp()
    alex.bk(s + (s/4) + (s/5))


for i in range(12):
    clock_stuff(100)
    alex.rt(30)

wn.mainloop()
