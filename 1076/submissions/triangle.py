def print_pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()  # Move to the next line after printing numbers for each row

if __name__ == "__main__":
    n = int(input())
    print_pattern(n)

