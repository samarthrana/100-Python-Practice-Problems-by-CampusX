# Take a number from the user and find the number of digits in it. 

# APPROACH 1

num = int(input())

str_num = str(num)

no_of_digits = len(str_num)

print(no_of_digits)

# Approach 2: without using len function

num = int(input())
str_num = str(num)
count = 0
for i in str_num:
    count += 1

print("Number of digits =", count)




