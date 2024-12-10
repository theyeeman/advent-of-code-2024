import time
import re


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    total_sum = 0

    regex_pattern = r"mul\((\d+),(\d+)\)"

    for input in inputs:
        multiply_pairs = re.findall(regex_pattern, input)

    for a, b in multiply_pairs:
        total_sum += int(a) * int(b)

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
