x = 5  # Variable global


def modify_global():
    global x
    x += 9
    print(f'valor modificado {x}')


modify_global()
