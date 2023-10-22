
def geom(a,b):
    c1,c2=0,0
    for z in range(b):
    
        for x in range(a):
            #print(x,a-x)
            c1=c1+x+(a-x)
        for y in range(a,0,-1):
            #print(y,a-y)
            c2=c2+y+(a-y)
    zz=c1+c2
    return zz

a,b = tuple(map(int,input().split(" ")))
for z in range(b):
    
    for x in range(a):
        print("*"*x , " " , "*"*(a-x))
    
    for y in range(a,0,-1):
        print("*"*y , " " , "*"*(a-y))

        
# print(geom(a,b)*5)