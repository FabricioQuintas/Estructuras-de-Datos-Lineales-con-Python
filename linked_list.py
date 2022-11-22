from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


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


    def size(self):
        return str(self.size)
    

    def iter(self):
        current = self.tail

        while current:
            val = current.data
            current = current.next
            yield val


    def delete(self, data):
        '''
        Params:
        data(any) = data to be deleted
        '''
        current = self.tail # Set current value to iterate
        previous = self.tail # And previous one

        while current: # While this is not "None"
            if current.data == data:
            # if current equals data
                if current == self.tail:
                # and the current is the tail
                    self.tail = current.next
                    # this one pass to be the next
                    # and we loss the previous node
                    self.size -= 1
                else:
                    previous.next = current.next
                    # the previous node, will reference the node
                    # next to this one, so we loss this one
                    self.size -= 1
                    return current.data

            previous = current
            current = current.next
    

    def search(self, data):
        '''
        Look if the data is in the linked list

        Params:
        data(any) = data to be found
        '''
        found = False
        for node in self.iter():
            if data == node:
                found = True
                print(f"Data {data} found!")
        if found == False:
            print(f"Data {data} wasn't found")


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



llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")

llist.print_list()