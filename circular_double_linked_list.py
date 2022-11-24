from node import TwoWayNode


class CircleDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        '''
        Add an Node to the list

        data(any) = value of the Node
        '''
        node = TwoWayNode(data)
        if self.head == None:
            self.head = node
        elif self.tail == None:
            self.tail = node
            self.tail.previous = self.head
            self.head.next = self.tail
            self._link_head_to_tail()
        else:
            cur_last = self.tail
            self.tail = node
            self._insert_node(cur_last, node)
            self._link_head_to_tail()
        self.size += 1

    def prepend(self, data):
        '''
        Insert a node at the start of the list

        data(any) = New head Node
        '''
        node = TwoWayNode(data)
        if self.head == None:
            self.head = node
        else:
            next = self.head

            self.head = node

            next.previous = self.head
            self.head.next = next
            self._link_head_to_tail()
        self.size += 1

    
    def _insert_node(self, previous, node, next=None):
        '''
        Insert a Node next to a previous one, or between 

        previous(Node) = First Node
        node(Node) = New middle Node
        next(Node, optional) = Last Node
        '''
        if next:
            next.previous = node
            node.next = next
        previous.next = node
        node.previous = previous

    def _link_head_to_tail(self):
        '''
        Method to link the tail to head in both ways
        '''
        self.head.previous = self.tail
        self.tail.next = self.head 

    def print(self):
        '''
        Print all Nodes, his values, next values and previous values.
        '''
        current = self.head
        size = self.size
        while size > 0:
            print(f'The Node {current} have value {current.data} and the next Node is {current.next.data} and previous Node is {current.previous.data}')
            current = current.next
            size -= 1

    def size(self): # Return the size of the Circle Double Linked List
        return str(self.size)        


if __name__ == '__main__':
    quantity_nodes = int(input('Insert the quantity of nodes: '))
    node_number = 1
    cllist = CircleDoubleLinkedList()
    while node_number <= quantity_nodes:
        data_node = input(f'Set a value for node number {node_number}: ')
        cllist.append(data_node)
        node_number += 1
    cllist.prepend("F")
    cllist.print()    
