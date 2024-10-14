#  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input())

result = n + (n*10 + n) + ((n*100) + (n*10) + n)


#  Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input())
n = str(n)
nn = str(n)+str(n)
nnn = str(n)+str(n)+str(n)

result = n + nn + nnn

print(result)