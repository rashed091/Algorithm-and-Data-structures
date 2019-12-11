from itertools import *
import operator

counter = count()
print(list(next(counter) for _ in range(5)))

print(list(accumulate([1, 2, 3, 4, 5], operator.add)))


def first_order(p, q, initial_val):
    """Return sequence defined by s(n) = p * s(n-1) + q."""
    return accumulate(repeat(initial_val), lambda s, _: p*s + q)


evens = first_order(p=1, q=2, initial_val=0)
print(list(next(evens) for _ in range(5)))


def second_order(p, q, r, initial_values):
    """Return sequence defined by s(n) = p * s(n-1) + q * s(n-2) + r."""
    intermediate = accumulate(
        repeat(initial_values),
        lambda s, _: (s[1], p*s[1] + q*s[0] + r)
    )
    return map(lambda x: x[0], intermediate)


fibs = second_order(p=1, q=1, r=0, initial_values=(0, 1))
print(list(next(fibs) for _ in range(8)))


print(list(repeat(2, 5)))

print(list(product([1, 2], ['a', 'b'])))

print(list(islice([1, 2, 3, 4, 5], 0, 5, 2)))


print(list(chain([1, 2], [3, 4, 5, 6], [7, 8, 9])))

print(list(chain.from_iterable([[1, 2, 3], [4, 5, 6]])))

print(list(filterfalse(bool, [1, 0, 1, 0, 0])))

print(list(takewhile(bool, [1, 0, 1, 0, 0])))

print(list(dropwhile(bool, [1, 0, 1, 0, 0])))
