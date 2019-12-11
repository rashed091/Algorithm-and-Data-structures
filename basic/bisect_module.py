import bisect
import random

haystack = [1, 4, 4, 5, 6, 8, 12]
needles = 4

print(bisect.bisect(haystack, needles))
print(bisect.bisect_right(haystack, needles))
print(bisect.bisect_left(haystack, needles))


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


# ['F', 'A', 'C', 'C', 'B', 'A', 'A']
[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]


SIZE = 7
random.seed(1902)

lst = []
for _ in range(SIZE):
    item = random.randrange(SIZE*2)
    bisect.insort(lst, item)
    print('%2d -> ' % item, lst)
