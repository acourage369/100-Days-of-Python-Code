# EXX
print("Hello welcome to my BMI calculator")

height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n"))

BMI = round(weight / height **2)

if BMI < 18.5:
    print(f"Your BMI is {BMI},you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI},you have normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI},you are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI},you are obese")
else:
    print(f"Your BMI is {BMI},you are clinically obese")

