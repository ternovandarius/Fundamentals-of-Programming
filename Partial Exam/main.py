def create_coord(x, y):
    '''
    This function creates a list that represents a certain point.
    input:x, y
    Preconditions: x, y - positive integers
    output: [x,y]
    Postconditions: [x, y] - list
    '''
    return [x, y]

def validate_input(id, hl, lr, color, value):
    '''
    Input:id, hl, lr, color, value
    Preconditions:id -  int, hl, lr - lists of integers, color - string, value - float
    Output: true or false
    Postconditions: true, if the parameters are valid, or false otherwise
    '''
    if id<=0:
        return False
    elif hl[0] <=0 or hl[1]<=0:
        return False
    elif lr[0] <=0 or lr[1]<=0:
        return False
    elif color=="":
        return False
    elif value<=0:
        return False
    elif abs((hl[0]-lr[0]))*abs((hl[1]-lr[1]))<25:
        return False
    return True

def get_id(plot):
    return plot[0]

def get_hl(plot):
    return plot[1]

def get_lr(plot):
    return plot[2]

def get_color(plot):
    return plot[3]

def get_value(plot):
    return plot[4]

def create_plot(id, hl, lr, color, value):
    return [id, hl, lr, color, value]

def add_plot(lst, plot):
    lst.append(plot)

def remove_plot(lst, pos):
    lst.pop(pos)

def list_plot(lst):
    for i in range (0, len(lst)):
        print(lst[i])

def compare_plots(plot1, plot2):
    '''
    This function compares two plots of land to see if they intersect.
    Input: plot1, plot2
    Preconditions: plot1, plot2 - plot objects, containing id, hl, lr, color and value
    Output: true or false
    Postconditions: true, if the plots overlap, or false otherwise
    '''
    if plot1[2][0]>plot2[1][0] and plot1[2][1]<plot2[1][1]:
        return True
    elif plot1[1][1]>plot2[2][1] and plot1[2][0]>plot2[1][0]:
        return True
    elif plot2[2][0]>plot1[1][0] and plot2[2][1]<plot1[1][1]:
        return True
    elif plot2[2][1]>plot1[1][1] and plot2[1][1]>plot1[2][1]:
        return True
    return False

def combine_plots(plot1, plot2):
    '''
    This function creates a new, big plot that is the combination of two smaller plots.
    Input: plot1, plot2
    Preconditions: plot1, plot2 - plot objects, containing id, hl, lr, color and value
    Output: plot'
    Postconditions: plot' = new plot of land using elements from the two smaller ones
    '''
    new_id=plot1[0]
    new_hl=plot1[1]
    new_lr=plot2[2]
    new_color="gray"
    new_value=(plot1[4]*abs((plot1[1][0]-plot1[2][0]))*abs((plot1[2][1]-plot1[2][1]))+plot2[4]*abs((plot2[1][0]-plot2[2][0]))*abs((plot2[2][1]-plot2[2][1])))/((abs((plot1[1][0]-plot1[2][0]))*abs((plot1[2][1]-plot1[2][1])))+abs((plot2[1][0]-plot2[2][0]))*abs((plot2[2][1]-plot2[2][1])))
    return create_plot(new_id, new_hl, new_lr, new_color, new_value)

def add_big_plot(lst, pos, new_plot):
    '''
    This function removes the smaller plot already existent in the list and adds the new, big one to the list.
    Input: lst, pos, new_plot
    Preconditions: lst - list of plots, pos - integer, new_plot - plot object
    Output: lst'
    Postconditions: lst' = lst, with a smaller plot removed and a big plot added
    '''
    big_plot = combine_plots(lst[pos], new_plot)
    lst.pop(pos)
    add_plot(lst, big_plot)

def compare_new_plot(lst, new_plot):
    for i in range (0, len(lst)):
        if compare_plots(lst[i], new_plot)==True:
            return i
    return -1

def ui_add(lst):
    id = input("Please insert the id.")
    left = input("Please input the x0 coord.")
    high = input("Please input the y0 coord")
    right = input("Please input the x1 coord.")
    down = input("Please input the y1 coord.")
    color = input("Please input the color")
    value = input("Please input the value")
    try:
        id = int(id)
        left = int(left)
        high = int(high)
        hl = create_coord(left, high)
        right = int(right)
        down = int(down)
        lr = create_coord(right, down)
        value = float(value)
        if (validate_input(id, hl, lr, color, value)):
            plot = create_plot(id, hl, lr, color, value)
            pos = compare_new_plot(lst, plot)
            if (pos == -1):
                add_plot(lst, plot)
            else:
                add_big_plot(lst, pos, plot)
        else:
            print("Your input is invalid! Try again.")
    except:
        print("One of the values is not valid! Try again.")

def run():
    lst=[]
    while True:
        x=input("What do you want to do?")
        if(x=="add"):
            ui_add(lst)
        elif(x=="list"):
            list_plot(lst)
        elif(x=="exit"):
            return

def test_add():
    lst=[]
    assert validate_input(12, [8, 9], [3, 3], "white", 3.5)==True
    assert validate_input(-1, [1, -4], [3, 5], "", 1.3)==False
    x=create_coord(1, 2)
    y=create_coord(5, 1)
    plot=create_plot(12, x, y, "blue", 1.2)
    add_plot(lst, plot)
    assert len(lst)==1
    remove_plot(lst, 0)
    assert len(lst)==0

def test_get():
    plot=[12, [2, 3], [10, 20], "red", 1.3]
    assert(get_id(plot))==12
    assert(get_hl(plot))==[2, 3]
    assert(get_lr(plot))==[10, 20]
    assert(get_color(plot))=="red"
    assert(get_value(plot))==1.3

def test_plots():
    lst=[]
    plot1=[12, [2, 3], [10, 20], "red", 1.3]
    plot2=[13, [4, 5], [20, 1], "red", 4.3]
    lst.append(plot1)
    assert compare_plots(plot1, plot2) == True
    assert compare_new_plot(lst, plot2) == 0


def test():
    test_get()
    test_add()
    test_plots()

test()
run()