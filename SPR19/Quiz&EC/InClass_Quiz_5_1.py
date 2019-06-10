
def distance(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    return abs(x) + abs(y)


def rectPerim(x1,y1, x2, y2, x3, y3, x4, y4):
    length = distance(x1, x2, x3, x4)
    width = distance(y1, y2, y3, y4)
    return abs(length) + abs(width)


print(f'The perimeter of a rectangle whose vertices have coordinates '
      f' (x1, y1 = 0,0), (x2, y2 = 50, 10), (x3, y3 = 30, 110), (x4,y4 = -20, 100) '
      f'is {rectPerim(0,0,50,10,30,110,-20,100)}.')

