import turtle

# Youtube: https://youtu.be/oe7JBBQsU0w

wn = turtle.Screen()
turtle.tracer(0, 0)
alex = turtle.Turtle()
alex.pensize(3)


def find_portions(x, y):
    x = x/6
    y = y/6
    return x, y


def positioning(t):
    screenheight, screenwidth = wn.canvheight, wn.canvwidth
    move_to(t, screenheight*-1/3, screenheight - screenwidth*1/6)
    x, y = find_portions(screenwidth*2, screenheight*2)
    return y, x


def rectangle(t, x, y):
    for i in range(2):
        t.fd(x)
        t.rt(90)
        t.fd(y)
        t.rt(90)


def square(t, x):
    for i in range(4):
        t.fd(x)
        t.lt(90)


def trapezoid(t, x):
    t.rt(30)
    t.fd(x*1/4)
    t.rt(60)
    t.fd(x - x * 1/4)
    t.rt(60)
    t.fd(x*1/4)
    t.rt(120)
    t.fd(x)


def move_to(t, x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def box_two_tabs(t, x, x1, y1):
    square(t, x)
    trapezoid(t, -x)
    move_to(t, x1 + x, y1 + x)
    t.seth(90 - t.heading())
    trapezoid(t, x)


def box_one_tab(t, x):
    square(t, x)
    trapezoid(t, -x)


def f_pattern(t, x, y, color, color1, space):
    x1, y1 = t.pos()
    t.color(color)
    t.begin_fill()
    rectangle(t, x, y)
    t.end_fill()
    move_to(t, x1 + x + space, y1)
    t.color(color1)
    t.begin_fill()
    rectangle(t, x/2, y)
    t.end_fill()
    x1, y1 = t.pos()
    move_to(t, x1 + x/2 + space, y1)


def alt_f_pattern(t, x, y, color, color1, space):
    x1, y1 = t.pos()
    t.color(color)
    t.begin_fill()
    rectangle(t, x / 2, y)
    t.end_fill()
    move_to(t, x1 + x/2 + space, y1)
    t.color(color1)
    t.begin_fill()
    rectangle(t, x, y)
    t.end_fill()
    x1, y1 = t.pos()
    move_to(t, x1 + x + space, y1)


def f_pattern_4by4(t, x, y, color, color1, space):
    counter = 1
    x1, y1 = t.pos()
    for i in range(4):
        for j in range(4):
            if counter % 2 == 0:
                alt_f_pattern(t, x, y, color, color1, space)
            else:
                f_pattern(t, x, y, color, color1, space)
        y1 = y1 - y - space
        move_to(t, x1, y1)
        counter += 1


def m_pattern(t, x, y, color, color1, space):
    x1, y1 = t.pos()
    t.seth(270)
    t.color(color1)
    t.begin_fill()
    square(t, x/2)
    t.end_fill()
    move_to(t, x1 + x/2, y1 - x/2 - space)
    t.color(color)
    t.begin_fill()
    rectangle(t, y/2, x/2)
    t.end_fill()
    move_to(t, x1 + x/2 + space, y1 - x/2)
    t.seth(90)
    t.color(color)
    t.begin_fill()
    rectangle(t, x/2, y/2)
    t.end_fill()
    move_to(t, x1 + x/2 + space, y1 - x/2 - space)
    t.seth(270)
    t.color(color1)
    t.begin_fill()
    square(t, x)
    t.end_fill()
    t.seth(0)
    x1, y1 = t.pos()
    move_to(t, x1 + x + space, y1 + x/2 + space)


def m_pattern_4by4(t, x, color, color1, space):
    y = x*2
    x1, y1 = t.pos()
    x1c, y1c = x1, y1
    for i in range(4):
        for j in range(4):
            m_pattern(t, x, y, color, color1, space)
            x1 = x1 + x + (x / 2) + (space * 2)
            move_to(t, x1, y1)
        y1 = y1 - x/2 - y/2 - (space * 2)
        x1 = x1c
        move_to(t, x1, y1)


def my_pat(t, x, color, color1, space):
    t.seth(270)
    for i in range(2):
        t.color(color)
        t.begin_fill()
        square(t, x)
        t.end_fill()
        x1, y1 = t.pos()
        move_to(t, x1, y1 - x - space)
        t.color(color1)
        t.begin_fill()
        square(t, x)
        t.end_fill()
        move_to(t, x1 + x + space, y1)


def my_pat_4by4(t, x, color, color1, space):
    x1, y1 = t.pos()
    for i in range(4):
        for j in range(4):
            my_pat(t, x, color, color1, space)
        move_to(t, x1, y1 - x * 2 - space * 2)
        x1, y1 = t.pos()


def box_setup(t):
    x, y = positioning(t)
    x1, y1 = t.pos()
    box_two_tabs(t, x, t.xcor(), t.ycor())
    move_to(t, x1 + x, y1 - x)
    square(t, x)
    move_to(t, x1, y1 - x*2)
    t.seth(0)
    box_two_tabs(t, x, t.xcor(), t.ycor())
    move_to(t, x1 + x, y1 - x*3)
    box_one_tab(t, x)
    move_to(t, x1 + x*2, y1)
    box_one_tab(t, x)
    move_to(t, x1 - x, y1 - x)
    t.seth(0)
    box_one_tab(t, x)
    return x, y, x1, y1


def full_design(t, color, color1, color2, color3):
    x, y, x1, y1 = box_setup(t)
    x1c, y1c = x1, y1
    x, y = x/7, y/6
    t.seth(0)
    move_to(t, x1 - 0.5, y1 + (y * 4.38) - 0.17)
    t.pensize(1)
    for i in range(2):
        for j in range(1):
            f_pattern_4by4(t, x, y, color, color1, 2)
            x1, y1 = t.pos()
            move_to(t, x1, y1 - 1)
            m_pattern_4by4(t, x, color, color1, 2)
        color, color1 = color1, color
    for i in range(1):
        move_to(t, x1c - x * 6 - 14, y1c - 1)
        x1c, y1c = t.pos()
        for j in range(1):
            my_pat_4by4(t, x/1.3 - 0.5, color2, color3, 2)
        move_to(t, (x1c + (x * 6) + 16) - (x1c + (x * 6) + 14), y1c)
        x1c, y1c = t.pos()
        color2, color3 = color3, color2
        for l in range(1):
            my_pat_4by4(t, x/1.3 - 0.5, color2, color3, 2)


full_design(alex, 'yellow', 'blue', 'red', 'black')


wn.mainloop()
