import turtle, time

wn = turtle.Screen()
alex = turtle.Turtle()


def setup_light(t, x):
    t.seth(90)
    t.begin_fill()
    for i in range(2):
        t.fd(x + 30)
        t.lt(90)
        t.fd(x//2)
        t.lt(90)
    t.end_fill()
    setup_circle(t, x)
    light_logic(t, x)



def setup_circle(t, x):
    t.seth(180)
    t.fd((x / 2) / 2)
    t.rt(90)


def light_logic(t, x):
    timer = 4
    pos = t.pos()
    t.shape('circle')
    while timer > 0:
        t.pu()
        if timer == 4:
            t.showturtle()
            t.color('red')
            x1, y = t.pos()
            round(x1, 4)
            round(y, 4)
            t.goto(x1, y + round((x/3), 3))
            time.sleep(1)
            timer += -1

        if timer == 3:
            t.color('yellow')
            x1, y = t.pos()
            round(x1, 4)
            round(y, 4)
            t.goto(x1, y + round((x/3), 3))
            time.sleep(1)
            timer += -1

        if timer == 2:
            t.color('green')
            x1, y = t.pos()
            round(x1, 4)
            round(y, 4)
            t.goto(x1, y + round((x/3), 3))
            time.sleep(1)
            timer += -1
        t.hideturtle()
        t.goto(pos)
        t.pd()
        timer = 4


setup_light(alex, 100)


wn.mainloop()
