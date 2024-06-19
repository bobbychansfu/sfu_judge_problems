import math

def counting_formula(order, repeat, n, r):
    if order and repeat:
        return n ** r
    elif order and not repeat:
        return math.factorial(n) // math.factorial(n - r)
    elif not order and repeat:
        return math.factorial(n + r - 1) // (math.factorial(r) * math.factorial(n - 1))
    elif not order and not repeat:
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


def main():
    for _ in range(4):
        input_line = input().strip()
        order, repeat, n, r = input_line.split()
        order = order == 'True'
        repeat = repeat == 'True'
        n = int(n)
        r = int(r)
        print(counting_formula(order, repeat, n, r))

if __name__ == "__main__":
    main()
