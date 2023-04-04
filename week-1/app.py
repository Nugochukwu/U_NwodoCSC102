choice = int(input("What calculation do you want to do"
                   " 1-Simple Interest"  
                   " 2-Compound Interest"  
                   " 3-Annuity Plan "))
if choice == 1:
    principle = float(input("What is the principle "))
    rate = float(input("What is the rate "))
    time = float(input("What is the time period in years "))
    amount = principle * (1 + (rate/100) * time)
    print(amount)
elif choice == 2:

    principle = float(input("What is the principle "))
    rate = float(input("What is the rate "))
    period = float(input("What are the number of compounding periods per year"))
    time = float(input("What is the time period in years "))
    amount = principle * (1 + rate/period) ** (period * time)
    print(amount)
elif choice == 3:

    principle = float(input("What is the principle "))
    rate = float(input("What is the rate "))
    period = float(input("What are the number of compounding periods per year"))
    time = float(input("What is the time period in years "))
    amount = (principle * ((1 + rate / period) ** (period * time)) - 1)/(rate/period)
    print(amount)

    
else:
    print("Invalid Input")