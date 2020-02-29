from collections import defaultdict, OrderedDict, Counter


pairs = {('a', 1), ('b', 2), ('c', 3)}

d1 = {}

for key, value in pairs:
    if key not in d1:
        d1[key] = []
    d1[key].append(value)
print(d1)


# ----------------- The defaultdict --------------------------->
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])


count = defaultdict(int)
names_list = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
for names in names_list:
    count[names] += 1
print(count)


lst = defaultdict(list)
lst[0].append(1)
lst[1].append(3)
print(lst)


#----------------------------- The OrderedDict -----------------------------#
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

for key, value in od.items():
    print(key, value)


lst = ["a", "c", "c", "a", "b", "a", "a", "b", "c"]
cnt = Counter(lst)
od = OrderedDict(cnt.most_common())
for key, value in od.items():
    print(key, value)
