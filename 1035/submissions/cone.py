r = float(input("Please enter r: "))
h = float(input("Please enter h: "))

if r<=0:
    print(round(float(0),2))
else:
    ans = (1/3)*r**2*h*3.14
    print(round(ans,2))

