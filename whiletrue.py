while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Not a number, cowboy')
    else:
        if num < 20:
            print('low')
        else:
            print(num**2)
print('Bye')
