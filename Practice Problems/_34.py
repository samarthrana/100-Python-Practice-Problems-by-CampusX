# Prime number

count = 0

for i in range(2, num//2):

    flag = 0
    if num%i ==0:
        flag = 1
    else:
        flag = 0
        print(i)


