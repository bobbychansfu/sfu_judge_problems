import math

def counting_formula(order, repeat, n, r):
    # your code here


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