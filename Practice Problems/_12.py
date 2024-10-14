# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

def Volume(r, h):

    v = 2*3.14*r*h
    return v

def Price(v):

    rate = v*40
    print("Rate of Milk = Rs", rate)

r = int(input("Enter radius: "))
h = int(input("Enter height: "))
v = Volume(r, h)

print(v)
print(Price(v))

