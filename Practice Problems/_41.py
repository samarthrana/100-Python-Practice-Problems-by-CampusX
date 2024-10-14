# Write a program to print the following pattern
# *
# **
# ***
# ****
# *****


for i in range(6):
    for j in range(6):

        if i == j:
            print('*'*i)
        else:
            pass

# Another Approach

for i in range(i, n):
    for j in range(0, i):
        print('*', end = " ")
    print("")


    

