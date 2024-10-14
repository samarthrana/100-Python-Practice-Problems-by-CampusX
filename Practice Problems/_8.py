# Write a program to find the euclidean distance between two coordinates.
import math

def eucledian_distance(a, b):

    dis = math.sqrt(((b[0] - a[0])*2 + (b[1] - a[1])*2))
    return dis

def create_point(x, y):

    return [x, y]

x1 = float(input("Enter the x value of point a: "))
y1 = float(input("Enter the y value of point a: "))
x2 = float(input("Enter the x value of point b: "))
y2 = float(input("Enter the y value of point b: "))

a = create_point(x1, y1)
b = create_point(x2, y2)

distance = eucledian_distance(a, b)

print("Distance between a and b is = ", distance)


