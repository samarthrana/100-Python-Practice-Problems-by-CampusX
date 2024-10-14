# HCF of two numbers

#finding factors first
# def factors(num1):

#     L = []
#     for i in range (1, num1+1):
#         if num1%i == 0:
#             L.append(i)
#     return L

# # x = factors(44)
# # print(x)  # List of all the factors

# # calculating HCF

# def HCF(num1, num2):

#     L1 = factors(num1)
#     L2 = factors(num2)
#     comm = []

#     for i in L1:
#         if i in L2:
#             comm.append(i)

#     return max(comm)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# a = HCF(num1, num2)
# print(a)



# ANOTHER APPROACH

def computeGCD(x, y):

    if x>y:
        small = y
    else:
        small = x

    for i in range(1, small + 1):
        if ((x%i == 0) and (y%i == 0)):
            gcd = i 

    return gcd

a = 60
b = 48

print(computeGCD(60, 48))




