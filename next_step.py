import random
from typing import Union
from itertools import product, starmap
from tqdm import tqdm
import time
from multiprocessing import Pool


def _hello(x, y):
    return 'Hello {} and {}'.format(x, y)


people = ['Josh', 'Sandi', 'Rachel', 'Emily']
dogs = ['Fitz', 'Mable', 'Aggie']

iterations = 10000000
show_result = False


def main():
    results = list()
    list_comp.__name__
    methods = [
        list_comp,
        product_method_then_starmap_in_list_comp,
        product_method_in_starmap_in_list_comp,
        product_method_in_starmap_in_list,
        nested_loops,
        nested_loops_smallest_first,
        set_comprehension,
        product_method_then_starmap_in_set_comp,
        product_method_in_starmap_in_set_comp,
        nested_loops_set,
        nested_loops_smallest_first_set
    ]

    results = list(map(_benchmark, methods))

    print('#    Name                                    s/iter')
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


def list_comp():
    return [_hello(x, y) for x in people for y in dogs]


def product_method_then_starmap_in_list_comp():
    result = product(people, dogs)
    return [x for x in starmap(_hello, result)]


def product_method_in_starmap_in_list_comp():
    return [x for x in starmap(_hello, product(people, dogs))]

# Winner


def product_method_in_starmap_in_list():
    return list(starmap(_hello, product(people, dogs)))


def nested_loops():
    combined = list()
    for x in dogs:
        for y in people:
            combined.append(_hello(y, x))
    return combined


def nested_loops_smallest_first():
    combined = list()
    for x in people:
        for y in dogs:
            combined.append(_hello(x, y))
    return combined


def set_comprehension():
    return {_hello(x, y) for x in people for y in dogs}


def product_method_then_starmap_in_set_comp():
    result = product(people, dogs)
    return {x for x in starmap(_hello, result)}


def product_method_in_starmap_in_set_comp():
    return {x for x in starmap(_hello, product(people, dogs))}


def nested_loops_set():
    combined = set()
    for x in people:
        for y in dogs:
            combined.add(_hello(x, y))
    return combined


def nested_loops_smallest_first_set():
    combined = set()
    for x in dogs:
        for y in people:
            combined.add(_hello(y, x))
    return combined


if __name__ == '__main__':
    main()
