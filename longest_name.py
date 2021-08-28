from itertools import product, repeat, starmap
from tqdm import tqdm
import time
from functools import partial


def _hello(x, y):
    return 'Hello {} and {}'.format(x, y)


people = ['Josh', 'Sandi', 'Rachel', 'Emily',
          'Alex H', 'Molly', 'Alex S', 'Mandi', 'Anna']

iterations = 100
show_result = False


def main():
    results = list()
    methods = [
        for_loop,
        just_max
    ]

    results = list(map(_benchmark, methods))

    print('#    Name                                              s/iter')
    for i, result in enumerate(sorted(results, key=lambda x: x[1])):
        print('{:3}) {:50}{:,.4}s'.format(
            i + 1, result[0], result[1] / iterations))


def _benchmark(method):
    start = time.time()
    name = method.__name__
    for _ in tqdm(range(iterations), leave=False, desc=name):
        result = method()
    if show_result:
        print(name)
        print(result)
    return(name, time.time() - start)


def for_loop():
    longest_name = ""
    for person in people:
        if len(person) > len(longest_name):
            longest_name = person

    return longest_name


# Winner
def just_max():
    return max(people, key=len)


if __name__ == '__main__':
    main()
