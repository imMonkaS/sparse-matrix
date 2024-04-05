import random
from typing import List

SRC_PATH = 'sources/'


def count_sparsity(matrix_file: str):
    with open(matrix_file, 'r') as f:
        f.readline()
        count_predominant = 0
        count_diagonal_predominant = 0
        count_lines = 0
        for line in f.readlines():
            count_lines += 1
            line = line.split()
            for l in line[:-1]:
                if '*' in l:
                    count_predominant += int(l[1:])
            if '*' in line[-1]:
                count_predominant += int(line[-1][1:]) - 1
                count_diagonal_predominant += 1
        return (count_predominant * 2 + count_diagonal_predominant) / (count_lines ** 2)


def is_sparse_matrix(matrix_file: str):
    if count_sparsity(matrix_file) > 0.5:
        return True
    return False


def print_matrix(matrix_file, output_file):
    pass


def read_matrix_file(matrix: List[List[str]]):
    pass


def algo(matrix_file: str, b: int):
    numbers = []

    matrix = []
    with open(matrix_file, 'r') as f:
        f.readline()
        for line in f.readlines():
            line = line.split()
            matrix.append(line)
            for l in line:
                if '*' not in l:
                    numbers.append(int(l))

    lesser_numbers = []
    bigger_numbers = []
    for num in numbers:
        if num < b:
            lesser_numbers.append(num)
        else:
            bigger_numbers.append(num)

    change_numbers = lesser_numbers + bigger_numbers
    change_numbers_index = 0

    for line in matrix:
        for col in range(len(line)):
            if '*' not in line[col]:
                line[col] = change_numbers[change_numbers_index]
                change_numbers_index += 1

    return matrix


def generate_matrix(
        matrix_size: int,
        expected_sparsity: float,
        start: int,
        end: int
):
    """
    Сгенерировать матрицу с разреженностью +- 1-2% от ожидаемой.
    """
    zeros_amount = int((expected_sparsity * matrix_size**2) / 2)
    random_numbers = [random.randint(start, end) for _ in range(int((matrix_size**2 - zeros_amount*2) / 2))]

    while zeros_amount * 2 + len(random_numbers) * 2 < matrix_size**2:
        zeros_amount += 1

    print(zeros_amount, random_numbers)

    for i in range(matrix_size):
        pass
