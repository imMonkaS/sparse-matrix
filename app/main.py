"""
Запрещено держать матрицу в чистом виде

Разные размеры матриц
Увеличиваем размеры

Меняется параметр наполности этой матрицы

Действие с этими матрицами

График 📈

Если 50% 0 а 50% 1 то она не разьеж.
"""
from utils import count_sparsity, SRC_PATH, is_sparse_matrix, algo, generate_matrix


def main():
    # print(is_sparse_matrix(SRC_PATH + 'test.txt'))
    # print(is_sparse_matrix(SRC_PATH + 'test2.txt'))
    # algo(SRC_PATH + 'test.txt', 4)
    generate_matrix(7, 0.89, 3, 8)


if __name__ == '__main__':
    main()
