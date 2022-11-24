from node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        '''
        Add an element to the TOP of the stack

        data(any) = Value of the Node
        '''
        node = Node(data)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        '''
        Return the data of the value at the top and remove it from the stack
        '''
        if self.top:
            data = self.top.data
            self.size -= 1

            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
        
            return data
        else:
            return "The stack is empty"
        
    def peek(self):
        if self.top:
            return self.top.data
        else:
            return "The stack is empty"
    
    def clear(self):
        '''
        Clear the entire stack
        '''
        while self.top:
            self.pop()

    def size(self):
        return str(self.size)

    def print(self):
        '''
        Print all data of the stack
        '''
        current = self.top
        size = self.size
        print(f'We have {size} elements in the stack')
        while size > 0:
            print(f'{current.data} is the element in position: {size}')
            current = current.next
            size -= 1


if __name__ == '__main__':
    quantity = int(input('How many items do you want to add to the stack?: '))
    myStack = Stack()

    for i in range(quantity):
        data = input(f'Set a value for the {i+1} item: ')
        myStack.push(data)
    myStack.print()    
    
    print(f'The size of the stack is: {myStack.size}')
    
    while myStack.size > 0: # Lets pop all items
        print(f'The last item of the stack is: {myStack.peek()}')
        print(f'The value {myStack.pop()} has been removed from the stack')
    
