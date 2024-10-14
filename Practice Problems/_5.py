# Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

# BRUTE FORCE

# x = int(input("Enter a 4 digit number: "))

# a = x//1000
# b = (x%1000)//100
# c = ((x%1000)%100)//10
# d = ((x%1000)%100)%10

# print("Reverse of the number = ", d*1000+c*100+b*10+a)

# MAKING A FUNCTION

def reverse_number(num):
    #Reverses a 4 digit number
    return int(str(int(num))[::-1])

number = 1234
reversed_number = reverse_number(number)
print(reversed_number)