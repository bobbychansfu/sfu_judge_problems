# Function to find all interleaving of string `X` and `Y`
def findInterleavings(X, Y, interleavings, curr=''):
    # insert `curr` into the set if the end of both strings is reached
    if not X and not Y:
        interleavings.add(curr)
        return
 
    # if the string `X` is not empty, append its first character in the
    # result and recur for the remaining substring
 
    if X:
        findInterleavings(X[1:], Y, interleavings, curr + X[0])
 
    # if the string `Y` is not empty, append its first character in the
    # result and recur for the remaining substring
 
    if Y:
        findInterleavings(X, Y[1:], interleavings, curr + Y[0])
 
    return interleavings
 
 
def shuffleAll(X, Y):
 
    # use set to handle duplicates
    interleavings = set()
 
    if not X and not Y:
        return interleavings
 
    findInterleavings(X, Y, interleavings)
    return list(interleavings)
 
 
def main():
 
    X = input()
    Y = input()
 
    shuffled = shuffleAll(X, Y)
    shuffled.sort()
    print(*shuffled)

main()
