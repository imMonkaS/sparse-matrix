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
            lesser_numbers.append(str(num))
        else:
            bigger_numbers.append(str(num))

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
        predominant: str,
        start: int,
        end: int
):
    """
    Сгенерировать матрицу с разреженностью +- 1-2% от ожидаемой.
    """
    numbers_amount = round((1 - (expected_sparsity/100)) * matrix_size**2)
    matrix = [[] for _ in range(matrix_size)]

    diagonal_numbers_amount = random.randint(0, min(numbers_amount, matrix_size))
    non_diagonal_numbers_amount = numbers_amount - diagonal_numbers_amount
    if non_diagonal_numbers_amount % 2 != 0:
        non_diagonal_numbers_amount += 1
        diagonal_numbers_amount -= 1
    non_diagonal_numbers_amount = int(non_diagonal_numbers_amount / 2)

    diagonal_positions = [(i, i) for i in range(matrix_size)]
    non_diagonal_positions = [(i, j) for i in range(1, matrix_size) for j in range(i)]

    non_diagonal_positions = random.sample(non_diagonal_positions, non_diagonal_numbers_amount)
    diagonal_positions = random.sample(diagonal_positions, diagonal_numbers_amount)

    positions = sorted(diagonal_positions + non_diagonal_positions)
    hash_rows = {}
    for pos in positions:
        if pos[0] not in hash_rows.keys():
            hash_rows[pos[0]] = [pos[1]]
        else:
            hash_rows[pos[0]].append(pos[1])

    for i in range(matrix_size):
        # В строке все нули
        if i not in hash_rows.keys():
            matrix[i].append(f'*{i + 1}')
        else:
            difference_left = hash_rows[i][0] - 0
            if difference_left != 0:
                matrix[i].append(f'*{difference_left}')

            row = hash_rows[i]
            for pos in range(len(row) - 1):
                matrix[i].append(f'{random.randint(start, end)}')
                zeros = (row[pos + 1] - row[pos]) - 1
                if zeros != 0:
                    matrix[i].append(f'*{zeros}')

            matrix[i].append(f'{random.randint(start, end)}')

            difference_right = i - hash_rows[i][-1]
            if difference_right != 0:
                matrix[i].append(f'*{difference_right}')

    return matrix


def unzipped_matrix_to_file(matrix: List[List[str]], predominant: str, output: str, head: int = None, tail: int = None):
    with open(output, 'w') as f:
        unzipped_matrix = matrix

        for row in unzipped_matrix:
            i = 0
            while i < len(row):
                if '*' in row[i]:
                    amount = int(row[i][1:])
                    for _ in range(amount):
                        row.insert(i, '0')
                    del row[i + amount]
                i += 1
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                unzipped_matrix[i].append(matrix[j][i])

        f.write(f'predominant: {predominant}' + '\n')

        if head is None or tail is None:
            for row in unzipped_matrix:
                f.write(' '.join(row) + '\n')
        else:
            for row in unzipped_matrix[:head] + unzipped_matrix[len(unzipped_matrix) - tail:]:
                f.write(' '.join(row[:head] + row[len(row) - tail:]) + '\n')


def matrix_to_file(matrix: List[List[str]], predominant: str, output: str):
    with open(output, 'w') as f:
        f.write(f'predominant: {predominant}' + '\n')
        for row in matrix:
            f.write(' '.join(row) + '\n')
