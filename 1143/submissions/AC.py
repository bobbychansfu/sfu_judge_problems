import sys
from heapq import *
#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

"""
sample test case
        2
        6
        0 0 0 2
        0 2 2 0
        2 0 2 2
        0 0 2 2
        0 0 1 -1
        2 0 1 -1
        1
        0 0 448 840

solution below uses a dijsktra to find the shortest path from the end
of the last edge to the start of the next edge, and distances are straight lines
(then use pythagoras)
"""

class Node:
    def __init__(self):
        self.edges = {}
        self.distance = -1

def pythag(x1,y1,x2,y2):
    return (abs(x1-x2)**2+abs(y1-y2)**2)**0.5

def dijkstra(nodes,px,py,sx,sy): # compute distance from px,py to sx,sy
    nodes[(px,py)].distance = 0
    q = [(0,px,py)]
    while len(q) != 0:
        x = heappop(q)
        d = x[0]
        a,b = x[1],x[2]
        if a == sx and b == sy:
            # revert all nodes to -1
            for e in nodes.keys():
                nodes[e].distance = -1
            return d
        for nn in nodes[(a,b)].edges.keys():
            if nodes[nn].distance == -1:
                nodes[nn].distance = nodes[(a,b)].edges[nn]+d
                heappush(q,(nodes[(a,b)].edges[nn]+d,nn[0],nn[1]))

def solve(n,lines): # solution for a single sigil
    nodes = {}
    # create first two nodes for the first line
    nodes[(lines[0][0],lines[0][1])] = Node()
    nodes[(lines[0][2],lines[0][3])] = Node()
    ans = pythag(lines[0][0],lines[0][1],lines[0][2],lines[0][3])
    nodes[(lines[0][0],lines[0][1])].edges[(lines[0][2],lines[0][3])] = ans
    nodes[(lines[0][2],lines[0][3])].edges[(lines[0][0],lines[0][1])] = ans
    px,py = lines[0][2],lines[0][3] # position where brush is
    for l in range(1,n):
        sx,sy,ex,ey = lines[l][0],lines[l][1],lines[l][2],lines[l][3]
        # move from px,py to sx,sy
        ans += dijkstra(nodes,px,py,sx,sy)
        # add line distance
        linedist = pythag(sx,sy,ex,ey)
        ans += linedist
        # add the edge into the graph
        if nodes.get((ex,ey)) == None: nodes[(ex,ey)] = Node()
        nodes[(sx,sy)].edges[(ex,ey)] = linedist
        nodes[(ex,ey)].edges[(sx,sy)] = linedist
        # adjust px,py
        px,py = ex,ey

    return ans

def solution(n,cases):
    ans = list()
    for i in range(n):
        ans.append(solve(len(cases[i]),cases[i]))
    return ans

if __name__ == "__main__":
    n = readint()
    cases = list()
    for _ in range(n):
        ptlist = list()
        for _ in range(readint()):
            a,b,c,d = readints()
            ptlist.append((a,b,c,d)) # go from (a,b) to (c,d)
        cases.append(ptlist)
    for i in solution(n,cases):
        print(i)
