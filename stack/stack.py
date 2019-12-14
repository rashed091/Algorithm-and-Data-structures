class Stack:
    def __init__(self):
        self._items = []
    
    def is_empty(self):
        return not bool (self._items)

    def push(self, item):
        self._items.append(item) # self._items.insert(0, item)

    def pop(self):
        return self._items.pop() # self._items.pop(0)

    def top(self):
        return self._items[-1] # self._items[0]

    def size(self):
        return len(self._items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(10)
    stack.push(100)
    stack.push(1000)
    print(stack.size())
    print(stack.pop())

