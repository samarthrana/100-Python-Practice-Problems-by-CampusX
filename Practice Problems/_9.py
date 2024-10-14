# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

def triangle(a, b, c):

    if a+b+c == 180:
        print("Yes, a triangle can be formed with the given angles.")
    else:
        print("Not Possible")

a = float(input("Enter 1st angle: "))
b = float(input("Enter 2nd angle: "))
c = float(input("Enter 3rd angle: "))

print(triangle(a, b, c))