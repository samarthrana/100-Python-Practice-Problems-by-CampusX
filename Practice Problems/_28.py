# Write a program to print whether a given number is prime number or not

def prime(num):

    if num%1 == 0 and num%num == 0:
        print("Number is Prime")
    else:
        print("Not Prime")

prime(37)