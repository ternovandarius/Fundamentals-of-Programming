from rental import *

class RentalList:
    def __init__(self):
        self.__data=[]
        #self.__data.append(Rental("0", "0", date(2017, 12, 12), date(2017, 12, 19)))
        #self.__data.append(Rental("1", "2", date(2018, 6, 13), date(2018, 6, 20)))
        #self.__data[1].test_set_returned_date(date(2018, 6, 15))

    def add(self, bookId, clientId):
        rented_date= date.today()
        due_date= date.today() + timedelta(days=7)
        self.__data.append(Rental(bookId, clientId, rented_date, due_date))

    def available(self, x):
        ok=-1
        for i in range(0, len(self.__data)):
            if self.__data[i].get_book_id() == x and self.__data[i].get_returned_date() == "not returned yet":
                ok=i
        if ok!=-1:
            return ok
        else:
            return True

    def set_id(self, value, i):
        self.__data[i].set_id(value)

    def return_book(self, pos):
        self.__data[pos].set_rental_returned_date()

    def list(self):
        for i in range (0, len(self.__data)):
            self.__data[i].list_rental()

    def remove(self, i):
        self.__data.remove(self.__data[i])

    def ret_pos(self, x):
        for i in range (0, len(self.__data)):
            if x==self.__data[i].get_rental_id():
                return i
        return -1

    def get_pos_for_insert(self, x):
        if len(self.__data)==0:
            return 0
        elif len(self.__data)==1:
            return 1
        for i in range(0, len(self.__data)):
            y=self.__data[i].get_id()
            y=int(y)
            if x<y:
                return i
        return len(self.__data)

    def set_id(self, pos, value):
        self.__data[pos].set_id(value)

    def get_in(self):
        i=len(self.__data)-1
        a=self.__data[i].get_rental_id()
        b=self.__data[i].get_book_id()
        c=self.__data[i].get_client_id()
        d=self.__data[i].get_rented_date()
        e=self.__data[i].get_due_date()
        f=self.__data[i].get_returned_date()
        tup=[a, b, c, d, e, f]
        return tup

    def find_late(self):
        latelst=[0]*365
        ok=0
        for i in range (0, len(self.__data)):
            if self.__data[i].get_returned_date()=="not returned yet":
                y=self.__data[i].get_due_date()
                if y<date.today():
                    ok=1
                    lateday=abs((y-date.today()).days)
                    latelst[lateday]=i
        if ok==0:
            print("No late rentals!")
        else:
            for i in range(0, len(latelst), -1):
                if i!=0:
                    self.__data[latelst[i]].list_rental()

    def undo_return(self, i):
        self.__data[i].set_unreturned()

    def redo_remove(self, rid, rend, dued, retd):
        i=len(self.__data)-1
        self.__data[i].set_id(rid)
        self.__data[i].set_rented_date(rend)
        self.__data[i].set_due_date(dued)
        self.__data[i].set_returned_date(retd)

    def redo_return(self, i, retd):
        self.__data[i].set_returned_date(retd)

    def find_activity(self, l):
        actlst=[0]*l
        clientlst=[0]*l
        tup=[]
        for i in range (0, len(self.__data)):
            client=self.__data[i].get_client_id()
            client=int(client)
            if self.__data[i].get_returned_date()=="not returned yet":
                today=date.today()
                rent_date=self.__data[i].get_rented_date()
                number=today-rent_date
                nn=number.days
            else:
                rent_date=self.__data[i].get_rented_date()
                ret_date=self.__data[i].get_returned_date()
                number=ret_date-rent_date
                nn=number.days
            actlst[client]=actlst[client]+nn
            clientlst[client]=client
        for i in range (0, len(actlst)):
            tup.append((clientlst[i], actlst[i]))
        return sorted(tup, key=lambda x:x[1], reverse=True)

    def find_most_rented(self, l):
        booklst=[0]*l
        newlst=[0]*l
        tup=[]
        for i in range (0, len(self.__data)):
            book=self.__data[i].get_book_id()
            booklst[book]+=1
            newlst[book]=book
        for i in range (0, len(booklst)):
            tup.append((newlst[i], booklst[i]))
        return sorted(tup, key=lambda x:x[1], reverse=True)


class UndoRental:

    def __init__(self):
        self.__actions=[]

    def __len__(self):
        return len(self.__actions)

    def add_action(self, action):
        self.__actions.append(action)

    def get_type(self, i):
        return self.__actions[i][0]

    def get_id(self, i):
        return self.__actions[i][1]

    def get_rented_date(self, i):
        return self.__actions[i][4]

    def get_due_date(self, i):
        return self.__actions[i][5]

    def get_returned_date(self, i):
        return self.__actions[i][6]

    def get_book_id(self, i):
        return self.__actions[i][2]

    def get_client_id(self, i):
        return self.__actions[i][3]

    def pop_last_elem(self):
        self.__actions.pop()

class RedoRental:

    def __init__(self):
        self.__undid=[]

    def __len__(self):
        return len(self.__undid)

    def add_undid(self, action):
        self.__undid.append(action)

    def get_type(self, i):
        return self.__undid[i][0]

    def get_id(self, i):
        return self.__undid[i][1]

    def get_rented_date(self, i):
        return self.__undid[i][4]

    def get_due_date(self, i):
        return self.__undid[i][5]

    def get_returned_date(self, i):
        return self.__undid[i][6]

    def get_book_id(self, i):
        return self.__undid[i][2]

    def get_client_id(self, i):
        return self.__undid[i][3]

    def pop_last_elem(self):
        self.__undid.pop()