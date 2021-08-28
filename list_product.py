import time
from itertools import product

from tqdm import tqdm

people = ['Josh', 'Sandi', 'Rachel', 'Emily']
dogs = ['Fitz', 'Mable', 'Aggie']

iterations = 10000000
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

start = time.time()
name = 'Product method in list comprehension'
for i in tqdm(range(iterations), leave=False, desc=name):
    combined = [x for x in product(people, dogs)]
if show_result:
    print(name)
    print(combined)
results.append((name, time.time() - start))

# Winner
start = time.time()
name = 'Product method in list'
for i in tqdm(range(iterations), leave=False, desc=name):
    combined = list(product(people, dogs))
if show_result:
    print(name)
    print(combined)
results.append((name, time.time() - start))

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
