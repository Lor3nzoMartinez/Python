import turtle, time

wn = turtle.Screen()
alex = turtle.Turtle()

green = turtle.Turtle()
green.color('green')
green.shape('circle')
yellow = turtle.Turtle()
yellow.color('yellow')
yellow.shape('circle')
red = turtle.Turtle()
red.color('red')
red.shape('circle')


# alex.circle(50)


def setup_light(t, t1, t2, t3, x):
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t.seth(90)
    t.begin_fill()
    for i in range(2):
        t.fd(x + 30)
        t.lt(90)
        t.fd(x//2)
        t.lt(90)
    t.end_fill()
    setup_circle(t, t1, t2, t3, x)
    light_logic(t1, t2, t3)


def setup_circle(t, t1, t2, t3, x):
    color_pos = [(), (), ()]
    counter = 0
    t.seth(180)
    t.fd((x / 2) / 2)
    t.rt(90)
    for i in color_pos:
        t.pu()
        t.fd(x / 3)
        t.pd()
        color_pos[counter] = t.pos()
        counter += 1
    counter = 0
    for i in [t1, t2, t3]:
        i.pu()
        i.goto(color_pos[counter])
        i.pd()
        i.showturtle()
        counter += 1
    t.hideturtle()


def light_logic(t1, t2, t3):
    timer = 4
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    while timer > 0:
        if timer == 4:
            t1.hideturtle()
            t2.hideturtle()
            t3.showturtle()
            time.sleep(2)
            timer += -1
        if timer == 3:
            t1.hideturtle()
            t2.showturtle()
            t3.hideturtle()
            time.sleep(2)
            timer += -1
        if timer == 2:
            t1.showturtle()
            t2.hideturtle()
            t3.hideturtle()
            time.sleep(2)
            timer += -1
        timer = 4


setup_light(alex, green, yellow, red, 100)


wn.mainloop()
