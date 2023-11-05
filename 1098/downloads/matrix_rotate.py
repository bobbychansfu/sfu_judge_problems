def rotate(matrix):
    # your code goes here

def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = []
        for _ in range(n):
            element = int(input())
            row.append(element)
        matrix.append(row)
    
    rotated_matrix = rotate(matrix)
    
    for row in rotated_matrix:
        print(*row)

if __name__ == "__main__":
    main()
