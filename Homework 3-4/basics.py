def read(x):
    '''
    This function takes the user input, a complex number in the form of a+bi, and returns the real and imaginary parts
    in the form of a list.
    Input: x
    Preconditions: x - string
    Output: [r, i]
    Postconditions: [r, i] list, r, i - integers
    '''
    rneg = False
    ineg = False
    r=0
    i=0
    rdone = False
    y=0
    if x[0]=='-':
        rneg = True
        y=1
    while y<len(x):
        if str.isdigit(x[y])==True:
            if rdone == False:
                r=r*10+int(x[y])
            else:
                i=i*10+int(x[y])
        else:
            if x[y]=='+':
                rdone = True
            elif x[y]=='-':
                rdone = True
                ineg = True
        y=y+1
    if rneg == True:
        r=-r
    if ineg == True:
        i=-i
    return [r, i]


def create_complex(r, i):
    '''
    This function creates a complex number by taking the real and imaginary parts and returning them as a list.
    Input: r, i
    Preconditions: r, i - integers
    Output: c
    Postconditions: c - complex number
    '''
    c=[r, i]
    return c

def get_Real(c):
    '''
    This function returns the real part of the complex number c.
    Input: c
    Preconditions: c - complex number
    Output: r
    Postconditions: r- integer
    '''
    return c[0]

def get_Imag(c):
    '''
    This function returns the imaginary part of the complex number c.
    Input: c
    Preconditions: c - complex number
    Output: i
    Postconditions: i- integer
    '''
    return c[1]

def set_Real(c, r):
    '''
    This function replaces the real part of the complex number c with the integer r.
    Input: c, r
    Preconditions: c - complex number, r - integer
    Output: c'
    Postconditions: c' = c modified with the real part now being r
    '''
    c[0]=r

def set_Imag(c, i):
    '''
    This function replaces the imaginary part of the complex number c with the integer i.
    Input: c, i
    Preconditions: c - complex number, i - integer
    Output: c'
    Postconditions: c' = c modified with the imaginary part now being i
    '''
    c[1] = i