a = int(input())

print(' '*(a-1)+'>')
print(' '*(a-1)+'|')
print(' '*(a-1)+'.')
for i in range(1,a):
	print(' '*(a-1-i)+'/'+'.'*i+'.'*(i-1)+'\\')