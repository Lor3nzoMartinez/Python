import turtle, random

wn = turtle.Screen()
renny = turtle.Turtle()
renny.speed(0)


def draw_axis(t, x):
    for i in range(4):
        t.lt(90)
        t.goto(0, 0)
        for j in range(1, x + 1):
            t.fd(20)
            if t.pos() < (0, 0):
                j = ' -' + str(j)
                t. write(j)
            else:
                j = ' ' + str(j)
                t.write(j)


def rectangle(t, xc, yc, W, H):
    t.pu()
    t.goto(xc, yc)
    t.pd()
    for i in range(2):
        t.lt(90)
        t.fd(H)
        t.lt(90)
        t.fd(W)


def get_center_of_rect(t, W, H):
    xc, yc = t.pos()
    xc = (-W/2) + xc
    yc = (H/2) + yc
    return xc, yc


def turtle_change(t, xc, yc):
    t.pu()
    t.goto(xc, yc)
    t.pd()


def playground(t, xc, yc, W, H):
    draw_axis(t, 20)
    rectangle(t, xc, yc, W, H)
    xc, yc = get_center_of_rect(t, W, H)
    turtle_change(t, xc, yc)


def is_in_rect(t,xc, yc, W, H):
    playground(t, xc, yc, W, H)
    xc, yc = get_center_of_rect(t, W, H)
    x, y = t.pos()
    TV = (xc - W / 2 <= x <= xc + W / 2) and (yc - H / 2 <= y <= yc + H / 2)
    return TV



def random_walk(t, xc, yc, W, H):
    while is_in_rect(t, xc, yc, W, H):
        trn_ngl = random.randint(0, 359)
        t.lt(trn_ngl)
        t.fd(20)
    else:
        return


random_walk(renny, 20, 50, 50, 75)

wn.mainloop()
