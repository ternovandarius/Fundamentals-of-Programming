from src.basics import *

def remove(lst, s, e):
    '''
    This function removes the elements starting from position s to position e+1.
    Input: lst, s, e
    Preconditions: lst - list of complex elements, s, e - integers
    Output: lst'
    Postconditions: lst' = lst without the elements on positions s, e or between s and e
    '''
    del lst[s:e+1]
    return lst

def replace(lst, v, r):
    '''
    This function replaces the elements that have the value v with the element r.
    Input: lst, v, r
    Preconditions: lst - list of complex number, v, r - complex numbers
    Output: lst'
    Postconditions: lst' = lst, but with elements that equal v replaced with r
    '''
    for i in range (0, len(lst)):
        if lst[i]==v:
            x=get_Real(r)
            y=get_Imag(r)
            set_Real(lst[i], x)
            set_Imag(lst[i], y)