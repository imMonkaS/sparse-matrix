import random
from typing import Tuple, List, Union


class SparseMatrix:
    """
    Класс разреженной матрицы
    """
    def __init__(
            self,
            positions: List[Tuple[Union[str, int], int, int]] = None,
            diagonal: List[Union[str, int]] = None,
            size=0,
            predominant='0',
            symmetric: bool = True
    ):
        """
        Конструктор с копированием
        Args:
            positions: позиции значений и сами значения
            diagonal: значения диагонали
            size: размерность матрицы
            predominant: самый часто встречаеющийся элемент
            symmetric: симметрична ли матрица
        """
        # positions stored as: [(value, row, column)]
        self._positions = [] if positions is None else positions
        self._diagonal = [] if diagonal is None else diagonal
        self._size = size
        self._predominant = predominant
        self._symmetric: symmetric

    def copy(self) -> 'SparseMatrix':
        """
        создать копию матрицы
        Returns:

        """
        return SparseMatrix(self._positions, self._diagonal, self._size, self._predominant, self._symmetric)

    def clear(self):
        """
        очистить все поля
        """
        self._size = 0
        self._diagonal = []
        self._positions = []
        self._predominant = '0'
        self._symmetric = True

    def matrix_filled(self) -> bool:
        if len(self._diagonal) == 0:
            return False
        return True

    def print_matrix_data(self):
        """
        Вывести всю инфу по матрице
        """
        print(f'''positions: {self._positions}
diagonal: {self._diagonal}
size: {self._size}
predominant: {self._predominant}
sparsity: {self.get_sparsity()}
density: {self.get_density()}
''')

    def generate(
            self,
            size: int,
            sparsity: float,
            rand_start: int,
            rand_end: int,
            predominant: str = '0'
    ) -> None:
        """
        сгенерировать матрицу с разреженностью sparsity с возможной погрешностью в +- 0.1
        Args:
            size: размерность
            sparsity: разреженность до сотых
            rand_start: начало диапазона случайных чисел
            rand_end: конец диапазона случайных чисел
            predominant: Самый часто встречающийся элемент
        """
        self.clear()

        numbers_amount = round((1 - sparsity) * size**2)
        diagonal_numbers_amount = random.randint(0, min(numbers_amount, size))
        non_diagonal_numbers_amount = numbers_amount - diagonal_numbers_amount
        if non_diagonal_numbers_amount % 2 != 0:
            non_diagonal_numbers_amount += 1
            diagonal_numbers_amount -= 1
        non_diagonal_numbers_amount = int(non_diagonal_numbers_amount / 2)

        diagonal_positions = [i for i in range(size)]
        if diagonal_numbers_amount > 0:
            diagonal_positions = random.sample(diagonal_positions, diagonal_numbers_amount)
        else:
            diagonal_positions = []

        self._diagonal = [predominant] * size
        for pos in diagonal_positions:
            self._diagonal[pos] = random.randint(rand_start, rand_end)

        non_diagonal_positions = [(i, j) for i in range(1, size) for j in range(i)]
        non_diagonal_positions = random.sample(non_diagonal_positions, non_diagonal_numbers_amount)
        for pos in non_diagonal_positions:
            self._positions.append(
                (
                    random.randint(rand_start, rand_end),
                    pos[0],
                    pos[1]
                )
            )

        self._positions += [(pos[0], pos[2], pos[1]) for pos in self._positions]

        self._size = len(self._diagonal)
        self._predominant = predominant

    def read_matrix_from_file(self, input_file_path: str, symmetric: bool = True) -> None:
        """
        считать матрицу из файла
        Args:
            input_file_path: путь до файла
            symmetric: симметрична ли матрица в файле
        """
        self.clear()

        with open(input_file_path, 'r') as f:
            self._predominant = f.readline().strip()
            for el in f.readline().strip().split():
                if el == self._predominant or not el.isdigit():
                    self._diagonal.append(el)
                elif el.isdigit():
                    self._diagonal.append(int(el))

            values = f.readline().strip().split()
            rows = f.readline().strip().split()
            columns = f.readline().strip().split()

            for i in range(len(values)):
                self._positions.append(
                    (
                        values[i] if values[i] == self._predominant or not values[i].isdigit() else int(values[i]),
                        int(rows[i]),
                        int(columns[i])
                    )
                )

        if symmetric:
            self._positions += [(pos[0], pos[2], pos[1]) for pos in self._positions]
        else:
            self._symmetric = False

        self._size = len(self._diagonal)

    def make_file_of_matrix(self, output_file_path: str) -> None:
        """
        Записать матрицу в файл в формате SSS
        Args:
            output_file_path: путь до файла записи
        """
        with open(output_file_path, 'w') as f:
            f.write('')
        with open(output_file_path, 'a') as f:
            f.write(self._predominant + '\n')
            f.write(' '.join([str(el) for el in self._diagonal]) + '\n')

            values = []
            rows = []
            columns = []

            if self._symmetric:
                positions = self._positions[:int(len(self._positions) / 2)]
            else:
                positions = self._positions

            for pos in positions:
                values.append(str(pos[0]))
                rows.append(str(pos[1]))
                columns.append(str(pos[2]))

            f.write(' '.join(values) + '\n')
            f.write(' '.join(rows) + '\n')
            f.write(' '.join(columns) + '\n')

    def print_matrix(
            self,
            head: int = None,
            tail: int = None
    ) -> None:
        """
        вывести матрицу (либо часть матрицы)
        Args:
            head: элементов вывести в начале
            tail: элементов вывести в конце

        Returns:

        """
        if head is not None and tail is not None:
            ht_range = list(range(0, head)) + list(range(self._size - tail, self._size))
        else:
            ht_range = range(self._size)

        for i in ht_range:
            for j in ht_range:
                if i == j:
                    print(str(self._diagonal[i]) + ' ', end='')
                else:
                    flag = False
                    for pos in self._positions:
                        if i == pos[1] and j == pos[2]:
                            print(str(pos[0]) + ' ', end='')
                            flag = True
                    if not flag:
                        print(self._predominant + ' ', end='')
                if head is not None and tail is not None:
                    if j == head - 1:
                        print('... ', end='')
            if head is not None and tail is not None:
                if i == head - 1:
                    print('\n' + '. ' * (head + tail + 2), end='')

            print()

    def print_matrix_to_file(
            self,
            output_file_path: str = None,
            head: int = None,
            tail: int = None
    ) -> None:
        """
        вывести матрицу (либо часть матрицы)
        Args:
            output_file_path: путь до файла для записи
            head: элементов вывести в начале
            tail: элементов вывести в конце
        """
        if head is not None and tail is not None:
            ht_range = list(range(0, head)) + list(range(self._size - tail, self._size))
        else:
            ht_range = range(self._size)

        with open(output_file_path, 'w') as f:
            f.write('')
        with open(output_file_path, 'a') as f:
            f.write(f'Разреженность: {self.get_sparsity()}\n')
            if self.is_sparse():
                f.write('Матрица разреженная\n')
            else:
                f.write('Матрица не разреженная\n')
            for i in ht_range:
                for j in ht_range:
                    if i == j:
                        f.write(str(self._diagonal[i]) + ' ')
                    else:
                        flag = False
                        for pos in self._positions:
                            if i == pos[1] and j == pos[2]:
                                f.write(str(pos[0]) + ' ')
                                flag = True
                        if not flag:
                            f.write(self._predominant + ' ')
                    if head is not None and tail is not None:
                        if j == head - 1:
                            f.write('... ')
                if head is not None and tail is not None:
                    if i == head - 1:
                        f.write('\n' + '. ' * (head + tail + 2))

                f.write('\n')

    def change_values(self, b: int) -> None:
        """
        Основной алгоритм по заданию. Заменяет значения в матрице.
        На места ненулевых элементов матрицы вначале помещаются все её ненулевые элементы большие b, а затем ненулевые элементы меньшие b.
        Args:
            b: число для алгоритма
        """
        positions = self._positions.copy()
        positions += [(int(self._diagonal[i]), i, i) for i in range(len(self._diagonal)) if self._diagonal[i] != self._predominant]
        positions = sorted(positions, key=lambda x: (x[1], x[2]))

        lesser_elements = []
        bigger_elements = []
        for pos in [el[0] for el in positions]:
            if int(pos) <= b:
                lesser_elements.append(int(pos))
            else:
                bigger_elements.append(int(pos))

        elements = bigger_elements + lesser_elements
        elements_counter = 0
        positions_counter = 0
        for pos in positions:
            if pos[1] == pos[2]:
                self._diagonal[pos[1]] = elements[elements_counter]
            else:
                self._positions[positions_counter] = (elements[elements_counter], pos[1], pos[2])
                positions_counter += 1
            elements_counter += 1
        self._symmetric = False

    def get_sparsity(self) -> float:
        """
        Найти разреженность.
        Returns:
            float, разреженность до сотых
        """
        return 1 - self.get_density()

    def get_density(self) -> float:
        """
        Найти обратное разрежнности (1 - разреженность)
        Returns:
            float, до сотых
        """
        return round((len(self._diagonal) + len(self._positions)) / self._size**2, 2)

    def is_sparse(self) -> bool:
        """
        Является ли матрица разреженной (нулей больше половины всех элементов)
        Returns:
            bool
        """
        if self.get_sparsity() > 0.5:
            return True
        return False
