import time


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


def has_cross(matrix, i, j):
    mas_set = set(['M', 'A', 'S'])

    try:
      if i - 1 < 0 or j - 1 < 0:
          return False
      
      maybe_mas_1 = set([matrix[i + 1][j + 1], matrix[i][j], matrix[i - 1][j - 1]])
      maybe_mas_2 = set([matrix[i + 1][j - 1], matrix[i][j], matrix[i - 1][j + 1]])

      if maybe_mas_1 == mas_set and maybe_mas_2 == mas_set:
          return True
      
      return False

    except IndexError:
        return False


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    matrix = convert_to_matrix(inputs)

    word_count = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'A':
                word_count += has_cross(matrix, i, j)

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
