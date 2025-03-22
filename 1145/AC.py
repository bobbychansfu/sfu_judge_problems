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

Sliding window for O(n) solution. There are other solutions that pass the easier testcases like starting on each char and only stopping once all chars are found,
or brute forcing each 26+ char substring.
"""


def solution(n,s):
    ans = 9999999999999999999999
    chars = [0]*26
    index = 0
    r = 26
    for i in range(n):
        inc = ord(s[i])-ord('a')
        chars[inc] += 1
        if chars[inc] == 1:
            r -= 1
        while r == 0 and index != n: # technically should never happen since the string must be at least 26 characters
            ans = min(ans,i-index)
            chars[ord(s[index])-ord('a')] -= 1
            if chars[ord(s[index])-ord('a')] == 0:
                r += 1
            index += 1
    if ans == 9999999999999999999999: return -1
    return ans-25

if __name__ == "__main__":
    n = readint()
    s = readin()
    print(solution(n,s))