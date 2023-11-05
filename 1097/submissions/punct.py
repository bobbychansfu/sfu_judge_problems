def minTimeToVisitAllPoints(points):
    # Initialize time to 0
    total_time = 0

    # Go through each point (except the last one)
    for i in range(len(points) - 1):
        # Calculate the change in x and y
        delta_x = abs(points[i+1][0] - points[i][0])
        delta_y = abs(points[i+1][1] - points[i][1])

        # The time to next point is the max of delta_x and delta_y
        # This is because we can move diagonally, covering one unit distance in both x and y in 1 second
        total_time += max(delta_x, delta_y)

    return total_time

# Example usage
n = int(input())
points = 
print(minTimeToVisitAllPoints(points))  # Output should be 9
