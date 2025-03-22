import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Solution:

The players receiving 1st and 2nd round byes can be thought of as taking up 2 or 4 slots
respectively in the bracket. There is some mathematical proof to show that if a valid bracket
exists, only one possible bracket size can be viable. Thus, find this size by multiplying by 2 until
the slot count exceeds the minimal number of slots needed (by assuming everyone without a second round bye 
has no bye). Let x be the number of slots - k*4, then the remaining
n-k players must fill in the remaining x slots. Then x-n-k players must receive a first round bye; assuming
this value is inbetween 0 and n-k-1 inclusive, this is a valid bracket.

For the first subtest (64 points), you can use brute force to find the correct format. This also does not 
require using long integer value.
"""


def solution(n,k):
    minslots = n+k*3
    slotcount = 1
    while slotcount < minslots:
        slotcount *= 2
    x = slotcount-k*4
    remainingplayers = n-k
    ans = x-remainingplayers
    if 0 <= ans < remainingplayers: return ans
    return -1


if __name__ == "__main__":
    for _ in range(readint()):
        n,k = readints()
        print(solution(n,k))