import sys
from copy import deepcopy
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Answer spoilers below:













The priority for obtaining digits is as follows:
1. get as many digits as possible
2. get as many 9s as possible
3. get as many 8s as possible
... (repeat with 7,6,5,4,3,2,1)

Condition 1 means we can use a 2-way prefix sum setup for even length arrays
to efficiently compare all possibilities. For odd length, it's either taking
all even indices or if all of the even indices are 0 then taking all odd indices.
"""

def compare(ar,br): # return array with higher digits
    for i in range(9,-1,-1):
        if ar[i] > br[i]: return ar
        if br[i] > ar[i]: return br
    return ar # tie

def solve(n,ar):
    odd = list()
    even = list()
    for i in range(n):
        if i % 2 == 0: even.append(ar[i])
        else: odd.append(ar[i])

    if n % 2 == 1: # odd case
        # either take all even indices or if they're all 0, take all odd indices
        if even.count(0) == len(even):
            if odd.count(0) == len(odd):
                print(0)
                return
            odd.sort()
            odd.reverse()
            print(*odd,sep="")
            return
        even.sort()
        even.reverse()
        print(*even,sep="")
        return

    # even case, create subarray counters
    counter = [0]*10
    left = [deepcopy(counter)] # prefix of even indices from left to right
    for i in range(n//2):
        counter[even[i]] += 1
        left.append(deepcopy(counter))

    counter = [0]*10
    right = [deepcopy(counter)] # prefix of odd indices from right to left
    for i in range(n//2):
        counter[odd[-i-1]] += 1
        right.append(deepcopy(counter))

    ansfreq = compare(left[-1],right[-1])
    for i in range(1,len(left)-1):
        combined = list()
        for j in range(10):
            combined.append(left[n//2-i][j]+right[i][j])
        ansfreq = compare(ansfreq,combined)
    ansl = list()
    for k in range(9,-1,-1):
        for _ in range(ansfreq[k]):
            ansl.append(k)
    print(*ansl,sep="")

if __name__ == "__main__":
    n = readint()
    ar = list(map(int, list(input()))) # list of plants
    solve(n,ar)