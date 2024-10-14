# Write a program that will convert celsius value to fahrenheit

while True:

    try:
        x = float(input("Enter the temperature: "))

        if type(x) == float:
            temp = (x*9/5) + 32
            print("Temperature in Farenheit will be: ", temp)
    except:
        print("Error in format.")




