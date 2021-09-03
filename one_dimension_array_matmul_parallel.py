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


def split_mat_vec(m, l, n, mat_x, mat_y, mat_z_global, z_j):
    mat_z = [0 for _ in range(m)]
    for i in range(m):
        for j in range(l):
            mat_z[index_translate_2d_1d(i, 0, m, 1)] +=\
                mat_x[index_translate_2d_1d(i, j, m, l)] * mat_y[index_translate_2d_1d(j, 0, l, 1)]
    for i in range(m):
        mat_z_global[index_translate_2d_1d(i, z_j, m, n)] = mat_z[i]


def mat_mul_threading(m, l, n, mat_x, mat_y):
    import threading

    mat_z = [0 for _ in range(m*n)]
    thread_list = []
    for j in range(n):
        mat_y_j = mat_y[j*l:(j+1)*l]
        thread_list.append(threading.Thread(target=split_mat_vec, args=(m, l, n, mat_x, mat_y_j, mat_z, j)))

    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    return mat_z

mat_c = mat_mul_threading(3, 2, 3, mat_a, mat_b)
print_matrix(3, 3, mat_c)
