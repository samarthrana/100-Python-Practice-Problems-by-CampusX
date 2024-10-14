# Write  a program that will tell whether the given number is divisible by 3 & 6

def sum_of_digits(num):

    sum = 0
    while num > 0:
        sum += num%10 #Extracting last digit
        num //= 10 #removing last digit
    return sum

# def div3(num):

#     if sum_of_digits(num)%3 == 0:
#         pass
#     else:
#         print("Not divisilble by 3")

def div6(num):

    if num%2 ==0 and div3%3 ==0:
        print("Number is divisible by 3 and 6")
    else:
        print("Not divisible")

N = int(input("Enter the number"))
div3 = sum_of_digits(N)
div6(N)
    
         