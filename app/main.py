"""
Запрещено держать матрицу в чистом виде

Разные размеры матриц
Увеличиваем размеры

Меняется параметр наполности этой матрицы

Действие с этими матрицами

График 📈

Если 50% 0 а 50% 1 то она не разьеж.
"""
from utils import is_sparse_matrix, SRC_PATH


def main():
    print(is_sparse_matrix(SRC_PATH + 'test.txt'))


if __name__ == '__main__':
    main()
