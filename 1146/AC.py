import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
Case 3 solution (Also valid for cases 1 and 2)

First construct a DAG based on the comparisons. If a topological order is impossible due to a cycle, return "NO".
Otherwise, return "YES" and count how many digits each digit has a higher/lower value than.
If this count of higher/lower combined should be 15, the digit has an exact value equal to the number of digits it has a higher value than.
Then for each hexadecimal decoding, return "?" if it contains a digit with an unknown value otherwise convert to decimal as expected.

Other notes:
Case 1 simply requires being able to convert the hexadecimal values into decimal.
Funny enough this can be done with int(s,16)

Case 2 can be done by brute force on the 6! = 720 possible configurations for the A,B,C,D,E,F digits. First keep
track of the configurations (if any) that are valid for all comparisons. Then decode each hexadecimal value according to
each valid encoding, and check if the unique value or "?" should be returned.
"""

class Node:
    def __init__(self):
        self.indeg = 0
        self.parents = {}
        self.children = {}
        self.searched = 0

basev = {"0":0,
     "1":1,
     "2":2,
     "3":3,
     "4":4,
     "5":5,
     "6":6,
     "7":7,
     "8":8,
     "9":9,
     "A":10,
     "B":11,
     "C":12,
     "D":13,
     "E":14,
     "F":15}

def evalComparison(a,b,sign): # assume a > b
    if sign == "<": return evalComparison(b,a,">")
    n = len(a)
    for i in range(n):
        if a[i] != b[i]: return a[i],b[i]
    return -1,-1

def resetSearchState(nodes):
    for i in range(16):
        nodes[i].searched = 0
        nodes[i].indeg = len(list(nodes[i].parents.keys()))

def determineAllHigher(nodes,i): # return a list of all nodes found in a dfs (except for self)
    nodes[i].searched = 1
    q = [i]
    ans = list()
    while len(q) != 0:
        x = q.pop()
        for j in nodes[x].children.keys():
            if nodes[j].searched == 0:
                ans.append(j)
                nodes[j].searched = 1
                q.append(j)
    return ans

def solution(comparisons,queries): # return string list for ans
    n,m = len(comparisons),len(queries)
    nodes = list()
    for _ in range(16):
        nodes.append(Node())

    # determine comparisons, create directed edges from lower values to higher values
    for c in comparisons:
        a,sign,b = c.split()
        higher,lower = evalComparison(a,b,sign)
        if higher == -1 and lower == -1: return ["NO"] # illegal comparison (equal values)
        hindex,lindex = basev[higher],basev[lower]
        nodes[lindex].children[hindex] = 1
        if nodes[hindex].parents.get(lindex) == None:
            nodes[hindex].parents[lindex] = 1
            nodes[hindex].indeg += 1

    # determine an arbritary topological sort, if it does not exist (because of a cycle) return NO
    topological_order = list()
    for i in range(16):
        if nodes[i].indeg == 0:
            topological_order.append(i)
    for i in range(16):
        if i == len(topological_order): return ["NO"] # there is a cycle, thus impossible
        x = topological_order[i]
        for j in nodes[x].children.keys():
            nodes[j].indeg -= 1
            if nodes[j].indeg == 0:
                topological_order.append(j)


    # a valid ordering does exist, determine which digits can have their exact values determined
    resetSearchState(nodes)
    ans = ["YES"]
    lowerthan = [0]*16
    higherthan = [0]*16
    for i in range(16):
        higherList = determineAllHigher(nodes,i)
        lowerthan[i] = len(higherList)
        for j in higherList:
            higherthan[j] += 1
        resetSearchState(nodes)

    translationList = list()
    for i in range(16):
        if lowerthan[i] + higherthan[i] == 15: translationList.append(higherthan[i])
        else: translationList.append("?")

    # translate the hexadecimal strings
    for q in queries:
        v = 0
        for digit in q:
            digitvalue = translationList[basev[digit]]
            if digitvalue == "?":
                v = -1
                break
            else:
                v *= 16
                v += digitvalue
        if v == -1: ans.append("?")
        else: ans.append(str(v))
    return ans


if __name__ == "__main__":
    n,m = readints()
    comparisons = list()
    for _ in range(n):
        comparisons.append(readin())
    queries = list()
    for _ in range(m):
        queries.append(readin())
    for line in solution(comparisons,queries):
        print(line)
    