layer1_height = float(input("Enter height of layer 1 (cm): "))
layer1_diameter = float(input("Enter diameter of layer 1 (cm): "))

layer2_height = float(input("Enter height of layer 2 (cm): "))  
layer2_diameter = float(input("Enter diameter of layer 2 (cm): "))

layer3_height = float(input("Enter height of layer 3 (cm): "))
layer3_diameter = float(input("Enter diameter of layer 3 (cm): "))

flavor = input("Enter cake flavor: ")

# Calculate total height 
total_height = layer1_height + layer2_height + layer3_height

# Validate rules
if total_height < 20:
  print("Your", flavor, "cake does not meet minimum height requirement of 20 cm.")
elif (layer1_diameter < 10 or layer1_diameter > 30) or (layer2_diameter < 10 or layer2_diameter > 30) or (layer3_diameter < 10 or layer3_diameter > 30):
  print("Your",flavor,"cake layer diameter does not meet contest rules.")  
else:
  print("Your",flavor,"cake entry is valid!")
