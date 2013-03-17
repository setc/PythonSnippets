def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    base = b
    sol = 1

    #Exceptions:
    if x < b: return 0
    if b == 0: return 0

    #We iterate until we get our solution:
    while base * b <= x:
        sol = sol + 1
        base = base * b
    return sol
