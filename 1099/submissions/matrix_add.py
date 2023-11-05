def read_matrix(rows, cols):
    return [[int(x) for x in input().split()] for _ in range(rows)]

def sum_matrices(matrix_a, matrix_b):
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]

def main():
    r, c = map(int, input().split())
    matrix_a = read_matrix(r, c)
    matrix_b = read_matrix(r, c)
    result_matrix = sum_matrices(matrix_a, matrix_b)
    for row in result_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
