"""
column-wise storage
[
 0 1
 2 3
 4 5
]
"""
mat_a = [0, 2, 4, 1, 3, 5] # 3, 2
"""
[
 0 1 2
 3 4 5
]
"""
mat_b = [0, 3, 1, 4, 2, 5] # 2, 3


def index_translate_2d_1d(i, j, m, n):
    """
    i, j: mat[i][j]
    m: n_rows
    n: n_cols
    """
    return i+j*m

def print_matrix(m, n, x):
    """
    m: n_rows
    n: n_cols
    x: array
    """
    print("[")
    for i in range(m):
        row = []
        for j in range(n):
            row.append(x[index_translate_2d_1d(i, j, m, n)])
        print(row)
    print("]")


print_matrix(3, 2, mat_a)
print_matrix(2, 3, mat_b)


def mat_mul(m, l, n, mat_x, mat_y):
    mat_z = [0 for _ in range(m*n)]
    for i in range(m):
        for j in range(n):
            for k in range(l):
                mat_z[index_translate_2d_1d(i, j, m, n)] +=\
                    mat_x[index_translate_2d_1d(i, k, m, l)] * mat_y[index_translate_2d_1d(k, j, l, n)]
    return mat_z

mat_c = mat_mul(3, 2, 3, mat_a, mat_b)
print_matrix(3, 3, mat_c)


