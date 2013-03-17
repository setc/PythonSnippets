def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    sol = ''
    i=0
    
    if len(s1) > len(s2):
        longstring = s1
        shortstring = s2
    else:
        longstring = s2
        shortstring = s1

    for i in range(len(shortstring)):
        sol = sol + shortstring(i)
        sol = sol + longstring(i)
    sol = sol + longstring[i+1:]

    return sol
