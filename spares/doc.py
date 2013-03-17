"""
This is an example of module documentation.
Yadda yadda yadda, writing about the module.
"""

something = 3.1415

def square(x):
    """
    And here is an example of function documentation.
    """
    return x**2     #comment

class Someone:
    """
    Example of class documentation
    """
    pass

print(square(42))
print(square.__doc__)
