"""
Запрещено держать матрицу в чистом виде

Разные размеры матриц
Увеличиваем размеры

Меняется параметр наполности этой матрицы

Действие с этими матрицами

График 📈

Если 50% 0 а 50% 1 то она не разьеж.
"""

from tests import *
SRC_PATH = 'sources/'


def main():
    matrix = SparseMatrix()
    matrix.generate(5, 0.7, 1, 9)
    matrix.print_matrix()
    matrix.change_values(5)
    print()
    matrix.print_matrix()


if __name__ == '__main__':
    main()
