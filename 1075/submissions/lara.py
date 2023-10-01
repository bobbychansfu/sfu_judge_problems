# Prompt the user to enter a magical number n
while True:
    
        n = int(input("Enter the magical number engraved on it: "))
        if n < 2:
            print("Invalid input! ",end="")
            continue
        break
    

# Initialize the starting number
number = 2

print("Reciting the keys to unlock the treasure:")

# Use a while loop to go through the numbers from 2 to n and display the even numbers
while number <= n:
    if number % 2 == 0:  # Check if the number is even
        print(number)
    number += 1  # Move to the next number

print("Congratulations, the treasure chest is unlocked!")
