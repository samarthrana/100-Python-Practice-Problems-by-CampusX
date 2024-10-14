# Write a program that will tell the number of dogs and chicken 
# are there when the user will provide the value of total heads and legs.

def dogs_and_chickens():

    heads = int(input("Enter total number of heads: "))
    legs = int(input("Enter total number of legs: "))
    ndogs = 0
    nchickens = 0

    if heads<=legs:

        ndogs = legs/2 - heads
        nchickens = 2*heads - legs/2

        print("Number of dogs =", int(ndogs))
        print("Number of chickens =", int(nchickens))

    else:
        print("Not Possible")

dogs_and_chickens()



