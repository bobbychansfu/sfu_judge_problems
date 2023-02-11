x = int(input("x: "))
y = int(input("y: "))
a = min(x,y)
b = max(x,y)
for i in range(a,b+1):
    if (i%4==1):
        print(i,end=" ")
print()