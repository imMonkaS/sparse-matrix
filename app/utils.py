def is_sparse_matrix(matrix_file: str):
    with open(matrix_file, 'r') as f:
        data = f.read()
        print(data)
        ones = data.count('1')
        zeros = data.count('0')
        if (zeros / (ones + zeros)) > 0.5:
            return False
        return True