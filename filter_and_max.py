from itertools import dropwhile, filterfalse, product, repeat, starmap
from tqdm import tqdm
import time
from functools import partial


people = {
    'Josh': {'age': 30, 'gender': 'm'},
    'Sandi': {'age': 26, 'gender': 'f'},
    'Rachel': {'age': 30, 'gender': 'f'},
    'Emily': {'age': 29, 'gender': 'f'},
    'Alex S': {'age': 30, 'gender': 'm'},
    'Alex H': {'age': 27, 'gender': 'm'},
    'Molly': {'age': 27, 'gender': 'f'},
    'Mandi': {'age': 29, 'gender': 'f'},
    'Anna': {'age': 24, 'gender': 'x'}
}

people_list = [
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

iterations = 10000000
show_result = False


def main():
    results = list()
    methods = [
        for_loop,
        filterFalse_in_max,
        filterFalse_in_max_item_methods,
        for_loop_combined_if,
        list_comp_in_max,
        for_loop_combined_if_keys,
        list_comp_in_max_item_methods,
        filter_in_max,
        filter_in_max_item_methods
    ]

    results = list(map(_benchmark, methods))

    print('#    Name                                              s/iter')
    for i, result in enumerate(sorted(results, key=lambda x: x[1])):
        print('{:3}) {:50}{:,.4}s'.format(
            i + 1, result[0], result[1] / iterations))


def _is_female(person):
    return person['gender'] == 'f'


def _is_female_item(person):
    return person[1]['gender'] == 'f'


def _is_not_female_item(person):
    return person[1]['gender'] != 'f'


def _get_age(person):
    return person['age']


def _get_age_item(person):
    return person[1]['age']


def for_loop():
    oldest_age = -1
    oldest_name = ''
    for name, details in people.items():
        if _is_female(details):
            if _get_age(details) > oldest_age:
                oldest_name = name
                oldest_age = details['age']

    return oldest_name


def for_loop_combined_if():
    oldest_age = -1
    oldest_name = ''
    for name, details in people.items():
        if _is_female(details) and _get_age(details) > oldest_age:
            oldest_name = name
            oldest_age = details['age']

    return oldest_name


# Winner
def for_loop_combined_if_keys():
    oldest_age = -1
    oldest_name = ''
    for key in people:
        if _is_female(people[key]) and _get_age(people[key]) > oldest_age:
            oldest_name = key
            oldest_age = people[key]['age']

    return oldest_name


def filterFalse_in_max():
    return max(filterfalse(lambda x: not _is_female(x[1]), people.items()), key=lambda x: _get_age(x[1]))[0]


def filterFalse_in_max_item_methods():
    return max(filterfalse(_is_not_female_item, people.items()), key=_get_age_item)[0]


def filter_in_max():
    return max(filter(lambda x: _is_female(x[1]), people.items()), key=lambda x: _get_age(x[1]))[0]


def filter_in_max_item_methods():
    return max(filter(_is_female_item, people.items()), key=_get_age_item)[0]


def list_comp_in_max():
    return max([x for x in people.items() if _is_female(x[1])], key=lambda x: _get_age(x[1]))[0]


def list_comp_in_max_item_methods():
    return max([x for x in people.items() if _is_female(x[1])], key=_get_age_item)[0]


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
