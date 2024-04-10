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
    # pairs = [
    #     (10, 70),
    #     (100, 70),
    #     (100, 90),
    #     (1000, 70),
    #     (1000, 90),
    #     (10000, 65),
    #     (10000, 95),
    #     (100000, 65),
    #     (100000, 95)
    # ]
    #
    # for pair in pairs:
    #     create_testing_data(
    #         pair[0],
    #         pair[1] / 100,
    #         SRC_PATH + f'report/{pair[0]}_{pair[1]}/data.txt',
    #         SRC_PATH + f'report/{pair[0]}_{pair[1]}/data.txt',
    #     )

    # size = 10000
    # dens = 95
    # create_testing_data(
    #     size,
    #     dens / 100,
    #     SRC_PATH + f'report/{size}_{dens}/data.txt',
    #     SRC_PATH + f'report/{size}_{dens}/output.txt',
    #     head=10,
    #     tail=10
    # )

    binary_search(2, 2)


if __name__ == '__main__':
    main()
