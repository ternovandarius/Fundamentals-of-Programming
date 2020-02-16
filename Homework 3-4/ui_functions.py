from tests import *

def ui_add(lst, biglst, x):
    try:
        y = read(x)
        c = create_complex(y[0], y[1])
        add_to_list(lst, c)
        biglst.append(lst[:])
    except:
        print("Invalid syntax! Correct syntax: add [value]")

def ui_insert(lst, biglst, x, z):
    try:
        y = read(x)
        c = create_complex(y[0], y[1])
        insert_into_list(lst, c, int(z))
        biglst.append(lst[:])
    except:
        print("Invalid syntax! Correct syntax: insert [value] at [position]")

def ui_list(lst, x):
    try:
        if len(x) > 1:
            if x[1] == "real":
                rlst = list_real(lst, int(x[2]), int(x[4]))
                print_list(rlst)
            elif x[1] == "modulo":
                m = int(x[3])
                if x[2] == "<":
                    print_list(find_lower(lst, m))
                elif x[2] == "=":
                    eqlst = find_equal(lst, m)
                    print_list(eqlst)
                elif x[2] == ">":
                    grtlst = find_greater(lst, m)
                    print_list(grtlst)
        else:
            print_list(lst)
    except:
        print(
            "Invalid syntax! Correct syntax: list OR list real [start position] to [end position] OR list modulo [< = >] [value]")

def ui_remove(lst, biglst, x):
    try:
        if len(x) > 2:
            remove(lst, int(x[1]), int(x[3]))
        else:
            remove(lst, int(x[1]), int(x[1]))
        biglst.append(lst[:])
    except Exception as ve:
        print(ve)

def ui_replace(lst, biglst, x):
    try:
        y = read(x[1])
        z = read(x[3])
        replace(lst, y, z)
        biglst.append(lst[:])
    except Exception as e:
        print(e)

def ui_sum(lst, x):
