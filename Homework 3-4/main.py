from ui_functions import *


def run():
    biglst=[]
    lst=[]
    while True:
        txt=input("What do you want to do?")
        x=txt.split(" ")
        if x[0]=="add":
            ui_add(lst, biglst, x[1])
        elif x[0]=="insert":
            ui_insert(lst, biglst, x[1], x[3])
        elif x[0]=="list":
            ui_list(lst, x)
        elif x[0]=="remove":
            ui_remove(lst, biglst, x)
        elif x[0]=="replace":
            ui_replace(lst, biglst, x)
        elif x[0]=="sum":
            try:
                s=calc_sum(lst, int(x[1]), int(x[3]))
                print_complex(s)
            except Exception as e:
                print (e)
        elif x[0]=="product":
            try:
                p=calc_prod(lst, int(x[1]), int(x[3]))
                print_complex(p)
            except Exception as e:
                print (e)
        elif x[0]=="filter":
            try:
                if x[1]=="real":
                    lst=filter_real(lst)
                elif x[1]=="modulo":
                    m = int(x[3])
                    if x[2] == "<":
                        lst = filter_modulo_less(lst, m)
                    elif x[2] == "=":
                        lst = filter_modulo_equal(lst, m)
                    elif x[2] == ">":
                        lst = filter_modulo_great(lst, m)
                biglst.append(lst[:])
            except Exception as e:
                print (e)
        elif x[0]=="undo":
            try:
                tup=list_undo(lst, biglst)
                lst=tup[0]
                biglst=tup[1]
            except Exception as e:
                print (e)
        elif x[0]=="exit":
            return
        else:
            print("Please input a valid command!")

test()
run()