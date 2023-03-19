# Python3 code to demonstrate working of
# Extract elements with Frequency greater than K
# Using count() + loop

# initializing list
test_list = list(map(int, input().split()))


# initializing K
K = 2

res = []
for i in test_list:
	
	# using count() to get count of elements
	freq = test_list.count(i)
	
	# checking if not already entered in results
	if freq > K and i not in res:
		res.append(i)

res.sort()
# printing results
print(*res)
