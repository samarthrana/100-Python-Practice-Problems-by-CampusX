# Write  a program to print the following pattern
#         *
#       * * *
#     * * * * *
#    * * * * * * *
# * * * * * * * * *

n = int(input())

for i in range(1, n+1):
    for j in range(0, n-i):
        print(" ", end = "")
    
    for k in range(1, 2*i):
        print("*", end= "")
    print("")