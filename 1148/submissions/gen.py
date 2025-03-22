from random import randint, choice
import sys
n = int(sys.argv[1])
k = int(sys.argv[2])

m = randint(n, min(n*(n-1)//2, 2e5))

edgeset = set()
adjlist = [[] for _ in range(n+1)]
for i in range(m):
    x = randint(1, n)
    y = randint(1, n)
    if x > y:
        x, y = y, x
    while (x, y) in edgeset or x == y:
        x = randint(1, n)
        y = randint(1, n)    
        if x > y:
            x, y = y, x
    edgeset.add((x, y))
    adjlist[x].append(y)
    adjlist[y].append(x)


hubset = set()
for i in range(k):
    x = randint(1, n)
    while x in hubset:
        x = randint(1, n)
    hubset.add(x)

# make sure each node is
# has a path to a hub
queue = list(hubset)
# bfs
visited = [False] * (n+1)
while queue:
    node = queue.pop(0)
    visited[node] = True
    for neighbor in adjlist[node]:
        if not visited[neighbor]:
            queue.append(neighbor)

for i in range(1, n+1):
    if not visited[i]:
        # if not connected to any hub
        # connect to a random hub
        
        x = choice(list(hubset))
        y = i 
        if x > y:
            x, y = y, x
        edgeset.add((x, y))
        m+=1

print(n, m, k)

maxcost = 1e9
for edge in edgeset:
    cost = randint(1, maxcost)
    print(edge[0], edge[1], cost)

print(*hubset)