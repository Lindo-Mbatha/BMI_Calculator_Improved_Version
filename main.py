print("Welcome to the BMI Calculator (Improved version)")

height = float(input("enter your height in metres: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height**2

if bmi <= 18:
  print(f"Your BMI is {round(bmi)}, you are underweight")
elif bmi <= 22:
    print(f"Your BMI is {round(bmi)}, you have a normal weight")
elif bmi <= 28:
    print(f"Your BMI is {round(bmi)}, you are slightly overweight")
elif bmi <= 33:
    print(f"Your BMI is {round(bmi)}, you are obese")
else:
  print(f"Your BMI is {round(bmi)}, you are clinically obese")