def get_divisors_sum(n):
    """Return the sum of divisors of n, excluding n itself."""
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid adding the same divisor twice for perfect squares
                divisors_sum += n // i
    return divisors_sum

def find_perfect_numbers(a, b):
    """Return a list of perfect numbers between a and b, inclusive."""
    return [num for num in range(a, b+1) if num == get_divisors_sum(num) and num != 1]

if __name__ == "__main__":
    a, b = map(int, input().split())
    perfect_numbers = find_perfect_numbers(a, b)
    
    if perfect_numbers:
        print(" ".join(map(str, perfect_numbers)))
    else:
        print("-1")
