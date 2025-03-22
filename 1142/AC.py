# intended solution setup using sieve, other methods using brute force with careful palindrome construction 
# are also possible and may be more character efficient.
# if you want to get really troll then you can also manually store the entire list of paliguprimes here


def all_paliguprimes(): # helper to generate all paliguprimes up to 1300000
    ar = [True]*1300001
    ar[0] = False
    ar[1] = False
    for i in range(3,1145,2):
        if ar[i]: #i is prime
            for j in range(i,1300000//i+1):
                ar[i*j] = False
    pallist = list()
    # now construct only the palindrome values that actually need to be checked
    for i in range(1,1000):
        s = str(i)
        t = s[::-1]
        v = int(s+t[1:])
        pallist.append(v*10+1)
        pallist.append(v*10+3)
        pallist.append(v*10+7)
        pallist.append(v*10+9)
        v = int(s+t)
        pallist.append(v*10+1)
        pallist.append(v*10+3)
        pallist.append(v*10+7)
        pallist.append(v*10+9)
    
    pallist.sort()
    paliguprimes = list()
    for p in pallist:
        if p > 1300000: break
        if ar[p]:
            paliguprimes.append(p)
    return paliguprimes

primes = all_paliguprimes()

def solution(n,ar,primes): # Update: binary search is actually not needed as two pointer can be used
    ans = 0
    ar.sort()
    ptr = 1
    for i in ar:
        while primes[ptr] < i:
            ptr += 1
        ans += min(abs(primes[ptr]-i),abs(primes[ptr-1]-i))
    return ans


if __name__ == "__main__":
    n = int(input())
    ar = list(map(int,input().split()))
    print(solution(n,ar,primes))