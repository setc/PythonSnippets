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

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):
        print('get[%s]:' % i, end = '')
    def __iter__(self):
        print('iter => ', end = '')
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self,x):
        print('contains: ', end = '')
        return x in self.data

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset  = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

if __name__ == '__main__':
    X = Squares(1,5)
    [n for n in X]

    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))

    for x in skipper:
        for y in skipper:
            print(x + y, end = ' ')

    Y = Iters([1,2,3,4,5])
    print(3 in Y)
    for i in Y:
        print(i, end = ' | ')

    print()
    print([i ** 2 for i in Y])
    print(list(map(bin,X)))

    I = iter(Y)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
