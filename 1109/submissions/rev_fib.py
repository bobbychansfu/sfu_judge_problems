def fibonacci(n):
    """
    Recursive function to find the nth Fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_reverse(n):
    """
    Function to print the first n Fibonacci numbers in reverse order
    """
    fib_sequence = [fibonacci(i) for i in range(n)]
    for num in reversed(fib_sequence):
        print(num, end=' ')
    print()

# Example usage
N = int(input())
print_fibonacci_reverse(N)

