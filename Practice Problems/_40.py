# Find the reverse of a number provided by the user(any number of digit) 

def reverse(num):

    str_num = str(num)
    print(str_num[::-1])

num = int(input())
reverse(num)