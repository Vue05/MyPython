'''print("Hello World")

print("*" * 10)

course = "python programming"
print(course[3])
print(course.title())
print(course.strip())
print(course.find(" pro"))
print(course.replace("programming", "code"))

print("ode" in course)'''

good_credit = True
high_income = False 
student = False

if (high_income or good_credit) and not student:
    print('Eligible')
else:
    print('Ineligible')
