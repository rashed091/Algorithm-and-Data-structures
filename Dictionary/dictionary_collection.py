from collections import defaultdict

view = {'a': 1, 'b': 2, 'c': 3}

print(view.keys())
print(view.values())
print(view.items())

dct = defaultdict(lambda: 1)
print(dct['a'])


listView = defaultdict(list)

listView[1].append('a')
listView[1].append('b')
listView[2].append('a')
listView[2].append('c')
print(listView)
