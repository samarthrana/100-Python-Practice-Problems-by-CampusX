# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

def is_narcissit(num):          #narcissit number and armstrong number are same

    num_str = str(num)
    sum = 0
    n = len(num_str)

    for i in num_str:

        sum += int(i)**n
    
    if sum == num:
        return True
    else:
        return False

num = 1634
x = is_narcissit(num)
print(x)