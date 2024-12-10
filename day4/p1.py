import time

PETURBS = [
    [ [0, 0], [0, 1], [0, 2], [0, 3] ],
    [ [0, 0], [0, -1], [0, -2], [0, -3] ],
    [ [0, 0], [1, 0], [2, 0], [3, 0] ],
    [ [0, 0], [-1, 0], [-2, 0], [-3, 0] ],
    [ [0, 0], [-1, -1], [-2, -2], [-3, -3]],
    [ [0, 0], [1, -1], [2, -2], [3, -3]],
    [ [0, 0], [-1, 1], [-2, 2], [-3, 3]],
    [ [0, 0], [1, 1], [2, 2], [3, 3]],
]


def pretty_print(matrix):
    print('************************')

    for row in matrix:
        print(row)

    print('************************')


def convert_to_matrix(inputs):
    matrix = []

    for row in inputs:
        matrix.append(list(row))

    return matrix


def are_indices_in_bounds(matrix, i, j):
    return i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[0])


def generate_words(matrix, i, j):
    word_list = []

    for peturb in PETURBS:
        curr_word = []

        for dx, dy  in peturb:
            next_i = i + dx
            next_j = j + dy

            if not are_indices_in_bounds(matrix, next_i, next_j):
                continue

            curr_word.append(matrix[next_i][next_j])
        
        word_list.append(''.join(curr_word))

    return word_list


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    matrix = convert_to_matrix(inputs)

    word_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for word in generate_words(matrix, i, j):
                if word == 'XMAS':
                    word_count += 1

    print(word_count)


# Boilerplate code below
class standard_func:
    def get_input_as_int(filename):
        with open(filename) as f:
            return list(map(lambda a : int(a), list((f.read()).split("\n"))))

    def get_input_as_str(filename):
        with open(filename) as f:
            return list((f.read()).split("\n"))

    def print_performance(start, end):
        print('Execution time (s):', round((end - start), 3))


if __name__ == "__main__":
    perf_counter_start = time.perf_counter()
    main()
    perf_counter_end = time.perf_counter()
    standard_func.print_performance(perf_counter_start, perf_counter_end)
