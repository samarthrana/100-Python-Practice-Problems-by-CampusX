# Coumpound Interest


def CI(p, r, n, t):

    Amount = 0
    n = int()
    if n > 0:
        
        Amount = p((1+r/n)**n)**t
        
    return Amount - p

# p = int(input())
# r = float(input())
# n = int(input())
# t = int(input())

var = CI(1000, 5, 3, 3)
print(var)