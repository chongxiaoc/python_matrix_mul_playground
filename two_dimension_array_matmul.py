import numpy as np

mat_a =[[0, 1], [2, 3], [4, 5]]
mat_b =[[0, 1, 2], [3, 4, 5]]

def mat_mul(m, l, n, mat_x, mat_y):
    """
    m: n_rows of mat_x
    l: n_cols of mat_x; n_rows of mat_y
    n: n_cols of mat_y
    """
    assert len(mat_x) == m
    assert len(mat_x[0]) == l
    assert len(mat_y) == l
    assert len(mat_y[0]) == n
    mat_z = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(l):
                mat_z[i][j] += mat_a[i][k] * mat_b[k][j]

    return mat_z


mat_c = mat_mul(3, 2, 3, mat_a, mat_b)
print(np.matrix(mat_a))
print(np.matrix(mat_b))
print(np.matrix(mat_c))
