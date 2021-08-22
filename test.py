import random
from typing import Union
from itertools import product, starmap
from tqdm import tqdm
import time
from multiprocessing import Pool


# def _intersect(list_1, list_2):
#     for x in list_1:
#         if x in list_2:
#             return True
#     return False


# list_1 = {'Josh', 'Sandi', 'Emily', 'Rachel'}
# list_2 = {'Josh', 'Sandi'}

# result = _intersect(list_1, list_2)
# print(result)

# for x in list_1:
#     for y in list_2:
#         print(x, y)

# print(not {None}.isdisjoint(list_1))
# print(not list_2.isdisjoint(list_1))
# print(list_2 & list_2)
# print(list_2.intersection(list_2))
# print(_intersect(list_1, list_2))

# result = list()
# thing = [(x, y) for x in list_1 for y in list_2 if not y.startswith('J')]
# thing2 = [(x, y) for y in list_2 for x in list_1 if not y.startswith('J')]

# for x, y in enumerate(thing):
#     print('{}: {}'.format(x + 1, y))

# print(thing)
# print(thing2)

# print(random.choice(thing))

# print(None and True)
# print(True and None)
# print(None or True)
# print(True or None)
# print(None and False)
# print(False and None)
# print(None or False)
# print(False or None)


# # print(None & True)
# # print(None | True)
# # print(None & False)
# # print(None | False)


# def my_or(x: Union[None, bool], y: bool):
#     if x is None:
#         return y
#     else:
#         return x or y


# def my_and(x: Union[None, bool], y: bool):
#     if x is None:
#         return y
#     else:
#         return x and y


# print(all([True, False]))

# loops = 0
# jumps = 0

# for i in range(500):
#     jumps += 1
#     for j in range(10):
#         jumps += 1
#         loops += 1

# print(jumps, loops)


def _hello(x, y=None):
    z = 0
    for i in range(100000000):
        z += 1
    if y is None:
        y = 'No one'
    return 'Hello {} and {}'.format(x, y)


people = ['Josh', 'Sandi', 'Rachel', 'Emily']
dogs = ['Fitz', 'Mable', 'Aggie']

iterations = 100000000
show_result = False

results = list()

start = time.time()
name = 'List comprehension'
for i in tqdm(range(iterations), leave=False, desc=name):
    combined = [(x, y) for x in people for y in dogs]
if show_result:
    print(name)
    print(combined)
results.append((name, time.time() - start))

start = time.time()
name = 'Product method, then list comprehension'
for i in tqdm(range(iterations), leave=False, desc=name):
    combined = product(people, dogs)
    combined = [x for x in combined]
if show_result:
    print(name)
    print(combined)
results.append((name, time.time() - start))

# start = time.time()
# name = 'Product method in list comprehension'
# for i in tqdm(range(iterations), leave=False):
#     combined = [x for x in product(people, dogs)]
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = list()
#     for x in people:
#         for y in dogs:
#             combined.append((x, y))
# name = 'Nested loops'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = list()
#     for x in dogs:
#         for y in people:
#             combined.append((y, x))
# name = 'Nested loops, little first'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))


# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = {(x, y) for x in people for y in dogs}
# name = 'Set comprehension'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = product(people, dogs)
#     combined = {x for x in combined}
# name = 'Product method, then set comprehension'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = {x for x in product(people, dogs)}
# name = 'Product method in set comprehension'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = set()
#     for x in people:
#         for y in dogs:
#             combined.add((x, y))
# name = 'Nested loops, set'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

# start = time.time()
# for i in tqdm(range(iterations), leave=False):
#     combined = set()
#     for x in dogs:
#         for y in people:
#             combined.add((y, x))
# name = 'Nested loops, smallest first, set'
# if show_result:
#     print(name)
#     print(combined)
# results.append((name, time.time() - start))

print('#    Name                                    s/iter')
for i, result in enumerate(sorted(results, key=lambda x: x[1])):
    print('{:3}) {:40}{:,.4}s'.format(
        i + 1, result[0], result[1] / iterations))


# start =time.time()
# for i in tqdm(range(100000), leave=False):
#     combined_2 = product(people, dogs)
# print('Product method', (time() - start))

# something = starmap(_hello, product(people, dogs))
# for x in something:
#     print(x)


# def f(x):
#     return x*x


# if __name__ == '__main__':
#     with Pool(8) as p:
#         print(p.starmap(_hello, product(people, dogs)))

# for x in something:
#     print(x)
