# Consider a positive number n. Determine all its decompositions as sums of prime numbers

def prime(x):
    if x<2:
        return False
    elif x%2==0 and x!=2:
        return False
    else:
        i=3
        while (i*i<x):
            if x%i==0:
                return False
            i+=2
    return True

def sum_list(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum

def print_sum(list):
    msg=""
    for i in range(len(list)):
        msg=msg+str(list[i])+"+"
    msg=msg+"\b"
    print (msg)

def decompose_iterative(n):
    lst=[]
    for i in range(2, n):
        if prime(i):
            lst.append(i)
            sum=i
            while sum<n:
                for j in range(2, n):
                    if prime(j):
                        lst.append(j)
                        sum=sum+j
    print_sum(lst)


def decompose_recursive(n, lst, current_nr):
    '''
    n-the decomposed number
    sum-the current sum of the elements
    x-the list of elements
    nr-current number to be added'''
    
    sum=sum_list(lst)
    if sum==n:
        print_sum(lst)
    if n>sum:
        return
    if prime(current_nr):
        lst.append(prime)
        sum=sum+current_nr
    return decompose_recursive(n, lst, current_nr+1)



def test_prime():
    assert prime(2)==True
    assert prime(4)==False
    assert prime(21)==False
    assert prime(31)==True

test_prime()
decompose_recursive(7, [], 0)