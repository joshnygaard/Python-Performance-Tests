
from tqdm import tqdm
import time


operators_set = {'OR', 'AND', 'NOT', 'NOR'}
operators_list = ['OR', 'AND', 'NOT', 'NOR']
operators_tuple = ('OR', 'AND', 'NOT', 'NOR')

my_rule_and = 'AND'
my_rule_has_ethic = 'has_ethic'


iterations = 100000000
show_result = True


def main():
    results = list()
    methods = [
        in_set,
        in_list,
        in_tuple
    ]

    results = list(map(_benchmark, methods))

    print('#    Name                                              s/iter')
    for i, result in enumerate(sorted(results, key=lambda x: x[1])):
        print('{:3}) {:50}{:,.4}s'.format(
            i + 1, result[0], result[1] / iterations))


def in_set():
    return my_rule_and in operators_set, my_rule_has_ethic in operators_set


def in_list():
    return my_rule_and in operators_list, my_rule_has_ethic in operators_list


def in_tuple():
    return my_rule_and in operators_tuple, my_rule_has_ethic in operators_tuple


def _benchmark(method):
    start = time.time()
    name = method.__name__
    for _ in tqdm(range(iterations), leave=False, desc=name):
        result = method()
    if show_result:
        print(name)
        print(result)
    return(name, time.time() - start)


if __name__ == '__main__':
    main()
