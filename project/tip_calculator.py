print("Welcome to the Tip Calculator")
rate=float(input("Enter the bill amount:Rs "))
tip=int(input("please enter the percentage amount of tip you wish to give  10,12 or 15 :"))
persons=int(input("Enter the number of persons :"))
perc_tip=tip/100
rate_percentage=(perc_tip*rate)
total_bill=rate+rate_percentage
individual_payment=round(total_bill/persons,2)
print(f"Each person should pay: Rs {individual_payment}/-")