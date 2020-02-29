import heapq

h = []
l = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]

# heappush, push the value item onto the heap
for i in l:
    heapq.heappush(h, i)

print(h)


l = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heapq.heapify(l)  # transform list x into a heap
print(l)


# heappop, pop and return the smallest item from the heap
e = heapq.heappop(l)
print(e)

# heapq.heappushpop, push item on the heap, then pop and return the smallest item from the heap
e = heapq.heappushpop(l, 5)
print(e)


# heapq.heapreplace, pop and return the smallest item from the heap, and also push the new item
e = heapq.heapreplace(l, 6)
print(e)

# heapq.nlargest
l2 = heapq.nlargest(4, l)
print(l2)

# heapq.nsmallest
l3 = heapq.nsmallest(4, l)
print(l3)
