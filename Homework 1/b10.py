def prop1(x):
    '''
    Function that calculates the product of the positive proper factors of an integer
    input: x - integer
    preconditions: -
    output: prints p
    postconditions: p is the product of positive proper factors of x, if x is positive, or 1 otherwise
    '''
    p=1

    for i in range(2, x):
        if x%i==0:
            p=p*i
    '''
    for i in range(-2, -x, -1):
        if x%i==0:
            p=p*i
    '''
    return p

def prop2(x):
    '''
    Function that calculates the product of the proper factors of an integer
    input: x - integer
    preconditions: -
    output: prints p
    postconditions: p is the product of proper factors of x, if x is positive, or 1 otherwise
    '''
    p=1

    for i in range(2, x):
        if x%i==0:
            p=p*i

    for i in range(-2, -x, -1):
        if x%i==0:
            p=p*i

    return p

def ui():
    while True:
        x= input("Input 1 to calculate the product for positive proper factors only, 2 for all proper factors and 3 to exit.")
        x = int(x)
        if x == 3:
            return
        else:
            y = input("Input the number:")
            y = int(y)
            if x == 1:
                r = prop1(y)
                print(r)
            else:
                r = prop2(y)
                print(r)

def test():
    assert prop1(5) == 1
    assert prop1(6) == 6
    assert prop1(20) == 400
    assert prop1(-1) == 1
    assert prop2(5)== 1
    assert prop2(9)==-9
    assert prop2(20)==160000

test()
ui()
