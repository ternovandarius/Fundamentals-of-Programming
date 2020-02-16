def add_to_list(lst, c):
    '''
    This function adds the complex number c at the end of the list lst.
    Input: lst, c
    Preconditions: lst - list, c - complex number
    Output: lst'
    Preconditions: lst'=lst U {c}
    '''
    lst.append(c)

def insert_into_list(lst, c, poz):
    '''
    This function inserts the complex number c into the list lst at the position poz.
    Input: lst, c, poz
    Preconditions: lst - list, c - complex number, poz - integer
    Output: lst'
    Postconditions: lst' is lst, but with c at position poz
    '''
    lst.insert(poz, c)