from itertools import product, repeat, starmap
from tqdm import tqdm
import time
from functools import partial


def _hello(x, y):
    return 'Hello {} and {}'.format(x, y)


people = ['Josh', 'Sandi', 'Rachel', 'Emily',
          'Alex H', 'Molly', 'Alex S', 'Mandi', 'Anna']


print(list(repeat(people, 4)))

dog = 'Mable'

iterations = 5000000
show_result = False


def main():
    results = list()
    methods = [
        partial_in_map,
        list_comp,
        repeat_in_map_with_len,
        repeat_in_map,
        for_loop,
        lambda_in_map
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


def partial_in_map():
    return list(map(partial(_hello, y=dog), people))


def lambda_in_map():
    return list(map(lambda x: _hello(x, dog), people))


def list_comp():
    return [_hello(x, dog) for x in people]


def repeat_in_map_with_len():
    return list(map(_hello, people, repeat(dog, len(people))))

# Winner


def repeat_in_map():
    return list(map(_hello, people, repeat(dog)))


def for_loop():
    result = list()
    for x in people:
        result.append(_hello(x, dog))
    return result


if __name__ == '__main__':
    main()
