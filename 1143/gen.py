from AC import solution
from random import randint
from math import gcd
import time

def colinear(ax,ay,bx,by,cx,cy):
    if ax == bx:
        return ax == cx
    if ay == by:
        return ay == cy
    # do some sort of slope bs i guess
    x = bx-ax
    y = by-ay
    g = gcd(x,y)
    x //= g
    y //= g
    if (cx-ax) % x != 0 or (cy-ay) % y != 0: return False
    return (cx-ax)//x == (cy-ay)//y

def generatePoints(n,r): # generate n points on 2d grid with coordiantes at most abs(r)
    pts = list()
    failcount = 0
    while len(pts) != n:
        x,y = randint(-r,r),randint(-r,r)
        flag = True
        for a in range(len(pts)-1):
            for b in range(len(pts)-2):
                if colinear(pts[a][0],pts[a][1],pts[b][0],pts[b][1],x,y):
                    flag = False
                    break
            if not flag: break
        if flag: 
            pts.append((x,y))
            failcount = 0
        else:
            failcount += 1
            if failcount > 1000:
                raise ValueError("The range of values is too small and self destructed the anti-colinear generator")
    return pts

def generatePoints2(n,r):
    assert r >= (2*n)
    mod = 60000000000013
    for failcount in range(1,101): # number of attempts
        pts = list()
        d = {}
        while len(pts) != n:
            x,y = randint(-r,r),randint(-r,r)
            if d.get((x,y)) == None: 
                d[(x,y)] = 1
                pts.append((x,y))
        flag = True
        #print("running check")
        # now check for system crashes.exe
        for a in range(n-1):
            slopes = {}
            for b in range(a,n):
                xdiff,ydiff = pts[a][0]-pts[b][0],pts[a][1]-pts[b][1]
                h = 0
                if ydiff == 0: # 0 slope case
                    h = pts[a][1]+10000000000000000000
                elif xdiff == 0: # -1 slope case
                    h = pts[a][0]-10000000000000000000
                else: # ah screw it
                    h = (ydiff*(pow(xdiff,mod-2,mod))) % mod
                if slopes.get(h) != None:
                    flag = False
                    break
                slopes[h] = 1
            if not flag: break
        if flag:
            return pts
        else:
            print("rest in pepperoni")
        if failcount % 10 == 0:
            print("warning: failcount has reached",failcount)
    raise ValueError("Monkey search failed, expand range")

def createsigiltree(pts): # given a series of points, create a sigil
    ar = [(pts[0][0],pts[0][1],pts[1][0],pts[1][1])]
    for i in range(2,len(pts)):
        x = randint(0,i-1)
        ar.append((pts[x][0],pts[x][1],pts[i][0],pts[i][1]))
    return ar

def genTreeCases(n,testcount,ptcount,r,filename): # ptcount is edge count
    for i in range(1,n+1):
        # generate input and output
        sigils = list()
        for _ in range(testcount):
            sigils.append(createsigiltree(generatePoints2(ptcount+1,r)))
        #print("now solving big case",i)
        #st = time.time()
        ans = solution(testcount,sigils)
        #ed = time.time()
        #print("done solving big case",i)
        #print(ed-st,"seconds taken")
        f = open(filename+str(i)+".in","w")
        f.write(str(testcount)+"\n")
        for j in range(testcount):
            f.write(str(ptcount)+"\n")
            for k in range(ptcount):
                f.write(str(sigils[j][k][0])+" "
                        +str(sigils[j][k][1])+" "
                        +str(sigils[j][k][2])+" "
                        +str(sigils[j][k][3])+"\n")
        f.close()
        f = open(filename+str(i)+".out","w")
        for u in range(len(ans)):
            f.write(str(ans[u]))
            if u+1 != len(ans): f.write("\n")
        f.close()
        
def createstraightpath(pts):
    ar = list()
    for i in range(len(pts)-1):
        ar.append((pts[i][0],pts[i][1],pts[i+1][0],pts[i+1][1]))
    return ar

def genLineCases(n,testcount,ptcount,r,filename): # ptcount is edge count
    for i in range(1,n+1):
        # generate input and output
        sigils = list()
        for _ in range(testcount):
            sigils.append(createstraightpath(generatePoints2(ptcount+1,r)))
        print("now solving big case",i)
        st = time.time()
        ans = solution(testcount,sigils)
        ed = time.time()
        print("done solving big case",i)
        print(ed-st,"seconds taken")
        f = open(filename+str(i)+".in","w")
        f.write(str(testcount)+"\n")
        for j in range(testcount):
            f.write(str(ptcount)+"\n")
            for k in range(ptcount):
                f.write(str(sigils[j][k][0])+" "
                        +str(sigils[j][k][1])+" "
                        +str(sigils[j][k][2])+" "
                        +str(sigils[j][k][3])+"\n")
        f.close()
        f = open(filename+str(i)+".out","w")
        for u in range(len(ans)):
            f.write(str(ans[u]))
            if u+1 != len(ans): f.write("\n")
        f.close()
        
class Node:
    def __init__(self):
        self.edges = {}

def createdensegraph(edgecount,pts):
    n = len(pts)-1
    connected = [0]*n
    nodes = {}
    for i in pts:
        nodes[i] = Node()
    edgelist = list()
    # create first edge
    x = randint(0,n-1)
    y = x
    while y == x:
        y = randint(0,n-1)
    connected[x] = 1
    connected[y] = 1
    nodes[pts[x]].edges[pts[y]] = 1
    nodes[pts[y]].edges[pts[x]] = 1
    edgelist.append((pts[x][0],pts[x][1],pts[y][0],pts[y][1]))

    # build remaining edges
    remainingedges = edgecount - 1
    while remainingedges != 0:
        x = randint(0,n-1)
        y = randint(0,n-1)
        if x != y and connected[x] == 1 and nodes[pts[x]].edges.get(pts[y]) == None:
            nodes[pts[x]].edges[pts[y]] = 1
            nodes[pts[y]].edges[pts[x]] = 1
            edgelist.append((pts[x][0],pts[x][1],pts[y][0],pts[y][1]))
            connected[y] = 1
            remainingedges -= 1

    return edgelist


def genGraphCases(n,testcount,edgecount,r,filename): # less nodes but edges can go wherever
    for i in range(1,n+1):
        # generate input and output
        sigils = list()
        for _ in range(testcount):
            sigils.append(createdensegraph(edgecount,generatePoints2(randint(edgecount//4,edgecount//3),r)))
        print("now solving big case",i)
        st = time.time()
        ans = solution(testcount,sigils)
        ed = time.time()
        print("done solving big case",i)
        print(ed-st,"seconds taken")
        f = open(filename+str(i)+".in","w")
        f.write(str(testcount)+"\n")
        for j in range(testcount):
            f.write(str(edgecount)+"\n")
            for k in range(edgecount):
                f.write(str(sigils[j][k][0])+" "
                        +str(sigils[j][k][1])+" "
                        +str(sigils[j][k][2])+" "
                        +str(sigils[j][k][3])+"\n")
        f.close()
        f = open(filename+str(i)+".out","w")
        for u in range(len(ans)):
            f.write(str(ans[u]))
            if u+1 != len(ans): f.write("\n")
        f.close()

if __name__ == "__main__":
    #print(colinear(7,6,5,9,1,15))
    #print(colinear(7,6,5,9,19,15))
    
    #print(generatePoints2(300,100000))
    genGraphCases(5,1,2000,1000000,"largegraph")