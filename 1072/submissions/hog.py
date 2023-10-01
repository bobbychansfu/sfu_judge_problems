def divide_large_number(large_number, prime_number):
    count = 0
    while large_number > 0:
        large_number //= prime_number
        count += 1
    return count

def main():
    # Prompt the user to input a large number
    large_number = int(input("Enter a large number: "))
    
    # Validate the large number input
    if large_number <= 0:
        print("Please enter a positive integer for the large number.")
        return
    
    # Prompt the user to input a prime number
    prime_number = int(input("Enter a prime number (2, 3, 5, or 7): "))
    
    # Validate the prime number input
    if prime_number not in [2, 3, 5, 7]:
        print("Please enter a valid prime number: 2, 3, 5, or 7.")
        return
    
    # Call the function to divide the large number by the prime number
    # and print the number of divisions made
    print("Number of divisions made: ", divide_large_number(large_number, prime_number))

if __name__ == "__main__":
    main()
