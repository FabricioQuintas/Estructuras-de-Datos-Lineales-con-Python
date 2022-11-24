

class Queue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data):
        self.inbound_stack.append(data)

    def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        if self.outbound_stack:
            return self.outbound_stack.pop()
        return None


if __name__ == '__main__':
    numbers = Queue()

    numbers.enqueue(5)
    numbers.enqueue(6)
    numbers.enqueue(7)
    
    print(numbers.inbound_stack)

    numbers.dequeue()
    print(numbers.outbound_stack)

    numbers.dequeue()
    print(numbers.outbound_stack)

    numbers.dequeue()
    print(numbers.outbound_stack)

    numbers.dequeue()
    print(numbers.outbound_stack)