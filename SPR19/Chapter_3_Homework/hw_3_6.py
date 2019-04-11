import turtle

'''
6. Use for loops to make a turtle draw these regular polygons (regular means all sides the
same lengths, all angles the same):

• An equilateral triangle

• A square

• A hexagon (six sides)

• An octagon (eight sides)
'''

wn = turtle.Screen()

wn.bgcolor('white')

alex = turtle.Turtle()

for i in range(3):
    alex.fd(100)
    alex.rt(120)

for i in range(4):
    alex.fd(100)
    alex.rt(90)

for i in range(6):
    alex.fd(100)
    alex.rt(60)

for i in range(8):
    alex.fd(100)
    alex.rt(45)
