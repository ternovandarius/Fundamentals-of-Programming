from src.basics import *

def calc_sum(lst, s, e):
    '''
    This function calculates the sum of the elements of lst between s and e+1.
    Input: lst, s, e
    Preconditions: lst - list of complex numbers, s, e - integers
    Output: sum
    Postconditions: sum - complex number which equals the sum
    '''
    r=0
    im=0
    for i in range (s, e+1):
        r=r+get_Real(lst[i])
        im=im+get_Imag(lst[i])
    sum=create_complex(r, im)
    return sum

def calc_prod(lst, s, e):
    '''
    This function calculates the product of the elements of lst between s and e+1.
    Input: lst, s, e
    Preconditions: lst - list of complex numbers, s, e - integers
    Output: pr
    Postconditions: pr - complex number which equals the product
    '''
    r=1
    im=1
    for i in range (s,e+1):
        r=r*get_Real(lst[i])
        im=im*get_Imag(lst[i])
    pr=create_complex(r, im)
    return pr