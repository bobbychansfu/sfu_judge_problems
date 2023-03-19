
 
# Function to return the maximum product of a subset of a given list
def findMaxProduct(nums):
    if len(nums) == 0:
        return 0
 
    if len(nums) == 1:
        return nums[0]
 
    product = 1         # to store the maximum product subset
 
    # stores the negative element having a minimum absolute value in the set
    abs_min_so_far = 1000
 
    negative = 0        # maintain the count of negative elements in the set
    positive = 0        # maintain the count of positive elements in the set
 
    contains_zero = False
 
    # traverse the given list
    for i in range(len(nums)):
 
        # if the current element is negative
        if nums[i] < 0:
            negative = negative + 1
            abs_min_so_far = min(abs_min_so_far, abs(nums[i]))
 
        # if the current element is positive
        elif nums[i] > 0:
            positive = positive + 1
 
        # if the current element is zero
        if nums[i] == 0:
            contains_zero = True
        else:
            product = product * nums[i]
 
    # if an odd number of negative elements are present, exclude the negative
    # element having a minimum absolute value from the subset
    if negative & 1:
        product = product   // -abs_min_so_far
 
    # special case – set contains one negative element and one or more zeroes
    if negative == 1 and positive == 0 and contains_zero:
        product = 0
 
    # special case – set contains all zeroes
    if negative == 0 and positive == 0 and contains_zero:
        product = 0
 
    # return the maximum product
    return product
 
 
def main():
    nums = list(map(int, input().split()))
    print(findMaxProduct(nums))
main()