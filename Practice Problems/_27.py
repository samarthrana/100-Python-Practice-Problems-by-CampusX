# Write a program to print the first 25 odd numbers

count = 0
i = 1

while True:

    if i%2 != 0:
        print(i)
        count += 1
    if count == 25:
        break
    i += 1
