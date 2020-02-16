from src.sub_3_list import *

def filter_real(lst):
    '''
    This function removes all numbers that are not real from the list.
    Input: lst
    Preconditions: lst - list of complex numbers
    Output: lst'
    Postconditions: lst' = lst without numbers that are not real
    '''
    lst=list_real(lst, 0, len(lst)-1)
    return lst

def filter_modulo_less(lst, m):
    '''
    This function removes all numbers whose modulo is lower than m.
    Input: lst, m
    Preconditions: lst - list of complex numbers, m - integer
    Output: lst'
    Postconditions: lst' = lst without numbers whose modulo is equal to or greater than m
    '''
    lst=find_lower(lst, m)
    return lst

def filter_modulo_equal(lst, m):
    '''
    This function removes all numbers whose modulo is equal to m.
    Input: lst, m
    Preconditions: lst - list of complex numbers, m - integer
    Output: lst'
    Postconditions: lst' = lst without numbers whose modulo is lower or greater than m
    '''
    lst=find_equal(lst, m)
    return lst

def filter_modulo_great(lst, m):
    '''
    This function removes all numbers whose modulo is greater than m.
    Input: lst, m
    Preconditions: lst - list of complex numbers, m - integer
    Output: lst'
    Postconditions: lst' = lst without numbers whose modulo is equal to or lower than m
    '''
    lst=find_greater(lst, m)
    return lst