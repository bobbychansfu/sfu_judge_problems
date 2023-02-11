d = int(input("d: "))
n = int(input("n: "))
t = 0

while (d>0):
	t += n
	n *= 2
	d -= 1
	
print(t/100)