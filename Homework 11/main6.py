import random
import string

def recursive(p, n, i, o, c):
    '''
    p-array that holds values
    n-number of parantheses
    i-current nr
    o-open parantheses
    c-closed parantheses
    '''
    if n%2!=0:
        print("This number of parantheses cannot be closed!")
        return 0
    else:
        if c==n//2:
            for i in range(0, len(p)):
                print(p[i], end="")
            print("\n")
            return p
        else:
            if o>c:
                p[i]=")"
                recursive(p, n, i+1, o, c+1)
            if o<n//2:
                p[i]="("
                recursive(p, n, i+1, o+1, c)

def test():
    n = 4
    p = [""] * n
    x=recursive(p, n, 0, 0, 0)
    y=true_iterative()
    #assert x==y test doesn't work :(

def iterative(n):
    let="()"
    return ("".join(random.choice(let) for i in range(n)))

def generate_n_validate(n):
    for i in range(10*n):
        x=iterative(n)
        o=0
        c=0
        for j in range(n):
            if x[j]=="(":
                o+=1
            else:
                if o<=c:
                    break
                else:
                    c+=1
        if c==o and c+o==n:
            print(x)

def validate_true_iterative(n, p):
    if p[0]==")" or p[3]=="(":
        return False
    open=1
    closed=1
    for i in range(1, 3):
        if p[i]=="(":
            open+=1
        else:
            closed+=1
    if open!=closed:
        return False
    else:
        return True

def true_iterative():
    '''
    This function prints the combinations of groups of closed paranthesis for n=4.
    '''
    p=[""]*4
    p[0]="("
    for j in range(2):
        if j==0:
            p[1]="("
            for k in range(2):
                if k==0:
                    p[2]="("
                    p[3]=")"
                    x=validate_true_iterative(4, p)
                    if x:
                        return p
                        #for i in range(4):
                            #print(p[i], end="")
                else:
                    p[2] = ")"
                    p[3] = ")"
                    x = validate_true_iterative(4, p)
                    if x:
                        return p
                        #for i in range(4):
                           # print(p[i], end="")


        else:
            p[1]=")"
            for k in range(2):
                if k==0:
                    p[2]="("
                    p[3]=")"
                    x=validate_true_iterative(4, p)
                    if x:
                        return p
                        #for i in range(4):
                           # print(p[i], end="")
                else:
                    p[2] = ")"
                    p[3] = ")"
                    x = validate_true_iterative(4, p)
                    if x:
                        return p
                       #for i in range(4):
                            #print(p[i], end="")


n=4
p=[""]*n
#recursive(p, n, 0, 0, 0)
#generate_n_validate(n)
#true_iterative()
test()