# intended solution setup using sieve, other methods using brute force with careful palindrome construction 
# are also possible and may be more character efficient.
# if you want to get really troll then you can also manually store the entire list of paliguprimes here


def all_paliguprimes(): # helper to generate all paliguprimes up to 1500000
    ar = [True]*1500001
    ar[0] = False
    ar[1] = False
    for i in range(2,1230):
        if ar[i]: #i is prime
            for j in range(i,1500000//i+1):
                ar[i*j] = False
    paliguprimes = list()
    for i in range(10,1500001):
        if ar[i]: # prime, check palindrome
            x = str(i//10)
            flag = True
            for j in range(len(x)//2):
                if x[j] != x[-j-1]:
                    flag = False
                    break
            if flag: paliguprimes.append(i)
    return paliguprimes

primes = all_paliguprimes()

def solution(n,ar,primes):
    ans = 0
    for i in ar:
        low = 0
        high = len(primes)-1
        while high-low > 1:
            mid = (low+high)//2
            if i == primes[mid]: # number is a paliguprime, break and return 0
                high = mid
                break
            elif i > primes[mid]: low = mid
            else: high = mid
        ans += min(abs(primes[low]-i),abs(primes[high]-i))
    return ans


if __name__ == "__main__":
    n = int(input())
    ar = list(map(int,input().split()))
    print(solution(n,ar,primes))