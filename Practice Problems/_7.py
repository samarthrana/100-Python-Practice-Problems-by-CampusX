# Write a program that will tell whether the given year is a leap year or not.abs

def leap_year(x):

    if x%4 == 0:
        print("It's a Leap Year.")
    else:
        print("It's not a Leap Year.")

year = int(input("Enter the year: "))
x = leap_year(year)
print(x)
