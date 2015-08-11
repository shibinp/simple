def diagonal_sum(matrix):
    row_size = len(matrix[0])
    return sum(row[i] for i, row in enumerate(matrix[:row_size]))


print diagonal_sum([[1,2],[3,4],[5,6]])
