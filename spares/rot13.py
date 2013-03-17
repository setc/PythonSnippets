def rot13(text):
    """
    Takes a string and applies the rot13 code to it.
    """

    from string import maketrans
    
    string = str(text)
    tocode = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code   = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"

    rot13 = maketrans(tocode, code)
    return string.translate(rot13)

a = rot13("Testing this piece of code.")
b = rot13(a)
print(a)
print(b)
