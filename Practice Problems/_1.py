# User will input (3ages). Find the oldest one. 
L = []

for i in range(1, 4):
    x = (input("Enter the age: "))
    L.append(x)

print("Oldest one's age is: ",  max(L), "years")