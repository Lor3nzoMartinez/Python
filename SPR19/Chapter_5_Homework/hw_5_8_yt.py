import turtle

## GUI INTERFACE

wn = turtle.Screen()
wn.bgcolor("lightgrey")
wn.title("Makin Bacon")

## TURTLEs

'''I will use to make most of background'''
bagrou = turtle.Turtle()
bagrou.color('pink')
bagrou.pensize(3)

'''I will use to make most of the design'''
fogrou = turtle.Turtle()
fogrou.color('lightblue')
fogrou.pensize(3)

'''The turtle i will use if i need to complete my design or to help out'''
extr = turtle.Turtle()
extr.color('black')
extr.pensize(1)

# Screen Facts

'''
Resolution = 795,945
Top right corner = 470,400
Top left corner = -475,400
Bot right corner = 470,-395
Bot left corner = -475,-395
'''

# Variable

Stats = [75, 65, 85, 95, 110, 120, 115, 125, 117, 180, 150, 175, 200, 210]


# Functions


def set_corner(Turtle, x, y):
    Turtle.pu()
    Turtle.setpos(x, y)
    Turtle.pd()


def bar_graph(Turtle, ls):
    set_corner(Turtle, -350, -200)
    for n in ls:
        Turtle.begin_fill()
        if n >= 100 and n < 200:
            Turtle.fillcolor('yellow')
        elif n < 100:
            Turtle.fillcolor('green')
        elif n >= 200:
            Turtle.fillcolor('red')
        Turtle.lt(90)
        Turtle.fd(n)
        Turtle.rt(90)
        Turtle.fd(5)
        Turtle.write(n)
        Turtle.fd(15)
        Turtle.rt(90)
        Turtle.fd(n)
        Turtle.end_fill()
        Turtle.lt(90)
        Turtle.fd(5)


##Execution

bar_graph(extr, Stats)

## ETC.
wn.mainloop()