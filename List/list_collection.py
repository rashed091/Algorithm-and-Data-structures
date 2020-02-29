import itertools, functools

list1 = [1, 2, 3, 4, 5]
list1.append(6)

list2 = [8, 6, 7, 9, 10]
list2.extend(list1)

print(list2)

print(sorted(list2))
print(list(reversed(list1)))
print(sum(list1))

print([sum(pair) for pair in zip(list1, list2)])

list3 = [(2, 3), (1, 2), (4, 1), (1, 1)]

print(sorted(list3, key=lambda el: (el[0], el[1])))

print(list(itertools.chain.from_iterable(list3)))
print(functools.reduce(lambda x, y: x + y, list1))

print(list1.count(1))
