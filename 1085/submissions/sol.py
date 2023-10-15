import sys
import bisect

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()

n, l, v, q = readints()
a = []

for i in range(n):
    x, s = input().split()
    x = int(x)

    if(s == "RIGHT"):
        x = (l - x)

    a.append(x / v)

a = sorted(a)

for i in range(q):
    idx = bisect.bisect_right(a, readint())

    print(n - idx)
