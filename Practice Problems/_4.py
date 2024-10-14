# Write a program that will give you the sum of 3 digits

L = []
i = 1
while i<4:
    x = int(input("Enter the number = "))
    L.append(x)
    i += 1

T = tuple(L)
print("Sum of numbers = ", sum(T))
    


