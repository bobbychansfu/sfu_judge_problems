n, q = map(int, input().split())
print(n,q)
from random import randrange

for _ in range(q):
    t = randrange(2)
    if t:
        a = randrange(1, n+1)
        b = randrange(1, n+1)
        a, b = min(a, b), max(a, b)
        c = chr(65+randrange(26))
        print(f"p {a} {b} {c}")
    else:
        x = randrange(1, n+1)
        print(f"q {x}")