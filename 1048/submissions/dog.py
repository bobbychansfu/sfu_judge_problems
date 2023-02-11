i = int(input("student: "))
d = 0
v = 0
m = 0
e = 0
while (i>=0):
	if (i%3==0):
		d += 1
	if (i%4==0):
		v += 1
	if (i%5==0):
		m += 1
	if (i%7==0):
		e += 1
	i = int(input("student: "))

print("dark arts:",d)
print("vision:",v)
print("mind reader:",m)
print("enchantment:",e)
