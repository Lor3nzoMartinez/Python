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


def rectangle(t, w, h):
    for i in range(2):
        t.fd(h)
        t.rt(90)
        t.fd(w)
        t.rt(90)


def rectangle_stuff(t, w, h):
    rectangle(t, w, h)
    t.rt(90)
    t.fd(h/2)
    t.lt(90)
    t.fd(-h/2)


rectangle_stuff(alex, 50, 55)

wn.mainloop()
