import pickle
import sys

with open("mapping.txt", "rb") as f:
    m = pickle.loads(f.read())

out = ""

for line in sys.stdin:
    for char in line:
        if char in m:
            out += m[char]
        else:
            out += char

print(out)