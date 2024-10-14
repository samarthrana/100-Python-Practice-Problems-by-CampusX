# Print all the armstrong numbers in the range of 100 to 1000

def armstrong(num):

    n = len(str(num))
    num_str = str(num)
    sum = 0

    for i in num_str:

        sum += int(i)**n

    if sum == num:
        return True
    else:
        return False

for i in range(100, 1000):

    if armstrong(i) == True:
        print(i)
    else:
        pass


    