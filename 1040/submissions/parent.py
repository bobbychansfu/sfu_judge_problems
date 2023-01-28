r1 = input("Did you eat? ")
r2 = input("Did you study? ")
r3 = input("Did you do your laundry? ")
r4 = input("Did you call grandma? ")

count = 0
if (r1 == 'yes'):
    count += 1
if (r2 == 'yes'):
    count += 1
if (r3 == 'yes'):
    count += 1
if (r4 == 'yes'):
    count += 1

if (count==0):
    print("We need to talk.")
elif (count==1 or count ==2):
    print("Ok.")
else:
    print("Good!")