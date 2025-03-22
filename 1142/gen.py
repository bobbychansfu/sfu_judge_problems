from AC import solution
from random import randint
import time


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


def random(runs,primes,count=255523): # generate runs of random values
    for i in range(1,runs+1):
        ar = list()
        for j in range(count):
            ar.append(randint(1,1234567))
        st = time.time()
        ans = solution(count,ar,primes)
        ed = time.time()
        print(ed-st)
        f = open("random"+str(i)+"-"+str(count)+".in","w")
        f.write(str(count)+"\n")
        for snth in ar:
            f.write(str(snth)+" ")
        f.close()
        f = open("random"+str(i)+"-"+str(count)+".out","w")
        f.write(str(ans))
        f.close()

def iterate(primes): # 5 tests to brute force every value
    ar = [list(),list(),list(),list(),list()]
    for i in range(1,1234568):
        ar[i%5].append(i)
    for a in range(5): # time check for sanity
        start = time.time()
        ans = solution(len(ar[a]),ar[a],primes)
        end = time.time()
        print(end-start)
        f = open("exhaustive"+str(a+1)+".in","w")
        f.write(str(len(ar[a]))+"\n")
        for snth in ar[a]:
            f.write(str(snth)+" ")
        f.close()
        f = open("exhaustive"+str(a+1)+".out","w")
        f.write(str(ans))
        f.close()

if __name__ == "__main__":
    st = time.time()
    ar = all_paliguprimes() # 996 total paliguprimes, takes about 0.3 seconds
    ed = time.time()
    print("Prime array generation time:")
    print(ed-st)
    #while ar[-1] > 1234567:
    #    ar.pop()
    #print(len(ar))
    #print(*ar)
    #random(11,ar,23)
    #iterate(ar)
    random(5,ar,599959)