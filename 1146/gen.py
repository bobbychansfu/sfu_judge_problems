from AC import solution
from random import randint,shuffle
from math import gcd
import time

digits = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

# NOTE: for creating situations where only some digits may have definied values could use a ranking system, this also makes a lot of other cases a lot easier

def buildComparison(a,b): # create two 15 digit values for comparison
    # digit a is assumed to be lower than digit b
    stra = ""
    strb = ""
    comparedigit = randint(0,14)
    for i in range(15):
        if i == comparedigit:
            stra += a
            strb += b
        else:
            x = digits[randint(0,15)]
            stra += x
            strb += x
    if randint(0,1) == 0: return stra+" < "+strb
    else: return strb+" > "+stra

# comparisons generators

def noshuffleGenerator(): # onlyhexadecode
    comparisons = list()
    for i in range(15):
        comparisons.append(digits[i]+" < "+digits[i+1])
    return comparisons

def createBaseComparisons(): # use for sixscramble cases
    comparisons = list()
    for i in range(15):
        comparisons.append(digits[min(i,9)]+" < "+digits[i+1])
    return comparisons

def sixFullGenerator(): # sixscramble, all digits have an exact value
    comparisons = createBaseComparisons()
    indices = [10,11,12,13,14,15]
    shuffle(indices)
    # digits[indices[i]] = i+10

    for i in range(5):
        comparisons.append(buildComparison(digits[indices[i]],digits[indices[i+1]]))

    # add a few arbritary connections
    for _ in range(3):
        x = randint(0,5)
        y = x
        while y == x:
            y = randint(0,5)
        if x < y: comparisons.append(buildComparison(digits[indices[x]],digits[indices[y]]))
        else: comparisons.append(buildComparison(digits[indices[y]],digits[indices[x]]))
        
    shuffle(comparisons)

    return comparisons

def sixPartialGenerator(): # sixscramble but arbritarily choose two digits to be unknown
    comparisons = createBaseComparisons()
    ranks = [1,2,3,4,5,randint(1,5)]
    shuffle(ranks)
    d = {}
    letters = ["A","B","C","D","E","F"]
    for i in range(6):
        if d.get(ranks[i]) == None: d[ranks[i]] = list()
        d[ranks[i]].append(letters[i])
    for i in range(1,5):
        for a in d[i]:
            for b in d[i+1]:
                comparisons.append(buildComparison(a,b))
    
    for _ in range(2):
        x = randint(1,5)
        y = x
        while y == x:
            y = randint(1,5)
        if x < y: comparisons.append(buildComparison(d[x][0],d[y][0]))
        else: comparisons.append(buildComparison(d[y][0],d[x][0]))
    
    shuffle(comparisons)

    return comparisons

def sixIllegalGenerator(): # sixscramble but there must be at least one error somewhere 
    comparisons = createBaseComparisons()
    indices = [10,11,12,13,14,15]
    shuffle(indices)
    # digits[indices[i]] = i+10

    for i in range(5):
        comparisons.append(buildComparison(digits[indices[i]],digits[indices[i+1]]))

    # add a few arbritary connections
    for _ in range(2):
        x = randint(0,5)
        y = x
        while y == x:
            y = randint(0,5)
        if x < y: comparisons.append(buildComparison(digits[indices[x]],digits[indices[y]]))
        else: comparisons.append(buildComparison(digits[indices[y]],digits[indices[x]]))
        
    # illegal move
    comparisons.append(buildComparison(digits[indices[4]],digits[indices[2]]))

    shuffle(comparisons)

    return comparisons

def perfectGenerator(addedhelp=10,divisions=16): # all digits have a definied value, give minimal information
    comparisons = list()
    rankcount = divisions
    ranks = list()
    for i in range(1,rankcount+1):
        ranks.append(i)
    while len(ranks) != 16:
        ranks.append(randint(1,rankcount))
    shuffle(ranks)
    d = {}
    for i in range(16):
        if d.get(ranks[i]) == None: d[ranks[i]] = list()
        d[ranks[i]].append(digits[i])
    for i in range(1,rankcount):
        for a in d[i]:
            for b in d[i+1]:
                comparisons.append(buildComparison(a,b))
    
    for _ in range(addedhelp):
        x = randint(1,rankcount)
        y = x
        while y == x:
            y = randint(1,rankcount)
        if x < y: comparisons.append(buildComparison(d[x][randint(0,len(d[x])-1)],d[y][randint(0,len(d[y])-1)]))
        else: comparisons.append(buildComparison(d[y][randint(0,len(d[y])-1)],d[x][randint(0,len(d[x])-1)]))
    
    shuffle(comparisons)

    return comparisons


def randomGenerator(c): # generate some arbritary number of comparisons, very likely to self contradict
    comparisons = list()
    for _ in range(c):
        x = randint(0,15)
        y = x
        while y == x:
            y = randint(0,15)
        comparisons.append(buildComparison(digits[x],digits[y]))
    return comparisons

def generateQueries(r):
    queries = list()
    
    # create ALL 1-digit queries
    for d in digits:
        queries.append(d)

    # create ALL 2-digit queries
    for a in digits:
        for b in digits:
            queries.append(a+b)

    # then just fill in the rest with arbritary 15 digit queries
    for _ in range(r):
        s = ""
        for _ in range(15):
            s += digits[randint(0,15)]
        queries.append(s)

    # and also add in 448 because I need to put in a Lucario joke somewhere
    queries.append("448")
    
    shuffle(queries)
    
    return queries

def write_case(comparisons,queries,filename):
    st = time.time()
    ans = solution(comparisons,queries) # return str list of answers
    ed = time.time()
    print("Case",filename,"took",str(round(ed-st,3)),"seconds")
    
    #input file

    f = open(filename+".in","w")
    f.write(str(len(comparisons))+" "+str(len(queries))+"\n")
    for c in comparisons:
        f.write(c+"\n")
    for q in queries:
        f.write(q+"\n")
    f.close()

    #output file

    f = open(filename+".out","w")
    for a in range(len(ans)):
        f.write(ans[a])
        if a+1 != len(ans): f.write("\n")
    f.close()

if __name__ == "__main__":
    
    # solve each case

    # comparisons = noshuffleGenerator()
    # write_case(comparisons,generateQueries(727),"hexadecimaltranslation") # this will make exactly 1000 cases XD
    

    #for i in range(5):
        #write_case(sixFullGenerator(),generateQueries(727),"perfect"+str(i))
        #write_case(sixPartialGenerator(),generateQueries(727),"partial"+str(i))
        #write_case(sixIllegalGenerator(),generateQueries(727),"error"+str(i))
        #write_case(perfectGenerator(10,16),generateQueries(727),"perfect"+str(i))
        #write_case(perfectGenerator(10,15),generateQueries(727),"14known"+str(i))
        #write_case(sixFullGenerator(),generateQueries(727),"perfectLarge"+str(i))
        #write_case(perfectGenerator(1985,16),generateQueries(727),"perfectLarge"+str(i))
        #write_case(perfectGenerator(1985,15),generateQueries(727),"14knownLarge"+str(i))
        #write_case(perfectGenerator(i**5,9),generateQueries(727),"minimalinfo"+str(i))
    i = 1
    while i < 2000:   
        write_case(randomGenerator(i),generateQueries(727),"random"+str(i))
        i *= 2