# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

def Profit_Loss(x, y):

    if x>y:
        print("Profit of", x - y)
    else:
        print("Loss of", y-x)

SP = int(input("Enter the Selling Price: "))
CP = int(input("Enter the Cost Price: "))

print(Profit_Loss(SP, CP))