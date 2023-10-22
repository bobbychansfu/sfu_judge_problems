def order(a, b, c):
    # Put the numbers in a list
    numbers = [a, b, c]

    # Sort the list
    numbers.sort()

    # Convert the list back to a tuple and return it
    return tuple(numbers)

def main():
    num1, num2, num3 = tuple(map(int, input().split(" ")))
    sorted_numbers = order(num1, num2, num3)
    print(*sorted_numbers)

if __name__ == "__main__":
    main()
