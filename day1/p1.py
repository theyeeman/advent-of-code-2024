import time


def parse_input(inputs):
    l_list, r_list = [], []

    for row in inputs:
        left, right = row.split('   ')

        l_list.append(int(left))
        r_list.append(int(right))

    return sorted(l_list), sorted(r_list)


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    l_list, r_list = parse_input(inputs)

    total_sum = 0

    for a, b in zip(l_list, r_list):
        total_sum += abs(a - b)

    print(total_sum)


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
