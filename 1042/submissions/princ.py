p = float(input("Please enter the principal: "))
y = float(input("Please enter the years: "))

r = 0
if (p >= 0 and p < 1000):
    r = 0.025
elif (p >= 1000 and p < 10000):
    r = 0.02
elif (p >= 10000 and p < 100000):
    r = 0.015
elif (p >= 100000):
    r = 0.01

if (p<0 or y<0):
    print("not possible")
else:
    print(round(p*(1.0+r*y),2))