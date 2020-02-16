lst=[]

def ui():
    while True:
        '''func = {"add": add(), "print": prnt(), "1": func1(), "2": func2()}'''
        x = input("What would you like to do? 'add' to add a new number, 'print' to print the entire list, '1' to print using the first property, '2' to print using the second property and 'exit' to exit the application. ")
        if x == "add":
            at = inpt()
            bt = create_complex_number(at[0], at[1])
            add(bt)
        elif x == "print":
            prnt(0, len(lst))
        elif x == "1":
            rt=func1()
            prnt(rt[0], rt[1])
        elif x == "2":
            rt=func2()
            prnt(rt[0], rt[1])
        elif x == "exit":
            return
        elif x == "test":
            testn()
        '''elif x == "3":
            rt=func3()
            prnt(rt[0], rt[1])'''
        
        

def inpt():
    x = input("Input the real part of the number: ")
    x = float(x)
    y = input("Input the imaginary part of the number: ")
    y = float(y)
    return (x, y)

def create_complex_number(a, b):
    '''
    This function creates a complex number c given a and b, its real and
    imaginary parts, respectively.
    Input: a, b
    Preconditions: a, b - float
    Output: c
    Postconditions: c - complex number (c=a+bi)
    '''
    tup = [a, b]
    return tup

def add (tup):
    lst.append(tup)

def prnt(x, y):
    for i in range (x, y):
        print("{0}+{1}i".format(lst[i][0], lst[i][1]))


def func1():
    '''
    This function searches the list for and returns the start and end of the longest sequence of
    numbers that have the same modulus.
    Input: -
    Preconditions: -
    Output: st, end - integers
    Postconditions: st indicates the start of the longest sequence
                    end indicates the end of the longest sequence 
    '''
    mx = 0
    nr = -1
    y = 1
    for x in range(0, len(lst)-1):
        nr = nr+1
        i = 1
        mod = get_Real(x)**2+get_Imag(x)**2
        for y in range (nr+1, len(lst)):
            if get_Real(y)**2+get_Imag(y)**2 == mod:
                i = i+1
            else:
                break
        if i>mx:
            st = nr
            end = i
            mx = i
        '''if mx>len(lst)/2:
            break'''
    return(st, end)

def func2():
    '''
    This function searches the list for and returns the start and end of the longest sequence of
    numbers whose sum of the moduluses equals 10+10i.
    Input: -
    Precondition: -
    Output: st, end
    Postcondition: st indicates the start of the longest sequence
                    end indicates the end of the longest sequence
    '''
    mx = 0
    cop = -1
    for x in lst:
        cop = cop+1
        nr = cop
        i = 0
        sr = 0
        si = 0
        while si < 10 and sr < 10 and nr<len(lst):
            i = i+1
            si = si + get_Imag(nr)
            sr = sr + get_Real(nr)
            nr = nr+1
        if si == 10 and sr == 10 and i>mx:
            st = cop
            end = nr
            mx = i
    return(st, end)

'''
def func3():
    This function searches the list for and returns the start and end of the longest sequence of
    real numbers.
    Input: -
    Precondition: -
    Output: st, end
    Postcondition: st indicates the start of the longest sequence
                    end indicates the end of the longest sequence
    mx = 0
    nr = -1
    y = 1
    st = 0
    end = 0
    for x in lst:
        nr = nr+1
        i = 1
        if get_Imag(nr)==0:
            for y in range (nr+1, len(lst)):
                if get_Imag(y)==0:
                    i = i+1
                else:
                    break
        if i>mx:
            mx = i
            st = nr
            end = y
    return(st, end)
'''

def get_Real(x):
    '''
    This function returns the real part of the complex number x.
    Input: x
    Preconditions: x - complex number
    Output: r
    Postconditions: r - float, real part of c
    '''
    return lst[x][0]

def get_Imag(x):
    '''
    This function returns the imaginary part of the complex number x.
    Input: x
    Preconditions: x - complex number
    Output: i
    Postconditions: i - float, imaginary part of c
    '''
    return lst[x][1]

def set_Real(c, x):
    '''
    This function sets the value of the real part of the complex number c.
    Input: c, x
    Preconditions: c - complex, x- float
    Output: c
    Postconditions: c- complex number with x as real part
    '''
    lst[c][0]=x
    return (lst[c][0], lst[c][1])

def set_Imag(c, x):
    '''
    This function sets the value of the imaginary part of the complex number c.
    Input: c, x
    Preconditions: c - complex, x - float
    Output: c
    Postconditions: c- complex number with x as imaginary part
    '''
    lst[c][1]=x
    return (lst[c][0], lst[c][1])

def testn():
    lst.append((2, 3))
    lst.append((3, 2))
    lst.append((2, 3))
    lst.append((3, 2))
    lst.append((2, 0))
    lst.append((2, 0))
    lst.append((3, 0))
    lst.append((0, 0))
    lst.append((3, 10))
    lst.append((4, 0))
    lst.append((5, 5))
    lst.append((6, 1))

def test1():
    d=create_complex_number(2.0, 3.0)
    add(d)
    c=create_complex_number(3.0, 2.0)
    add(c)
    b=create_complex_number(-2.0, 3.0)
    add(b)
    a=create_complex_number(2.0, 1.0)
    add(a)
    assert func1()==(0, 3)
    lst.clear()
'''
def test3():
    lst.append([2, 0])
    lst.append([3, 3])
    lst.append([5, 0])
    lst.append([0, 0])
    lst.append([3, 0])
    assert func3()==(2, 5)
    lst.clear()
'''
def test2():
    d=create_complex_number(10.0, 10.0)
    add(d)
    c=create_complex_number(2.0, 5.0)
    add(c)
    b=create_complex_number(7.0, 2.0)
    add(b)
    a=create_complex_number(1.0, 3.0)
    add(a)
    e=create_complex_number(2.0, 5.0)
    add(e)
    f=create_complex_number(8.0, 5.0)
    add(f)
    assert func2()==(1, 4)
    lst.clear()

def test():
    test1()
    test2()
    #test3()

test()
ui()
