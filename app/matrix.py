import random
from typing import Tuple, List, Union


class SparseMatrix:
    def __init__(self):
        # positions stored as: [(value, row, column)]
        self._positions: List[Tuple[Union[str, int], int, int]] = []
        self._diagonal: List[Union[str, int]] = []
        self._size = len(self._diagonal)
        self._predominant = '0'
        self._symmetric: bool = True

    def print_matrix_data(self):
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
        if head is not None and tail is not None:
            ht_range = list(range(0, head)) + list(range(self._size - tail, self._size))
        else:
            ht_range = range(self._size)

        with open(output_file_path, 'w') as f:
            f.write('')
        with open(output_file_path, 'a') as f:
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
        pass

    def get_sparsity(self) -> float:
        return 1 - self.get_density()

    def get_density(self) -> float:
        diagonal = len([_ for _ in self._diagonal if _ != self._predominant])
        off_diagonal = len(self._positions) * 2

        return round((diagonal + off_diagonal) / self._size**2, 2)

    def is_sparse(self) -> bool:
        if self.get_sparsity() > 0.5:
            return True
        return False
