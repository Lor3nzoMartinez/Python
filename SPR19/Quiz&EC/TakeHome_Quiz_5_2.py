import math


def circleArea(R):
    A = math.pi*R**2
    return round(A, 2)


def circleCircumference(R):
    C = 2*math.pi*R
    return round(C, 2)


def cylinderArea(R, H):
    SA = (circleCircumference(R)*H)+(2*circleArea(R))
    return round(SA, 2)


def cylinderVolume(R, H):
    V = circleArea(R)*H
    return round(V, 2)


def AtoVRatio(R, H):
    AtoVRatio = cylinderArea(R, H) / cylinderVolume(R, H)
    return round(AtoVRatio, 2)


# print(circleArea(12))
#
# print(circleCircumference(12))
#
# print(cylinderArea(12, 5))
#
# print(cylinderVolume(12,5))
#
# print(f'%{AtoVTRatio(12, 5)}')

print('R   H   Cyl Area   Cyl Vol   (Cyl Area)/(Cyl Vol)')
print('-------------------------------------------------')
for i in range(1, 4):
    for j in range(4, 7):
        print(f'{i}   {j}   {cylinderArea(i, j)}       {cylinderVolume(i, j)}       {AtoVRatio(i, j)}')
