# Write a program that will take three digits from the user and add the square of each digit.

def sum_of_square(x1, x2, x3):

    sum = 0
    L = [x1, x2, x3]
    for i in range(0, 3):
        sum = sum + L[i]**2
        i+=1
    return sum

S = sum_of_square(1, 2, 3)
print(S)