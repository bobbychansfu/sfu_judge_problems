def prime_factors_sum(n):
    i = 2
    sum_factors = 0
    while i * i <= n:
        while (n % i) == 0:
            sum_factors += i
            n //= i
        i += 1
    if n > 1:
        sum_factors += n
    return sum_factors

def john_and_mia_game(a, b):
    sum_a = prime_factors_sum(a)
    sum_b = prime_factors_sum(b)
    if sum_a == sum_b:
        return "Win"
    else:
        return "Lose"

# Read input
a, b = map(int, input().strip().split())

# Get result
result = john_and_mia_game(a, b)

# Print result
print(result)
