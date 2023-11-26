def find_nth_number(n):
    # Base cases
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 2

    # Recursive call
    return find_nth_number(n-1) + find_nth_number(n-2) + find_nth_number(n-3)

# Example usage
n = int(input())
print(find_nth_number(n))
