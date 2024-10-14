# Write a program that can multiply 2 numbers provided by the user without using the * operato

def multiply(a, b):

    if b == 1:
        return a
    else:
        return a + multiply(a, b-1)

print(multiply(3, 4))