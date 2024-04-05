SRC_PATH = 'sources/'


def is_sparse_matrix(matrix_file: str):
    with open(matrix_file, 'r') as f:
        data = f.read()
        ones = data.count('1')
        zeros = data.count('0')
        if (zeros / (ones + zeros)) < 0.5:
            return False
        return True


def print_matrix(matrix_file, output_file):
    pass

def is_correctly_structurized_matrix():
    pass
