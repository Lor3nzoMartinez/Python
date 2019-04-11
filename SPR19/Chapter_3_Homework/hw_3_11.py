import turtle

wn = turtle.Screen()
wn.bgcolor('white')

alex = turtle.Turtle()

for i in range(5):
    alex.rt(144)
    alex.fd(100)

alex.pu()
alex.fd(15)
alex.hideturtle()

wn.mainloop()