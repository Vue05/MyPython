height = int(input("What is your height in cm? "))

if height >= 117:
    print("You can go on the ride!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("You can pay $5")
    elif age <= 18:
        print("You can pay $7")
    else:
        print("You have to pay $12")

else:
    print("Feel free to come back when you're taller!")
