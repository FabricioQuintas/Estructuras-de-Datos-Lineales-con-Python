from node import TwoWayNode


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = TwoWayNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1

    def dequeue(self):
        current = self.head

        if self.count == 1:
            self.head = None
            self.tail = None
            self.count -= 1
        elif self.count >= 1:
            self.head = self.head.next
            self.head.previous = None
            self.count -= 1
        
        return current.data

    def size(self):
        return int(self.count)


if __name__ == '__main__':
    quantity = int(input('How many items do you want to add to the queue?: '))
    myQueue = Queue()

    for i in range(quantity):
        data = input(f'Set a value for the {i+1} item: ')
        myQueue.enqueue(data)

    while myQueue.size() > 0:
        print(f'Element: {myQueue.dequeue()}, has been removed')