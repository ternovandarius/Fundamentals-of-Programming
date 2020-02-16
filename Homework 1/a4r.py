def num_sort(x):
    '''
    Function that takes each digit of a number, then creates the highest
    possible value using those digits.
    input: x - integer
    preconditions: -
    output: function returns a number or a message
    postconditions: function returns the largest number possible with the same
    digits as x if x is positive, or a message otherwise
    '''
    
    if x < 0:
        return "Integer needs to be positive!"
    else:
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            y = 0
            while x>0:
                arr[x%10] = arr[x%10]+1
                x = x//10
            for i in range (9, 0, -1):
                while arr[i]>0:
                    arr[i] = arr[i]-1
                    y = y*10 + i
            return y

def ui():
    while True:
        x = input("Insert an integer, or type 'exit' to close the program.")
        if x == "exit":
            return
        else:
            x = int(x)
            r = num_sort(x)
            print(r)

def test():
    assert num_sort(23321234) == 43332221
    assert num_sort(123) == 321
    assert num_sort(1) == 1
    assert num_sort(-142231) == "Integer needs to be positive!"

test()
ui()
