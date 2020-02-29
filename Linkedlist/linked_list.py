class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def remove(self, item):
        current = self.head
        previous = None

        while True:
            if current.value == item:
                break
            previous, current = current, current.next
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def print_list(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next


if __name__ == "__main__":
    lst = LinkedList()
    lst.add(5)
    lst.add(10)
    lst.add(15)
    lst.print_list()
    lst.remove(10)
    lst.print_list()