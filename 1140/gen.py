from AC import solution
from random import randint
import time


def generateExtensive(): # create all up to n = 20 (210 cases)
    infile = open("extensive.in","w")
    outfile = open("extensive.out","w")
    infile.write("230\n")
    for i in range(1,21):
        for j in range(i+1):
            infile.write(str(i)+" "+str(j)+"\n")
            ans = solution(i,j)
            outfile.write(str(ans)+"\n")
    infile.close()
    outfile.close()

def generateRandom(maxN,iv): # generate 256 instances with n being up to a certain value (limit k to half of n)
    infile = open(str(iv)+"random"+str(maxN)+".in","w")
    outfile = open(str(iv)+"random"+str(maxN)+".out","w")
    infile.write(str(256)+"\n")
    for _ in range(256):
        n = randint(1,maxN)
        k = randint(0,n//2)
        infile.write(str(n)+" "+str(k)+"\n")
        ans = solution(n,k)
        outfile.write(str(ans)+"\n")
    infile.close()
    outfile.close()

if __name__ == "__main__":
    #generateExtensive()
    for ii in range(10):
        generateRandom(8501936885,ii)