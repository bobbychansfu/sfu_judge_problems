def reversedInteger(number):
    if number >= 0:
        # For non-negative numbers, convert to string, reverse the string and convert back to integer.
        return int(str(number)[::-1])
    else:
        # For negative numbers, convert to string (excluding the '-' sign), reverse the string,
        # convert back to integer and then make it negative.
        return -int(str(number)[:0:-1])

def main():
	s = int(input())
	print(reversedInteger(s))

if __name__ == "__main__":
    main()