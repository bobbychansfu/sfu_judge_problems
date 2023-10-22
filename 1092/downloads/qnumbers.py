def order(a, b, c):
    # fill in this function

def main():
    num1, num2, num3 = tuple(map(int, input().split(" ")))
    sorted_numbers = order(num1, num2, num3)
    print(*sorted_numbers)

if __name__ == "__main__":
    main()
