def time_to_boil(s, r):
    # If the water is already at or above boiling point
    if s >= 100:
        return 0
    
    # Simulate the increase in temperature
    seconds = 0
    while s < 100:
        s += r
        seconds += 1

    return seconds

# Input number of test cases
t = int(input())
time = 0

# Iterate through each test case
for _ in range(t):
    s, r = map(int, input().split())
    time += time_to_boil(s, r)

print (time)