# Write a program to print all the unique combinations of 1,2,3 and 4 ?

# BRUTE FORCE

def comb(L):

    for i in range(4):
        for j in range(4):
            for k in range (4):
                for l in range(4):
                    if( i != j and j!=k and k != l and l!=i and i!=k and j!=l):
                        print(L[i], L[j], L[k], L[l])

comb([1, 2, 3, 4])

# USING PERMUTATIONS function

from itertools import permutations

#get all combinations of length 1, 2, 3, 4 of length 4

comb = permutations([1, 2, 3, 4], 4)

for i in comb:
    print(i)


