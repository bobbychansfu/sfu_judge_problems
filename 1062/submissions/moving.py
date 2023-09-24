inp = input("Enter the date you want to move in: ").split()
month = int(inp[0])
date = int(inp[1])

if(month == 11 or month == 12 or month == 1):
  print("It is not a good day to move in")
elif(date % 10 == 9 or date % 10 == 0):
    print("It is not a good day to move in")
else:
    print("It is good day to move in")

