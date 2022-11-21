from array import Array


class Grid: # Representation of a grid
    def __init__(self, rows, columns, fill_value=None):
        '''
        rows(int) = quantity of rows
        columns(int) = quantity of columns
        fill_value(any, optional) = value of items, None as default
        '''
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
        
    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""

        for row in range(self.get_height()): # Iterate through each row
            for col in range(self.get_width()): # Iterate through each col
                # To the result, add the value of data and a space
                result += str(self.data[row[col]]) + " "

            result += "-" # Add an - for each row

        return str(result)
    