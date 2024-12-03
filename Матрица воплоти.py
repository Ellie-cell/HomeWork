

def get_matrix(n, m, value):
    matrix = []
    for i in range(n) :
        matrix_1 = []
        for j in range(m) :
            matrix_1.append(value)
        matrix.append(matrix_1)
    return matrix


a = get_matrix (2, 2, 10)
b = get_matrix (3, 5, 42)
c = get_matrix (4, 2, 13)
print(a)
print(b)
print(c)