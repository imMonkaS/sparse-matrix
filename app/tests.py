from matrix import SparseMatrix
from utils import *


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
