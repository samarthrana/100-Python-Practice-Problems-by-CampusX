# Print all factors of a given number provided by the user.

def factors(num):

    L = []

    for i in range(1, num//2):

        if num%i==0:
            L.append(i)
    return L

print(factors(24))

