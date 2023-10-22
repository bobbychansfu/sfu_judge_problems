def print_pattern(n,m):
    # Helper function to print a specific line
    def print_line(leading_spaces, stars, inner_spaces):
        print(' ' * leading_spaces + '*' * stars + ' ' * inner_spaces + '*' * stars)

    for j in range(m):
        # Top part of the pattern
        for i in range(n):
            print_line(n-i-1, i+1, 1)

        # Middle part of the pattern, stars decreasing
        for i in range(n-1, -1, -1):
            print_line(n-i-1, i+1, 1)


# Set the size of the pattern
n = 3
m = 2
# Print the pattern
print_pattern(n,m)
