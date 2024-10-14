# Print the first 20 numbers of a Fibonacci series  

def fibonacci(num):

    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)


print('0')
for i in range(0, 20):

    print(fibonacci(i))