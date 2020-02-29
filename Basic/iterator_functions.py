from itertools import *

# iter
nums = [1, 2, 3, 4, 5]
iters = [iter(nums)] * 2
print(list(id(itr) for itr in iters))


def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)


def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return zip_longest(*iters, fillvalue=fillvalue)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(better_grouper(nums, 2)))

print(list(better_grouper(nums, 4)))

print(list(grouper(nums, 4)))



