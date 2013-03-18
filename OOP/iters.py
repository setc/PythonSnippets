#iters.py
#
#Example of creating iterators with classes.

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):                 #Overloading iter to create a iterator
        return self
    def __next__(self):                 #Return square at each iteration
        if self.value == self.stop:     #unless is at the end of the sequence
            raise StopIteration
        self.value += 1
        return self.value ** 2
