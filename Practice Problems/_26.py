# Write a program that can find the factorial of a given number provided by the user.

def factorial(num):

    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(10))


    