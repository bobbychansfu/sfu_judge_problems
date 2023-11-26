def calculate_happiness():
    # Reading the first line: number of stones and size of each scroll
    n, m = map(int, input().split())

    # Reading the second line: integers on the stones
    stones = list(map(int, input().split()))

    # Reading the third and fourth lines: integers on the 'Joy' and 'Sorrow' scrolls
    joy_scroll = set(map(int, input().split()))
    sorrow_scroll = set(map(int, input().split()))

    # Initial happiness
    happiness = 0

    # Calculating happiness
    for stone in stones:
        if stone in joy_scroll:
            happiness += 1
        elif stone in sorrow_scroll:
            happiness -= 1

    return happiness

# Running the function and printing the result
final_happiness = calculate_happiness()
print(final_happiness)
