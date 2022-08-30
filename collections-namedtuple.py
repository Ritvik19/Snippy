from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt1 = Point(1, 2)
pt2 = Point(3, 4)
dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot_product)
# 11

from collections import namedtuple

Car = namedtuple("Car", "Price Mileage Colour Class")
xyz = Car(Price=100000, Mileage=30, Colour="Cyan", Class="Y")
print(xyz)
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(xyz.Class)
# Y
