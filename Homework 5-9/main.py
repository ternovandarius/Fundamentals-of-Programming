from booklist import *
from clientlist import *
from rentallist import *
from tests import *
from ui import *


def run():
    b_list=BookList()
    c_list=ClientList()
    r_list=RentalList()
    cu_list=UndoClient()
    cr_list=RedoClient()
    bu_list=UndoBook()
    br_list=RedoBook()
    ru_list=UndoRental()
    rr_list=RedoRental()
    while True:
        x=input("Please enter your command.")
        if x=="add book":
            ui_add_book(b_list, bu_list)
        elif x=="list book":
            b_list.list()
        elif x=="remove book":
            ui_remove_book(b_list, bu_list)
        elif x=="update book":
            ui_update_book(b_list, bu_list)
        elif x=="add client":
            ui_add_client(c_list, cu_list)
        elif x=="list client":
            c_list.list()
        elif x=="update client":
            ui_update_client(c_list, cu_list)
        elif x=="remove client":
            ui_remove_client(c_list, cu_list)
        elif x=="rent book":
            ui_rent_book(b_list, c_list, r_list, ru_list)
        elif x=="list rent":
            r_list.list()
        elif x=="return book":
            ui_return_book(b_list, r_list, ru_list)
        elif x=="search client":
            ui_search_client(c_list)
        elif x=="search book":
            ui_search_book(b_list)
        elif x=="test":
            b_list.test()
            c_list.test()
        elif x=="stats":
            y=input("Which stats do you want to see? Most <rented> books, Most <active> clients, Most rented <author> or <late> rentals?")
            if y=="late":
                r_list.find_late()
            elif y=="active":
                l=c_list.return_len()
                newlst=r_list.find_activity(l)
                for i in range (0, len(newlst)):
                    if newlst[i][1]!=0:
                        elem=newlst[i][0]
                        c_list.print_elem(elem)
            elif y=="rented":
                l=b_list.return_len()
                newlst=r_list.find_most_rented(l)
                for i in range (0, len(newlst)):
                    if newlst[i][1]!=0:
                        elem=newlst[i][0]
                        b_list.print_elem(elem)
            elif y=="author":
                l=b_list.return_len()
                newlst=r_list.find_most_rented(l)
                for i in range (0, len(newlst)):
                    if newlst[i][1]!=0:
                        elem=newlst[i][0]
                        b_list.print_author(elem)
        elif x=="undo client":
            ui_undo_client(c_list, cu_list, cr_list)
        elif x=="redo client":
            ui_redo_client(c_list, cu_list, cr_list)
        elif x=="undo book":
            ui_undo_book(b_list, bu_list, br_list)
        elif x=="redo book":
            ui_redo_book(b_list, bu_list, br_list)
        elif x=="undo rent":
            ui_undo_rental(r_list, ru_list, rr_list)
        elif x=="redo rent":
            ui_redo_rental(r_list, ru_list, rr_list)
        elif x=="exit":
            return

#tests()
run()
