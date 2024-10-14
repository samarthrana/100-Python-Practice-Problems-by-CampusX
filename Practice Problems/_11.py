# Write a program to find the simple interest when the value of principle,rate of interest and time period is given.

def SI(p, r, t):

    return (p*r*t)/100

p = int(input("Enter Principal Amount: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter the time period: "))

print(SI(p, r, t))
