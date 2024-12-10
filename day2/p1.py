import time

MAX_SAFE_DIFFERENCE = 3


def parse_input(input):
    return list(map(int, input.split(' ')))


def is_safe(report):
    is_increasing = False

    if report[0] < report[-1]:
        is_increasing = True
    elif report[0] > report[-1]:
        is_increasing = False
    else:
        return False

    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) > MAX_SAFE_DIFFERENCE or abs(report[i] - report[i + 1]) == 0:
            return False
        
        if is_increasing and report[i] > report[i + 1]:
            return False
        
        if not is_increasing and report[i] < report[i + 1]:
            return False
        
    return True


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')

    num_safe_reports = 0
    
    for row in inputs:
        num_safe_reports += is_safe(parse_input(row))

    print(num_safe_reports)


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
