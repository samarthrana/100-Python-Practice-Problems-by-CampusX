# Write a program to print the following pattern
# *
# **
# ***
# **
# *

row = int(input("Enter nos rows: "))

for i in range(1, row+1):
    for j in range(0, i):

        print("*", end = " ")

    print("")

for k in range(row, 1, -1):
    for l in range(0, k-1):
        print("*", end = " ")
    print("")


