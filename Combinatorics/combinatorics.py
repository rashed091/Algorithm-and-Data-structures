from itertools import product, combinations, combinations_with_replacement, permutations

print(list(product('abc', repeat=2)))
print(list(combinations('abc', 2)))
print(list(combinations_with_replacement('abc', 2)))
print(list(permutations('abc', 2)))