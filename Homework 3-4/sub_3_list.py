from src.basics import *

def print_complex(c):
    '''
    This function prints a complex number.
    Input: c
    Preconditions: c - complex number
    Output: prints something
    Postconditions: prints the complex number in the correct form, based on its properties
    '''
    if c[0]>0 or c[0]<0:
        if c[1]>0:
            print ("{0}+{1}i".format(c[0], c[1]))
        elif c[1]<0:
            print ("{0}{1}i".format(c[0], c[1]))
        elif c[1]==0:
            print(c[0])
    elif c[0]==0:
        print("{0}i".format(c[1]))


def print_list(lst):
    '''
    This function prints a list of complex numbers.
    Input: lst
    Preconditions: lst - list
    Output: prints something
    Postconditions: prints a list of complex numbers, using the print_complex function
    '''
    for i in range (0, len(lst)):
        print_complex(lst[i])

def list_real(lst, s, e):
    '''
    This function returns the real numbers in list lst between value s and e.
    Input: lst, s, e
    Preconditions: lst - list of complex numbers, s,e - integers
    Output: rlst
    Postconditions: rlst - list of real numbers
    '''
    rlst=[]
    for i in range (s, e+1):
        if get_Imag(lst[i])==0:
            rlst.append(lst[i])
    return rlst

def get_modulo(c):
    '''
    This function returns the value of the modulo of a complex number.
    Input: c
    Preconditions: c- complex number, c=a+bi
    Output: m
    Postconditions: m- float, m=sqrt(a^2+b^2)
    '''
    a=get_Real(c)
    b=get_Imag(c)
    m=(a**2+b**2)**0.5
    return m

def find_lower(lst, m):
    '''
    This function returns a list of complex numbers in the list lst with the modulo lower than m.
    Input: lst, m
    Preconditions: lst - list of complex numbers, m - integer
    Output: lowlst
    Postconditions: lowlst- list of complex numbers with modulo lower than m
    '''
    lowlst=[]
    for i in range(0, len(lst)):
        if is_lower(lst[i], m):
            lowlst.append(lst[i])
    return lowlst

def is_lower(c, m):
    '''
    This function checks whether the modulo of a complex number is lower than a number m.
    Input: c,m
    Preconditions: c - complex number, m - integer
    Output: True/False
    Postconditions: True if the modulo is lower, or false otherwise.
    '''
    x=get_modulo(c)
    if x<m:
        return True
    else:
        return False

def find_equal(lst, m):
    '''
    This function returns a list of complex numbers in the list lst with the modulo m.
    Input: lst, m
    Preconditions: lst - list of complex numbers, m - integer
    Output: eqlst
    Postconditions: eqlst- list of complex numbers with modulo m
    '''
    eqlst=[]
    for i in range (0, len(lst)):
        if is_equal(lst[i], m) == True:
            eqlst.append(lst[i])
    return eqlst

def is_equal(c, m):
    '''
    This function checks whether the modulo of a complex number is  m.
    Input: c,m
    Preconditions: c - complex number, m - integer
    Output: True/False
    Postconditions: True if the modulo is m, or false otherwise.
    '''
    if get_modulo(c)==m:
        return True
    else:
        return False

def find_greater(lst, m):
    '''
    This function returns a list of complex numbers in the list lst with the modulo greater than m.
    Input: lst, m
    Preconditions: lst - list of complex numbers, m - integer
    Output: grtlst
    Postconditions: eqlst- list of complex numbers with modulo greater than m
    '''
    grtlst=[]
    for i in range (0, len(lst)):
        if is_greater(lst[i], m) == True:
            grtlst.append(lst[i])
    return grtlst

def is_greater(c, m):
    '''
    This function checks whether the modulo of a complex number is greater than m.
    Input: c,m
    Preconditions: c - complex number, m - integer
    Output: True/False
    Postconditions: True if the modulo is greater than m, or false otherwise.
    '''
    if get_modulo(c)>m:
        return True
    else:
        return False
