# Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit

class unit_conversion:

    def __init__(self):

        self.menu()

    def menu(self):

        user_input = input("""Choose a unit system:
        1. Length Conversion (cm to ft)
        2. Distane Conversion (km to miles)
        3. Currency Conversion (USD to INR)
        4. Exit""")

        if user_input == '1':
            self.Length_Conversion()
        elif user_input == '2':
            self.Distance_Conversion()
        elif user_input == '3':
            self.Currency_Conversion()
        elif user_input == '4':
            print("Bye")

    
    def Length_Conversion(self):

        num = float(input("Enter length in cm: "))
        num = 0.0328084*num
        print("Length in ft = ", num)

    def Distance_Conversion(self):

        dis = float(input("Enter distance in km: "))
        dis = dis*0.62
        print("Distance in miles = ", dis)

    def Currency_Conversion(self):

        amt = float(input("Enter the amount in USD: "))
        amt = 83.97*amt
        print("Amount in INR = ", amt)


convert = unit_conversion()

convert.Length_Conversion()


    