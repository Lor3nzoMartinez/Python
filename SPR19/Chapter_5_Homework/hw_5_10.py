import math

x = 0

def find_hypot ( a, b):
        x = a**2 + b**2
        x = math.sqrt(x)
        return x

print(find_hypot(2,3))