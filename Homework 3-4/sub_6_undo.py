from src.sub_2_remove_replace import *

def list_undo(lst, biglst):
    '''
    This function reverts the list back by one modifying command.
    Input: lst, biglst
    Preconditions: lst - list of complex numbers, biglst - list of lists
    Output: tup = (lst', biglst')
    Postconditions: lst' = lst reverted by one step, biglst' = biglst with its last element removed
    '''
    y = len(biglst) - 2
    if y < 0:
        lst = []
    else:
        lst = biglst[y].copy()
    remove(biglst, y + 1, y + 1)
    tup=lst, biglst
    return tup