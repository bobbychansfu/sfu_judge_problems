import sys, random

n, m, k = map(int, sys.argv[1:4])
print(n, m, k)
E = []
edges = set()
for _ in range(m):
	a, b = 0, 0
	while a == b or (a, b) in edges:
		a, b = random.randrange(1, n+1), random.randrange(1, n+1)
		a, b = sorted((a, b))
	E.append((a,b))
	edges.add((a,b))
print('\n'.join([' '.join([str(a) for a in e]) for e in E]))

Qs = []
for _ in range(k):
	t = 0
	while t not in [1, 3]:
		t = random.randrange(1, 4)
	if t == 1:
		a, b = 0, 0
		while a == b or (a, b) in edges:
			a, b = random.randrange(1, n+1), random.randrange(1, n+1)
			a, b = sorted((a, b))
		edges.add((a,b))
		Qs.append((1, a, b))
	if t == 2:
		a, b = random.sample(list(edges), 1)[0]
		edges.remove((a,b))
		Qs.append((2, a, b))
	if t == 3:
		a, b = 0, 0
		while a == b:
			a, b = random.randrange(1, n+1), random.randrange(1, n+1)
		Qs.append((3, a, b))
print('\n'.join([' '.join([str(a) for a in q]) for q in Qs]))
