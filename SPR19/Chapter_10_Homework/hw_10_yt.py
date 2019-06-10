import turtle

wn = turtle.Screen()
alex = turtle.Turtle()


def bar_graph(t, n):
    des = ''

    if 95 <= n <= 100 :
        des = '''A's'''
        print(des)
    elif 85 <= n <= 95:
        des = '''B's'''
        print(des)
    elif 75 <= n <= 85:
        des = '''C's'''
        print(des)
    elif 65 <= n <= 75:
        des = '''D's'''
        print(des)
    elif n < 65:
        des = '''F's'''
        print(des)

    t.lt(90)
    t.fd(n)
    t.rt(90)
    t.fd(20)
    t.write(n, des)
    t.fd(30)
    t.rt(90)
    t.fd(n)
    t.lt(90)
    t.fd(5)


for i in [50, 60, 70, 80, 90, 100]:
    bar_graph(alex, i)

wn.mainloop()