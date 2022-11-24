from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        '''
        Params:
        data(any) = data to be deleted
        '''
        current = self.head # Set current value to iterate
        previous = None
        while current: # While this is not "None"
            if current.data == data:
            # if current equals data
                if current == self.head: # and the current is the head
                    self.next = self.head # the next pass to be the new head
                    self.size -= 1
                    return
                else:
                    previous.next = current.next # the previous node reference the next node, and we loss this one
                    self.size -= 1
                    return
            previous = current
            current = current.next
    
    def search(self, data):
        '''
        Look if the data is in the linked list

        Params:
        data(any) = data to be found
        '''
        for node in self.iter():
            if data == node:
                return True
        return False

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
   
    def print_list(self):
        '''
        Print all data of the linked list, step by step
        '''
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        '''
        Add a node at the end of the linked list

        Params:
        data(any) = data of the last node of the list
        '''
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next        
            current.next = node
        self.size += 1

    def prepend(self, data):
        '''
        Add a node at the start of the linked list

        Params:
        data(any) = data of the new first node of the list
        '''
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_after_node(self, previous_node, data):
        '''
        Insert a new node after another one

        Params:
        previous_node(any) = Must be the data to search and insert node after it
        data(any) = New node
        '''
        if self.search(previous_node): 
            new_node = Node(data) # Create new node
            current_node = self.head # Set current node
            while current_node.data != previous_node: # Itinerate through the list to get the chosen node
                current_node = current_node.next
            new_node.next, current_node.next = current_node.next, new_node
        else: print("Previous node is not present in the list")
            

''' TEST
llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node("G", "F")

llist.print_list()
'''