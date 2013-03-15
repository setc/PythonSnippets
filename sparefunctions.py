#To Relocate Functions
#Sebastian Torrente
#I type a lot of functions while studying Python that don't fit any type of
#module or are too few. Normally, as they are kinda trivial or small cases of
#'reinventing the whell' I discard them. But I thought it would be better if I
#compile them.

#I Think I have another one of those around, must search it later.
"""
Different functions that I type waiting for the right module to be transfered
"""

def ltreesum(tree):
    """
    This function gets a list tree composed by nested lists and numbers and add
    all the numbers that finds in it.
    """
    #As an additional note, this is one of the cases where recursion is an
    #option, iteration is always the best choice when possible.
    total = 0
    for element in tree:
        if not isinstance(element, list):
            total += element
        else:
            total += ltreesum(element)
    return total

#Hardcoded reduce

def hardreduce(function, sequence):
    """
    Reduce is kinda hard to understand at first, this funcion only purpose is
    as a reminder of what reduce do.
    """
    stack = sequence[0]
    for next in sequence[1:]:
        stack = function(stack, next)
    return stack

#Harcoded map
def mymap(func, *seqs):
    """
    Map function as shown in Learn Python by Mark Lutz.
    """
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

def mymap2(func, *seqs):
    """
    Same as before, just a different example
    """
    res = []
    for args in zip(*seqs):
        yield func(*args)

def mymap3(fun, *seqs):
    """
    Same as before, the third example
    """
    return (func(*args) for args in zip(*seqs))

def main():

    #Test of ltreeadder:
    tree = [1, [[2, 3], [5, 6]], 8, [9, [10, [11, 12, 13], 14]]]
    print('ltreesum',ltreesum(tree))

    #Test of hardcoded
    print('hardreduce',hardreduce((lambda x, y: x+y), [1,2,3,4,5]))

    #Test of mymap
    print('mymap',mymap(abs, [-2, -1, 0, 1, 2]))
    print('mymap2',mymap2(pow, [1,2,3],[2,3,4,5]))
    print('mymap3',mymap3(pow, [1,2,3],[2,3,4,5]))
    
if __name__ == '__main__':
    main()
