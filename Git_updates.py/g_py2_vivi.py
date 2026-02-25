print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill += 5
        print("Please pay $5.")
    elif age <= 18:
        bill += 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("You're doing amazing, enjoy a free ride with us!")
    else:
        bill += 12
        print("Please pay $12.")

    photo_taken = input("Would you like to have your photo taken? Answer Yes or No ")
    if photo_taken == "Yes":
        bill += 3
        print(f"Your total bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
