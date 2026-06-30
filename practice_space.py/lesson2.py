name = "Dindu"
height_m = 1.75
weight_kg = 83

bmi = weight_kg / (height_m * height_m)

print(f"Your bmi is : {round(bmi, 2)}")

if bmi >= 25.0:
    print(f"{name} is overweight")
elif bmi <= 18.5:
    print(f"{name} is underweight")
else:
    print(f"{name} is not overweight")
