# Write a program that will tell whether the number entered by the user is odd or even.

def ODD_EVE(num):

    if num%2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")

number = int(input())
x = ODD_EVE(number)
print(x)