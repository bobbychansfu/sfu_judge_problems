PI = 3.14
RATE_PER_LITRE = 2.35 

# Input cylinder dimensions
r = int(input())
h = int(input())

# Calculate volume 
volume_cm3 = PI * r**2 * h 

# Convert to litres
volume_litres = volume_cm3 / 1000

# Calculate total price
total_price = volume_litres * RATE_PER_LITRE

print(round(total_price,2))