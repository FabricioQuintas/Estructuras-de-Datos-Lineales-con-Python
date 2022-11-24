from node import Node


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    
    def append(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.head.next = self.head
        else:
            node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
        self.size += 1

    def print(self):
        current = self.head
        size = self.size
        while size > 0:
            print(f'The Node {current} have value {current.data}')
            current = current.next
            size -= 1

    