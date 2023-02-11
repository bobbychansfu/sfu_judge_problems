w = int(input("width: "))
l = int(input("length: "))

print('='*(w+2))
for i in range(l):
	print('|'+'v'*(w)+'|')
print('='*(w+2))