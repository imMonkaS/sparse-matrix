import datetime
import time
from typing import Tuple, Union, List

from main import SRC_PATH
from matrix import SparseMatrix


def test_matrix_class():
    matrix = SparseMatrix()
    matrix2 = SparseMatrix()

    # matrix.read_matrix_from_file(SRC_PATH + 'test.txt')
    # print('matrix_from_file')
    # matrix.print_matrix_data()

    # matrix2.generate(8, 0.7, 1, 5, '#')
    # print('generated_matrix')
    # matrix2.print_matrix(SRC_PATH + 'testik.txt')
    # matrix2.make_file_of_matrix(SRC_PATH + 'testik_data.txt')
    # matrix2.print_matrix_data()
    matrix2.read_matrix_from_file(SRC_PATH + 'testik_data.txt')
    matrix2.print_matrix_to_file(SRC_PATH + 'testik.txt')
    # matrix2.print_matrix()


def test_generate():
    matrix = SparseMatrix()
    matrix.generate(8, 0.7, 1, 5, '#')
    # matrix.print_matrix_data()
    matrix.make_file_of_matrix(SRC_PATH + 'test_generate/data.txt')
    matrix.print_matrix_to_file(SRC_PATH + 'test_generate/full.txt')


def test_reading():
    matrix = SparseMatrix()
    matrix.read_matrix_from_file(SRC_PATH + 'test.txt')
    # matrix.print_matrix_data()
    matrix.make_file_of_matrix(SRC_PATH + 'test_reading/data.txt')
    matrix.print_matrix_to_file(SRC_PATH + 'test_reading/full.txt')


def test_head_tail():
    matrix = SparseMatrix()
    matrix.generate(8, 0.7, 1, 5, '#')
    matrix.print_matrix()
    print()
    matrix.print_matrix(3, 2)


def test_head_tail_file():
    matrix1 = SparseMatrix()
    matrix1.generate(10, 0.7, 1, 5, '#')
    matrix1.make_file_of_matrix(SRC_PATH + 'head_tails_file/data.txt')
    matrix1.print_matrix_to_file(SRC_PATH + 'head_tails_file/gen_file.txt')
    matrix1.print_matrix_to_file(SRC_PATH + 'head_tails_file/gen_file3to2.txt', 3, 2)


def test_algorithm():
    matrix = SparseMatrix()
    # matrix.generate(5, 0.6, 1, 9)
    # matrix.make_file_of_matrix(SRC_PATH + 'algo/data.txt')
    matrix.read_matrix_from_file(SRC_PATH + 'algo/data.txt')
    matrix.print_matrix()
    matrix.change_values(5)
    print()
    matrix.print_matrix()


def create_testing_data(size, sparsity, data_file, output_file, rand_start=1, rand_end=100, predominant='0', head=None, tail=None):
    matrix = SparseMatrix()
    matrix.generate(size, sparsity, rand_start, rand_end, predominant)

    matrix.make_file_of_matrix(data_file)
    matrix.print_matrix_to_file(output_file, head, tail)


def test_time(data_file, b, output_file, time_file, head=None, tail=None):
    with open(output_file, 'w') as f:
        f.write('')

    matrix = SparseMatrix()

    start_filling_time = time.perf_counter()
    matrix.read_matrix_from_file(data_file)
    end_filling_time = time.perf_counter()

    # -----------TIME MEASURING-------------
    with open(time_file, 'a') as f:
        algo_time = time.perf_counter()
        matrix.change_values(b)
        end_algo_time = time.perf_counter()
        total_algo_time = end_algo_time - algo_time

        output_time = time.perf_counter()
        matrix.print_matrix_to_file(output_file, head, tail)
        end_output_time = time.perf_counter()
        total_output_time = end_output_time - output_time

        total_filling_time = end_filling_time - start_filling_time
        f.write(f'{datetime.datetime.now()}: Выполнение считывания матрицы с файла загяло {total_filling_time*1000:.3f} мс или {total_filling_time:.6f} с\n')
        f.write(f'{datetime.datetime.now()}: Выполнение алгоритма заняло {total_algo_time*1000:.3f} мс или {total_algo_time:.6f} с\n\n')
        f.write(f'{datetime.datetime.now()}: Вывод матрицы занял {total_output_time*1000:.3f} мс или {total_output_time:.6f} с\n\n')
    # -------------------------------------


def binary_search(pos: Tuple[int, int], items: List[Tuple[Union[str, int], int, int]]):
    items = [
        (1, 0, 1),
        (2, 3, 2),
        (3, 4, 2),
        (4, 0, 6),
        (5, 0, 4),
        (8, 0, 10),
        (6, 6, 8),
        (7, 1, 10),
    ]

    pos = (0, 4)

    items = sorted(items, key=lambda x: (x[1], x[2]))
    print(items)
    l = 0
    r = len(items)
    while l <= r:
        mid = l + (r - l) // 2
        if items[mid][1] == pos[0]:
            print(mid, items[mid][0])
            return
        elif items[mid][1] < pos[0]:
            l = mid + 1
        else:
            r = mid - 1

    print("-1")
    return
