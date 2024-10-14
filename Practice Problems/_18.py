# Write a program that will check whether the number is armstrong number or not.

def Armstrong(number):

    sum = 0
    n = int(len(str(number)))
    L = []
    for i in range(n):
            
        L.append(number%10)
        number //= 10

    for i in range(n):

        sum = sum + L[i]**n
        
    return sum

    if sum == number:
        return True
    return False

number = int(input())
if Armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number.")