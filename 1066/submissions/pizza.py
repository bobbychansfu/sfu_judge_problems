#Bobby wants to buy pizza and he has two options to choose from. However he is not sure which one is better in terms of price per square centimeter. Write a program to help Bobby calculate which pizza is better.

#Input
#diameter and price of the first pizza.
#diameter and price of the second pizza.

#Output 
#the price per square centimeter for each pizza
#the area of each pizza 
#which pizza is a better buy based on the lower price per square centimeter.

#Hint
#Use formula of area of a circle

diameter1 = float(input("Enter the diameter of pizza 1: "))
price1 = float(input("Enter the price of pizza 1: "))
diameter2 = float(input("Enter the diameter of pizza 2: "))
price2 = float(input("Enter the price of pizza 2: "))

# Calculate the area of each pizza
radius1 = diameter1 / 2
area1 = 3.14 * (radius1 ** 2)

radius2 = diameter2 / 2
area2 = 3.14 * (radius2 ** 2)

# Calculate the price per square inch for each pizza
price_per_sq_inch1 = price1 / area1
price_per_sq_inch2 = price2 / area2

# Determine which pizza is a better buy
if price_per_sq_inch1 < price_per_sq_inch2:
    print("The first pizza is the better buy.")
elif price_per_sq_inch2 < price_per_sq_inch1:
    print("The second pizza is the better buy.")
else:
    print("Both pizzas have the same price per square inch.")