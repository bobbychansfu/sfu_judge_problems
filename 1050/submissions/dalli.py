def isDallidrum(s):
	s = str(s)
	i = 0
	j = len(s) - 1
	while i < j:
		if s[i] != s[j]:
			return False
		i = i + 1
		j = j - 1
	return True
 
 
def main():
	s = int(input())
	if isDallidrum(s):
		print('Yes')
	else:
		print('No')

main()