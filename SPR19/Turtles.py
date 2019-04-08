import turtle

bg = input("What's your favorite color? (red, green, blue, pink):")
tc = input("What color would you like the turtle to be?")
ps = input("How thick would you like the lines?")

wn = turtle.Screen()

wn.bgcolor(bg)

alex = turtle.Turtle()
alex.pensize(int(ps))
alex.color(tc)


def rectangle(t, h, w):
    for i in range(2):
        t.fd(h)
        t.rt(90)
        t.fd(w)
        t.rt(90)


rectangle(alex, 10, 20)

wn.mainloop()
