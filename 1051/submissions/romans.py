def romanToInts(s):
	ROMANS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # Variable for accumulating total
	number = 0
        
        # Process all characters except the last one
	for i in range(len(s) - 1):
		if ROMANS[s[i + 1]]  > ROMANS[s[i]]:
			number -= ROMANS[s[i]]
		else:
			number += ROMANS[s[i]]
		        
        # Process last character
	number += ROMANS[s[len(s) - 1]]
	
	return number

def main():
	s = input()
	print(romanToInts(s))

main()