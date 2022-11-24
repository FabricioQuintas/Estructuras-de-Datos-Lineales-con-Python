

class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def enqueue(self, data):
        '''
        Insert a element at the end of the queue
        '''
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        '''
        Remove the last element of the queue
        '''
        data = self.items.pop()
        self.size -= 1
        return data
    
    def traverse(self):
        '''
        Iterate through all the Queue and print his elements
        '''
        total_items = self.size
        for i in range(total_items):
            print(self.items[i])
    

if __name__ == '__main__':
    quantity = int(input('How many items do you want to add to the queue?  '))
    myQueue = ListQueue()

    for i in range(quantity):
        data = input(f'Set a value for the {i+1} item: ')
        myQueue.enqueue(data)

    myQueue.traverse()