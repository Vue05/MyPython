print("Welcome to the tip calculator!")
total_amount = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people_to_split_bill = int(input("How many people to split the bill? "))
bill_per_person = total_amount * (tip_percent / 100)+ total_amount
bill_per_person /= no_of_people_to_split_bill
print(f"Each person should pay: ${round(bill_per_person, 2)}")