import sys
n_words = int(sys.argv[1])
n_qs = int(sys.argv[2])
valid_words = list(open('words.txt', 'r').read().split())
import random
ws = random.sample(valid_words, n_words)
print(n_qs)
print('\n'.join(ws))
