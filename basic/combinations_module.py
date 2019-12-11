from itertools import *

bills = [1, 2, 3]

print(list(combinations(bills, 2)))

for i in range(1, 4):
    for combination in combinations(bills, i):
        if sum(combination) == 3:
            print(combination)

print(list(combinations_with_replacement(bills, 2)))


for i in range(1, 4):
    for combination in combinations_with_replacement(bills, i):
        if sum(combination) == 3:
            print(combination)