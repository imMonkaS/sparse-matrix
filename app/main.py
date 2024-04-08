"""
Запрещено держать матрицу в чистом виде

Разные размеры матриц
Увеличиваем размеры

Меняется параметр наполности этой матрицы

Действие с этими матрицами

График 📈

Если 50% 0 а 50% 1 то она не разьеж.
"""
from utils import *


def main():
    # print(is_sparse_matrix(SRC_PATH + 'test.txt'))
    # print(is_sparse_matrix(SRC_PATH + 'test2.txt'))
    # algo(SRC_PATH + 'test.txt', 4)
    # generate_matrix(7, 0.89, 3, 8)
    # generate_matrix(5, 70, '0', 1, 5)
    # generate_matrix(10, 70, '0', 1, 5)
    # matrix_to_file(generate_matrix(10, 70, '0', 10, 100), '0', SRC_PATH + 'test_generation.txt')
    # matrix_to_file(generate_matrix(5, 70, '0', 1, 9), '0', SRC_PATH + 'test_generation.txt')
    # matrix = generate_matrix(10, 70, '0', 1, 9)
    # unzipped_matrix_to_file(matrix, '0', 'testhead1.txt')
    # unzipped_matrix_to_file(matrix, '0', 'testhead2.txt', 3, 3)
    # unzipped_matrix_to_file(generate_matrix(5, 70, '0', 1, 9), '0', SRC_PATH + 'test_generation2.txt')
    # generate_matrix(10000, 90, '0', 1, 5)

    matrix = generate_matrix(10, 80, '0', 1, 5)
    print(is_sparse_matrix(SRC_PATH + 'test/test.txt'))
    matrix_to_file(matrix, '0', SRC_PATH + 'test/test.txt')
    unzipped_matrix_to_file(matrix, '0', SRC_PATH + 'test/full.txt')
    changed_matrix = algo(SRC_PATH + 'test/test.txt', 3)
    matrix_to_file(changed_matrix, '0', SRC_PATH + 'test/changed.txt')
    unzipped_matrix_to_file(changed_matrix, '0', SRC_PATH + 'test/changedfull.txt')


    # print(count_sparsity('matrix.txt'))


if __name__ == '__main__':
    main()
