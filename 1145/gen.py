from AC import solution
from random import randint,shuffle
import time


def generatePossible(n,s): # create n instances that are solvable with length s
    for i in range(n):
        infile = open("possible"+str(i)+"-"+str(s)+".in","w")
        outfile = open("possible"+str(i)+"-"+str(s)+".out","w")
        infile.write(str(s)+"\n")
        # create charlist
        ar = list()
        for j in range(26):
            ar.append(chr(j+97))
        for _ in range(s-26):
            ar.append(chr(97+randint(0,25)))
        shuffle(ar)
        st = "".join(ar)
        infile.write(st+"\n")
        ans = solution(s,st)
        outfile.write(str(ans)+"\n")
        infile.close()
        outfile.close()

def generateImpossible(n,s): # create n instances that are not solvable with length s
    nope = randint(0,25)
    for i in range(n):
        infile = open("impossible"+str(i)+"-"+str(s)+".in","w")
        outfile = open("impossible"+str(i)+"-"+str(s)+".out","w")
        infile.write(str(s)+"\n")
        # create charlist
        ar = list()
        for j in range(26):
            if j != nope: ar.append(chr(j+97))
        while len(ar) != s:
            x = randint(0,25)
            if x != nope: ar.append(chr(97+x))
        shuffle(ar)
        st = "".join(ar)
        infile.write(st+"\n")
        ans = solution(s,st)
        outfile.write(str(ans)+"\n")
        infile.close()
        outfile.close()

def generateRandom(n,s): # create n instances that are solvable with length s
    for i in range(n):
        infile = open("random"+str(i)+"-"+str(s)+".in","w")
        outfile = open("random"+str(i)+"-"+str(s)+".out","w")
        infile.write(str(s)+"\n")
        # create charlist
        ar = list()
        for _ in range(s):
            ar.append(chr(97+randint(0,25)))
        shuffle(ar)
        st = "".join(ar)
        infile.write(st+"\n")
        ans = solution(s,st)
        outfile.write(str(ans)+"\n")
        infile.close()
        outfile.close()

if __name__ == "__main__":
    f = 10 # frequency
    l = 520000 # length
    generatePossible(f,l)
    generateImpossible(f,l)
    generateRandom(f,l)