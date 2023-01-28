full = input()
i = full.find(" ")
coun = full[:i]
cap = full[i+1:]
print(cap, "is", coun + "'s capital city")
