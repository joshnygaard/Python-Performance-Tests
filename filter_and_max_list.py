from itertools import dropwhile, filterfalse, product, repeat, starmap
from tqdm import tqdm
import time
from functools import partial


people = [
    {'name': 'Josh', 'age': 30, 'gender': 'm'},
    {'name': 'Sandi', 'age': 26, 'gender': 'f'},
    {'name': 'Rachel', 'age': 30, 'gender': 'f'},
    {'name': 'Emily', 'age': 29, 'gender': 'f'},
    {'name': 'Alex S', 'age': 30, 'gender': 'm'},
    {'name': 'Alex H', 'age': 27, 'gender': 'm'},
    {'name': 'Molly', 'age': 27, 'gender': 'f'},
    {'name': 'Mandi', 'age': 29, 'gender': 'f'},
    {'name': 'Anna', 'age': 24, 'gender': 'x'}
]

iterations = 20000000
show_result = False


def main():
    results = list()
    methods = [
        for_loop,
        filterFalse_in_max,
        for_loop_combined_if,
        list_comp_in_max,
        filter_in_max,
    ]

    results = list(map(_benchmark, methods))

    print('#    Name                                              s/iter')
    for i, result in enumerate(sorted(results, key=lambda x: x[1])):
        print('{:3}) {:50}{:,.4}s'.format(
            i + 1, result[0], result[1] / iterations))


def _is_female(person):
    return person['gender'] == 'f'


def _is_not_female(person):
    return person['gender'] != 'f'


def _get_age(person):
    return person['age']


def for_loop():
    oldest_age = -1
    oldest_name = ''
    for person in people:
        if _is_female(person):
            if _get_age(person) > oldest_age:
                oldest_name = person['name']
                oldest_age = person['age']

    return oldest_name


def for_loop_combined_if():
    oldest_age = -1
    oldest_name = ''
    for person in people:
        if _is_female(person) and _get_age(person) > oldest_age:
            oldest_name = person['name']
            oldest_age = person['age']

    return oldest_name


# Winner
def filterFalse_in_max():
    return max(filterfalse(_is_not_female, people), key=_get_age)['name']


def filter_in_max():
    return max(filter(_is_female, people), key=_get_age)['name']


def list_comp_in_max():
    return max([x for x in people if _is_female(x)], key=_get_age)['name']


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
