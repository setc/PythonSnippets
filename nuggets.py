def McNuggets(n):

    sizes = (6, 9, 20)
       
    if n == 0: return True

    for amount in sizes:
        if n >= amount and McNuggets(n - amount):
            return True

    return False
