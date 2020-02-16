def perfect(x):
    '''
    This function checks whether a number is equal to the sum of its divisors,
    excluding itself.
    input: x - integer
    preconditions: x positive
    output: True or False
    postconditions: function returns True if the number is perfect, or false otherwise
    '''
    s=0

    for i in range(1, x):
        if x%i==0:
            s=s+i

    if s==x:
        return True
    else:
        return False

def program(x):
    '''
    This function checks whether there is a perfect number smaller than the number given.
    input: x - integer
    preconditions: x positive
    output: function prints something
    postconditions: function prints the largest perfect number smaller than the number given,
    or a message if it does not exist.
    '''
    r = False
    for i in range (x-1, 0, -1):
        r=perfect(i)
        if r == True:
            return i
            break
    if r == False:
        return "No such number exists."

def ui():
    while True:
        x = input("Insert the number, or 'exit' to exit:")
        if x == "exit":
            return
        else:
            x = int (x)
            y = program(x)
            print(y)

def test():
    assert program(6) == "No such number exists."
    assert program(-1) == "No such number exists."
    assert program (7) == 6
    assert program (28) == 6
    assert program (30) == 28
    assert program (500) == 496

test()
ui()
