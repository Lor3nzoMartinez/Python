import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(25):
    for i in range(4):
        alex.fd(20)
        alex.lt(90)
    alex.lt(15)

wn.mainloop()