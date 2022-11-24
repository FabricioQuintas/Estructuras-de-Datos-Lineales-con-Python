from node import Node


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        '''
        Insert a new Node

        data(any) = Value of the node
        '''
        node = Node(data)

        if self.head == None: # Our list doesn't have any values
            self.head = node
            self.head.next = self.head
        else: # Our list have any value
            node.next = self.head # The next of the new node, is the head
            current = self.head
            while current.next != self.head: # Iterate until get the last node of our list
                current = current.next
            current.next = node
        self.size += 1

    def print(self):
        '''
        Print all value of Nodes
        '''
        current = self.head
        size = self.size
        while size > 0:
            print(f'The Node {current} have value {current.data} and the next Node is {current.next}')
            current = current.next
            size -= 1


if __name__ == '__main__':
    quantity_nodes = int(input('Insert the quantity of nodes: '))
    node_number = 1
    node = CircularLinkedList()
    while node_number <= quantity_nodes:
        data_node = input(f'Set a value for node number {node_number}: ')
        node.append(data_node)
        node_number += 1
    node.print()