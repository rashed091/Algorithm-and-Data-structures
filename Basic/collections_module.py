from collections import Counter, deque

seq = [1, 2, 3, 4, 5, 6, 7, 1, 2, 4, 1]

seq_count = Counter(seq)
print(seq_count)


# The element() Function
cnt = Counter({1: 3, 2: 4})
print(list(cnt.elements()))

# The most_common() Function
print(cnt.most_common())

# The subtract() Function
deduct = {1: 1, 2: 2}
cnt.subtract(deduct)
print(cnt)


# -------------------------------- The deque ---------------------------------
lst = ["a", "b", "c"]
deq = deque(lst)
print(deq)

deq.append('x')
deq.appendleft('y')
print(deq)
print(deq.pop())
print(deq.popleft())
print(deq.clear())
