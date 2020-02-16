def read_string(string):
    sum=0
    f=string.split(" ")
    add=1
    for i in range(0, len(f)):
        if f[i].isdigit():
            if add==1:
                sum=sum+f[i]
            else:
                sum=sum-f[i]
        elif f[i]=="+":
            add=1
        elif f[i]=="-":
            add=0
    if sum>0:
        return True
    else:
        return False

lst=[1, 2, 1, 15, 20, 11, 7, 4, 9, 10]

def iterative(lst):
    string=""
    for i in range(0, len(lst)):
        str=str+lst[i]
        if i!=len(lst)-1:
