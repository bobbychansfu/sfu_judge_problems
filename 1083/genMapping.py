import string
import random
import pickle

letters = list(string.ascii_uppercase)
newLetters = list(string.ascii_uppercase)
random.shuffle(newLetters)

letters += string.punctuation
newLetters += string.punctuation

m = dict(zip(letters, newLetters))
m[' '] = ' '
m['\n'] = '\n'

with open("mapping.txt", "wb") as f:
    f.write(pickle.dumps(m))

print(m)