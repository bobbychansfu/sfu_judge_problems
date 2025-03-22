from random import randrange

n = randrange(2000, 100000)

s = ''.join([chr(ord('1') + randrange(9)) for _ in range(n)])

print(n)
print(s)