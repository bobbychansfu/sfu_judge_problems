def find_enchanted_stones(rows, cols, grid):
    # List to store the coordinates of the enchanted stones
    enchanted_stones = []

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is an enchanted stone
            if grid[i][j] == 'X':
                # Rows and columns are 1-indexed in the output, so we add 1 to each
                enchanted_stones.append((i + 1, j + 1))

    # Return the list of coordinates
    return enchanted_stones

def main():
    # Read the number of rows and columns
    rows, cols = map(int, input().split())

    # Read the grid, splitting each line into a list of characters
    grid = [input().split() for _ in range(rows)]

    # Find the enchanted stones
    enchanted_stones = find_enchanted_stones(rows, cols, grid)
    if len(enchanted_stones) == 0:
         print("None")

    # Print the enchanted stones' coordinates
    for stone in enchanted_stones:
        print(*stone)

# Call the main function to run the program
if __name__ == "__main__":
    main()

