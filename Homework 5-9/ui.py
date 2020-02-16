from booklist import *
from clientlist import *
from rentallist import *

def ui_add_book(b_list, bu_list):
    '''
    This function adds a "Book" object into the b_list.
    Input: b_list
    Preconditions: b_list = list of books
    Output: b_list'
    Postconditions: b_list' = b_list+ new book object
    '''
    a = input("Please input the name of the book.")
    b = input("Please input the description of the book.")
    c = input("Please input the author of the book")
    b_list.add(a, b, c)
    tup = b_list.get_in()
    x = tup[0]
    y = tup[1]
    z = tup[2]
    a = tup[3]
    bu_list.add_action(("add", x, y, z, a))

def ui_remove_book(b_list, bu_list):
    '''
    This function removes a "Book" object from the b_list.
    Input: b_list
    Preconditions: b_list - list of books
    Output: b_list'
    Postconditions: b_list'=b_list - a book object
    '''
    y = input("Please input the id of the book you want to remove.")
    i = b_list.find(int(y))
    tup = b_list.get_in_targeted(i)
    one = tup[0]
    two = tup[1]
    three = tup[2]
    four = tup[3]
    bu_list.add_action(("remove", one, two, three, four))
    b_list.remove(i)

def ui_update_book(b_list, bu_list):
    '''
    This list updates a certain parameter of a "Book" object.
    Input: b_list
    Preconditions: b_list - list of books
    Output: b_list'
    Postconditions: b_list' = b_list, but with an element changed
    '''
    z = input("Please enter the id of the book you want to update.")
    z = int(z)
    i = b_list.find(z)
    y = input("What do you want to update?")
    tup = b_list.get_in_targeted(i)
    a=tup[0]
    b=tup[1]
    c=tup[2]
    d=tup[3]
    if y == "title":
        q = input("Please enter the new title.")
        bu_list.add_action(("updatet", a, b, c, d))
        b_list.update_title(i, q)
    elif y == "desc":
        q = input("Please enter the new description.")
        bu_list.add_action(("updated", a, b, c, d))
        b_list.update_desc(i, q)
    elif y == "author":
        q = input("Please enter the new author.")
        bu_list.add_action(("updatea", a, b, c, d))
        b_list.update_author(i, q)

def ui_add_client(c_list, cu_list):
    '''
    This function adds a "Client" object to c_list.
    Input: c_list
    Preconditions: c_list - list of clients
    Output: c_list'
    Postconditions: c_list'=c_list + new client
    '''
    y = input("Please input the name of the client.")
    c_list.add(y)
    tup=c_list.get_in()
    x=tup[0]
    y=tup[1]
    cu_list.add_action(("add", x, y))

def ui_update_client(c_list, cu_list):
    '''
    This function changes the name of a client object in c_list.
    Input: c_list
    Preconditions: c_list - list of clients
    Output: c_list'
    Postconditions: c_list' = c_list, with one element changed
    '''
    y = input("Please enter the id of the client you want to update.")
    y = int(y)
    i = c_list.find(y)
    z = input("Please enter the new name.")
    tup=c_list.get_in_targeted(i)
    x=tup[0]
    y=tup[1]
    cu_list.add_action(("update", x, y))
    c_list.update_name(i, z)

def ui_remove_client(c_list, cu_list):
    '''
    This functions removes a "client" object from c_list.
    Input: c_list
    Preconditions: c_list - list of clients
    Output: c_list'
    Postconditions: c_list' = c_list - one client
    '''
    y = input("Please enter the id of the client you want to remove.")
    y = int(y)
    i = c_list.find(y)
    tup = c_list.get_in_targeted(i)
    one = tup[0]
    two = tup[1]
    cu_list.add_action(("remove", one, two))
    c_list.remove(i)

def ui_rent_book(b_list, c_list, r_list, ru_list):
    '''
    This function creates an entry in r_list.
    Input: b_list, c_list, r_list
    Preconditions: b_list - list of books, c_list - list of clients, r_list - list of rentals
    Output: r_list'
    Postconditions: r_list' = r_list + new rental entry
    '''
    a = input("Please enter the id of the book you want to rent.")
    a = int(a)
    i = b_list.find(a)
    j = r_list.available(a)
    if i != -1 and j == True:
        b = input("Please enter your client id.")
        b = int(b)
        k = c_list.find(b)
        if k != -1:
            r_list.add(a, b)
            tup=r_list.get_in()
            one=tup[0]
            two=tup[1]
            three=tup[2]
            four=tup[3]
            five=tup[4]
            six=tup[5]
            ru_list.add_action(("rent", one, two, three, four, five, six))
        else:
            print("This user ID does not exist!")
    else:
        print("This book is unavailable.")

def ui_return_book(b_list, r_list, ru_list):
    '''
    This function modifies an entry in the r_list.
    Input: b_list, r_list
    Preconditions: b_list - list of books, r_list - list of rentals
    Output: r_list'
    Postconditions: r_list' = r_list with one element modified
    '''
    y = input("Input the id of the book you want to return.")
    y = int(y)
    i = b_list.find(y)
    if i != -1:
        j = r_list.available(y)
        if j != True:
            r_list.return_book(j)
            tup = r_list.get_in()
            one = tup[0]
            two = tup[1]
            three = tup[2]
            four = tup[3]
            five = tup[4]
            six = tup[5]
            ru_list.add_action(("return", one, two, three, four, five, six))
        else:
            print("This book is already returned!")
    else:
        print("This book does not exist!")

def ui_search_client(c_list):
    y = input("What do you want to search by? Id or name?")
    y = y.lower()
    if y == "id":
        s_id = input("Please enter the desired id.")
        c_list.search_id(s_id)
    elif y == "name":
        s_name = input("Please enter the desired name")
        c_list.search_name(s_name)

def ui_search_book(b_list):
    y = input("What do you want to search it by: <id> <title> <description> or <author>?")
    if y == "id":
        s_id = input("Please enter the desired id")
        b_list.search_id(s_id)
    elif y == "title":
        s_title = input("Please enter the desired title")
        b_list.search_title(s_title)
    elif y == "description":
        s_desc = input("Please enter the desired description")
        b_list.search_desc(s_desc)
    elif y == "author":
        s_author = input("Please enter the desired author")
        b_list.search_author(s_author)

def ui_undo_client(c_list, cu_list, cr_list):
    i = len(cu_list)
    if i <= 0:
        print("No more actions to undo!")
    else:
        i = i - 1
        if cu_list.get_type(i) == "add":
            # then we need to remove
            new_obj=("remove", cu_list.get_id(i), cu_list.get_name(i))
            cr_list.add_undid(new_obj)
            c_list.remove(i)
            cu_list.pop_last_elem()
            #c_list.set_back_id()
        elif cu_list.get_type(i) == "remove":
            #then we need to insert it back into its place
            x=cu_list.get_id(i)
            pos=c_list.get_pos_for_insert(x)
            y=cu_list.get_name(i)
            c_list.insert(pos, x, y)
            new_obj=("add", cu_list.get_id(i), cu_list.get_name(i))
            cr_list.add_undid(new_obj)
            cu_list.pop_last_elem()
            #c_list.set_fwd_id()
        elif cu_list.get_type(i) == "update":
            #then we need to update it to its previous state
            x=cu_list.get_id(i)
            y=cu_list.get_name(i)
            cu_list.pop_last_elem()
            z=c_list.find(x)
            tup=c_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_obj = ("update", new_id, new_name)
            cr_list.add_undid(new_obj)
            c_list.update_name(z, y)

def ui_redo_client(c_list, cu_list, cr_list):
    i=len(cr_list)
    if i<=0:
        print("No actions to redo!")
    else:
        i = i - 1
        if cr_list.get_type(i) == "add":
            # then we need to remove
            new_obj = ("remove", cr_list.get_id(i), cr_list.get_name(i))
            cu_list.add_action(new_obj)
            c_list.remove(i)
            cr_list.pop_last_elem()
            # c_list.set_back_id()
        elif cr_list.get_type(i) == "remove":
            # then we need to insert it back into its place
            x = cr_list.get_id(i)
            pos = c_list.get_pos_for_insert(x)
            y = cr_list.get_name(i)
            c_list.insert(pos, x, y)
            new_obj = ("add", cr_list.get_id(i), cr_list.get_name(i))
            cu_list.add_action(new_obj)
            cr_list.pop_last_elem()
            # c_list.set_fwd_id()
        elif cr_list.get_type(i) == "update":
            # then we need to update it to its previous state
            x = cr_list.get_id(i)
            y = cr_list.get_name(i)
            cr_list.pop_last_elem()
            z = c_list.find(x)
            tup = c_list.get_in_targeted(z)
            new_id = tup[0]
            new_name = tup[1]
            new_obj = ("update", new_id, new_name)
            cu_list.add_action(new_obj)
            c_list.update_name(z, y)

def ui_undo_book(b_list, bu_list, br_list):
    i = len(bu_list)
    if i <= 0:
        print("No more actions to undo!")
    else:
        i = i - 1
        if bu_list.get_type(i) == "add":
            # then we need to remove
            new_obj=("remove", bu_list.get_id(i), bu_list.get_title(i), bu_list.get_desc(i), bu_list.get_author(i))
            br_list.add_undid(new_obj)
            b_list.remove(i)
            bu_list.pop_last_elem()
            #b_list.set_back_id()
        elif bu_list.get_type(i) == "remove":
            #then we need to insert it back into its place
            x=bu_list.get_id(i)
            pos=b_list.get_pos_for_insert(x)
            y=bu_list.get_title(i)
            z=bu_list.get_desc(i)
            a=bu_list.get_author(i)
            b_list.insert(pos, x, y, z, a)
            new_obj=("add", bu_list.get_id(i), bu_list.get_title(i), bu_list.get_desc(i), bu_list.get_author(i))
            br_list.add_undid(new_obj)
            bu_list.pop_last_elem()
            #b_list.set_fwd_id()
        elif bu_list.get_type(i) == "updatet":
            #then we need to update it to its previous state
            x=bu_list.get_id(i)
            y=bu_list.get_title(i)
            bu_list.pop_last_elem()
            z=b_list.find(x)
            tup=b_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_desc=tup[2]
            new_author=tup[3]
            new_obj = ("updatet", new_id, new_name, new_desc, new_author)
            br_list.add_undid(new_obj)
            b_list.update_title(z, y)
        elif bu_list.get_type(i) == "updated":
            #then we need to update it to its previous state
            x=bu_list.get_id(i)
            y=bu_list.get_title(i)
            bu_list.pop_last_elem()
            z=b_list.find(x)
            tup=b_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_desc=tup[2]
            new_author=tup[3]
            new_obj = ("updated", new_id, new_name, new_desc, new_author)
            br_list.add_undid(new_obj)
            b_list.update_desc(z, y)
        elif bu_list.get_type(i) == "updatea":
            #then we need to update it to its previous state
            x=bu_list.get_id(i)
            y=bu_list.get_title(i)
            bu_list.pop_last_elem()
            z=b_list.find(x)
            tup=b_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_desc=tup[2]
            new_author=tup[3]
            new_obj = ("updatea", new_id, new_name, new_desc, new_author)
            br_list.add_undid(new_obj)
            b_list.update_author(z, y)

def ui_redo_book(b_list, bu_list, br_list):
    i = len(br_list)
    if i <= 0:
        print("No more actions to redo!")
    else:
        i = i - 1
        if br_list.get_type(i) == "add":
            # then we need to remove
            new_obj=("remove", br_list.get_id(i), br_list.get_title(i), br_list.get_desc(i), br_list.get_author(i))
            bu_list.add_actions(new_obj)
            b_list.remove(i)
            br_list.pop_last_elem()
            #b_list.set_back_id()
        elif br_list.get_type(i) == "remove":
            #then we need to insert it back into its place
            x=br_list.get_id(i)
            pos=b_list.get_pos_for_insert(x)
            y=br_list.get_title(i)
            z=br_list.get_desc(i)
            a=br_list.get_author(i)
            b_list.insert(pos, x, y, z, a)
            new_obj=("add", br_list.get_id(i), br_list.get_title(i), br_list.get_desc(i), br_list.get_author(i))
            bu_list.add_action(new_obj)
            br_list.pop_last_elem()
            #b_list.set_fwd_id()
        elif br_list.get_type(i) == "updatet":
            #then we need to update it to its previous state
            x=br_list.get_id(i)
            y=br_list.get_title(i)
            br_list.pop_last_elem()
            z=b_list.find(x)
            tup=b_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_desc=tup[2]
            new_author=tup[3]
            new_obj = ("updatet", new_id, new_name, new_desc, new_author)
            bu_list.add_action(new_obj)
            b_list.update_title(z, y)
        elif br_list.get_type(i) == "updated":
            #then we need to update it to its previous state
            x=br_list.get_id(i)
            y=br_list.get_title(i)
            br_list.pop_last_elem()
            z=b_list.find(x)
            tup=b_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_desc=tup[2]
            new_author=tup[3]
            new_obj = ("updated", new_id, new_name, new_desc, new_author)
            bu_list.add_action(new_obj)
            b_list.update_desc(z, y)
        elif br_list.get_type(i) == "updatea":
            #then we need to update it to its previous state
            x=br_list.get_id(i)
            y=br_list.get_title(i)
            br_list.pop_last_elem()
            z=b_list.find(x)
            tup=b_list.get_in_targeted(z)
            new_id=tup[0]
            new_name=tup[1]
            new_desc=tup[2]
            new_author=tup[3]
            new_obj = ("updatea", new_id, new_name, new_desc, new_author)
            bu_list.add_action(new_obj)
            b_list.update_author(z, y)


def ui_undo_rental(r_list, ru_list, rr_list):
    i = len(ru_list)
    if i <= 0:
        print("No more actions to undo!")
    else:
        i = i - 1
        if ru_list.get_type(i) == "rent":
            # then we need to remove
            new_obj=("remove", ru_list.get_id(i), ru_list.get_book_id(i), ru_list.get_client_id(i), ru_list.get_rented_date(i), ru_list.get_due_date(i), ru_list.get_returned_date(i))
            rr_list.add_undid(new_obj)
            r_list.remove(i)
            ru_list.pop_last_elem()
            #r_list.set_back_id()
        elif ru_list.get_type(i) == "return":
            #then we need to insert it back into its place
            x=ru_list.get_id(i)
            new_obj=("unreturn", ru_list.get_id(i), ru_list.get_book_id(i), ru_list.get_client_id(i), ru_list.get_rented_date(i), ru_list.get_due_date(i), ru_list.get_returned_date(i))
            r_list.undo_return(x)
            rr_list.add_undid(new_obj)
            ru_list.pop_last_elem()
            #r_list.set_fwd_id()

def ui_redo_rental(r_list, ru_list, rr_list):
    i = len(rr_list)
    if i <= 0:
        print("No more actions to redo!")
    else:
        i = i - 1
        if rr_list.get_type(i) == "remove":
            new_obj=("rent", rr_list.get_id(i), rr_list.get_book_id(i), rr_list.get_client_id(i), rr_list.get_rented_date(i), rr_list.get_due_date(i), rr_list.get_returned_date(i))
            ru_list.add_action(new_obj)
            r_list.add(rr_list.get_book_id(i), rr_list.get_client_id(i))
            r_list.redo_remove(rr_list.get_id(i), rr_list.get_rented_date(i), rr_list.get_due_date(i), rr_list.get_returned_date(i))
            rr_list.pop_last_elem()
            #r_list.set_back_id()
        elif rr_list.get_type(i) == "unreturn":
            x=rr_list.get_id(i)
            new_obj=("return", rr_list.get_id(i), rr_list.get_book_id(i), rr_list.get_client_id(i), rr_list.get_rented_date(i), rr_list.get_due_date(i), rr_list.get_returned_date(i))
            y=r_list.ret_pos(rr_list.get_id(i))
            r_list.redo_return(y, rr_list.get_returned_date(i))
            ru_list.add_action(new_obj)
            rr_list.pop_last_elem()
            #r_list.set_fwd_id()
