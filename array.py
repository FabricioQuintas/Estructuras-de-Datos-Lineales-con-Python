import random
from functools import reduce

class Array: # Represent an array
    def __init__(self, capacity, fill_value=None):
        '''
        capacity(int) = static size of the array.
        fill_value=(any, optional) = value at each position, None as default.
        '''
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        '''
        index(int) = index that we want to look at.
        '''
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        '''
        index(int) = index of number that we want to change.
        new_item(any) = new value for the item in the array.
        '''
        self.items[index] = new_item

    def __randomnumbers__(self, lower, upper):
        '''
        Receives 2 parameters, and set all array with random numbers between them
        ----
        lower(int) = minimum value
        upper(int) = maximum value
        '''
        for i in range(self.capacity - 1):
            random = random.randint(lower, upper)
            self.__setitem__(i, random)
    
    def __sumitems__(self):
        '''
        Sum all items an return the accumulative value
        '''
        return reduce(lambda a, b: a + b, self.items)