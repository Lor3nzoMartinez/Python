import turtle

# Youtube: https://youtu.be/oGUzRlMRPV4

wn = turtle.Screen()
alex = turtle.Turtle()


data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]


def move_pirate(t, trn_ngl, steps):
    t.lt(trn_ngl)
    t.fd(steps)


for (x, y) in data:
    move_pirate(alex, x, y)

wn.mainloop()
