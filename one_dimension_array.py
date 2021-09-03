"""
column-wise storage
[
 0 1
 2 3
 4 5
]
"""
mat = [0, 2, 4, 1, 3, 5]


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
            row.append(x[j*m+i])
        print(row)
    print("]")


print_matrix(3, 2, mat)
