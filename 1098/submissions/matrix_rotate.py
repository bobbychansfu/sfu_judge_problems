def rotate(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

def main():
    # Input for the size of the matrix
    n = int(input())
    
    # Input for the elements of the matrix
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            element = int(input())
            row.append(element)
        matrix.append(row)
    
   
    rotated_matrix = rotate(matrix)
    
    # Displaying the rotated matrix
    
    for row in rotated_matrix:
        print(*row)

# Run the main function
if __name__ == "__main__":
    main()
