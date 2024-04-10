SRC_PATH = 'sources/'


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
