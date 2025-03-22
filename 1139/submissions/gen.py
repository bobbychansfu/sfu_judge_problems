from random import randint
import sys
n = int(sys.argv[1])
k = int(sys.argv[2])

n = randint(2, n)
k = randint(1, min(n-1, k))

if len(sys.argv) > 3:
    maxn = int(sys.argv[3])
else: maxn = 1e9
a = [randint(1, maxn) for _ in range(n)]
print(n, k)
print(*a)