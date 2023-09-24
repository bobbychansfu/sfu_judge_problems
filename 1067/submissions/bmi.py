weight=float(input("Enter weight (kg): "))
height=float(input("Enter height (cm): "))
BMI=weight/((height/100)**2)      #formula for calculating bmi

if BMI<16:
    print("Severe Thinness")
elif BMI<17:
    print("Moderate Thinness")
elif BMI<18:
    print("Mild Thinness")
elif BMI<25:
    print("Normal")
elif BMI<30:
    print("Overweight")
elif BMI<35:
    print("Case I Obesity")
elif BMI<40:
    print("Case II Obesity")
else:
    print("Case III Obesity")