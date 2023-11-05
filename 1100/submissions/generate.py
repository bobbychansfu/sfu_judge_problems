import random
choices = [0,11,12,13]
greater = [13,14,15,16,17]
n = int(input())
eggs = []
for _ in range(n):
    r = random.choice(choices)
    if (r == 13):
        r = random.choice(greater)
    eggs.append(r)
print(*eggs)