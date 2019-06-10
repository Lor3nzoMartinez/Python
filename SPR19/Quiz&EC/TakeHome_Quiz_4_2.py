import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


def dotted(t, Lng, color, n):
    t.color(color)
    n = n + (n-1)
    Lng = Lng / n
    t.fd(Lng / 2)
    for i in range(n//2):
        t.pu()
        t.fd(Lng / 2)
        t.pd()
        t.fd(Lng/2)


def dashed_pentagon(t, Lng, color, n):
    t.color(color)
    for i in range(5):
        dotted(t, Lng, color, n)
        t.lt(72)


# dotted(alex, 270, 'blue', 5)
dashed_pentagon(alex, 270, 'green', 5)

wn.mainloop()
