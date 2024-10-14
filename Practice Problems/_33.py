# # Finding multiples 

def multiples(num, count):

    L = []
    i = 1
    for i in range(1, count+1):
        
        temp = num*i
        L.append(temp)
        i+=1
    
    return L

a = multiples(2, 10)
print(a)

def LCM(num1, num2):

    L1 = multiples(num1, count=100)
    L2 = multiples(num2, count=100)

    for i in L1:
        if i in L2:
            temp = i
            break
        else:
            continue

    return temp

a = LCM(57, 89)
print(a)



# Another Approah

def LCM(a, b):

    greater = max(a, b)
    smaller = min(a, b)

    for i in range(greater, a*b+1, greater  ):

        if i % smaller ==0 :
            return i

print(LCM(8, 16))
