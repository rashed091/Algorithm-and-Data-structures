class Queue:
    def __init__(self):
        self._items = []
    
    def is_empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        self._items.pop()

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(10)
    queue.enqueue(100)
    print(queue.size())