class Node:
    def __init__(self, node_prev, value):
        self.node_prev = node_prev
        self.node_next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, value):
        if self.head is None and self.tail is None:
            self.head = self.tail = Node(None, value)
        else:
            self.tail.node_next = Node(self.tail, value)
            self.tail = self.tail.node_next

    def operation(self):
        if self.head.value < self.tail.value:
            if self.head.value + self.tail.value < 2**30:
                self.head.value = self.head.value + self.tail.value
            else:
                self.head.value = (self.head.value + self.tail.value) % 2**30
            self.tail.node_next = self.head
            self.head.node_prev = self.tail
            self.head = self.head.node_next
            self.head.node_prev = None
            self.tail = self.tail.node_next
            self.tail.node_next = None
        else:
            if 0 < self.tail.value - self.head.value < 2**30:
                self.tail.value = self.tail.value - self.head.value
            else:
                self.tail.value = (self.tail.value - self.head.value) % 2**30
            self.tail.node_next = self.head
            self.head.node_prev = self.tail
            self.tail = self.tail.node_prev
            self.tail.node_next = None
            self.head = self.head.node_prev
            self.head.node_prev = None

    def print(self):
        current = self.head
        while current is not None:
            print(current.value, ' ', end='')
            current = current.node_next


def main():
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    linked_list = LinkedList()
    for value in array:
        linked_list.push_back(value)

    for _ in range(k):
        linked_list.operation()

    linked_list.print()


if __name__ == "__main__":
    main()
