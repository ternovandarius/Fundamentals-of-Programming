from book import *

class BookList:
    def __init__(self):
        self.__data=[]

    def test(self):
        self.__data.append(Book("The Lord of The Rings: The Fellowship of the Ring", "Hobbits do things", "J. R. R. Tolkien"))
        self.__data.append(Book("The Catcher in the Rye", "Holden Caulfield does things", "J. D. Salinger"))
        self.__data.append(Book("The Odyssey", "Odysseus does things", "Homer"))
        self.__data.append(Book("Dictionary", "Words...don't do things", "Oxford"))
        self.__data.append(Book("The Lord of The Rings: The Two Towers", "Hobbits do things again", "J. R. R. Tolkien"))
        self.__data.append(Book("The Lord of The Rings: Return of the King", "Hobbits do things one last time", "J. R. R. Tolkien"))

    def add(self, title, desc, author):
        self.__data.append(Book(title, desc, author))

    def return_len(self):
        return len(self.__data)

    def list(self):
        for i in range (0, len(self.__data)):
            self.__data[i].print_book()

    def print_author(self, i):
        x=self.__data[i].get_author()
        print(x)

    def print_elem(self, i):
        self.__data[i].print_book()

    def find(self, x):
        for i in range (0, len(self.__data)):
            y=self.__data[i].get_id()
            y=int(y)
            if y == x:
                return i
        return -1

    def update_title(self, i, new_title):
        try:
            self.__data[i].set_title(new_title)
        except Exception as e:
            print (e)

    def update_desc(self, i, new_desc):
        try:
            self.__data[i].set_desc(new_desc)
        except Exception as e:
            print (e)

    def update_author(self, i, new_author):
        try:
            self.__data[i].set_author(new_author)
        except Exception as e:
            print (e)

    def remove(self, i):
        try:
            self.__data.remove(self.__data[i])
        except Exception as e:
            print (e)


    def search_id(self, s_id):
        ok=False
        for i in range (0, len(self.__data)):
            x=s_id.lower()
            y=self.__data[i].get_id()
            y=str(y)
            y=y.lower()
            if x in y:
                ok=True
                self.__data[i].print_book()
        if ok==False:
            print("The selected id does not exist!")

    def search_title(self, s_title):
        ok=False
        for i in range (0, len(self.__data)):
            x=s_title.lower()
            y=self.__data[i].get_title()
            y=str(y)
            y=y.lower()
            if x in y:
                ok=True
                self.__data[i].print_book()
        if ok==False:
            print("The selected title does not exist!")

    def search_desc(self, s_desc):
        ok=False
        for i in range (0, len(self.__data)):
            x=s_desc.lower()
            y=self.__data[i].get_desc()
            y=str(y)
            y=y.lower()
            if x in y:
                ok=True
                self.__data[i].print_book()
        if ok==False:
            print("The selected description does not exist!")

    def search_author(self, s_author):
        ok=False
        for i in range (0, len(self.__data)):
            x=s_author.lower()
            y=self.__data[i].get_author()
            y=str(y)
            y=y.lower()
            if x in y:
                ok=True
                self.__data[i].print_book()
        if ok==False:
            print("The selected author does not exist!")

    def get_in_targeted(self, i):
        one=self.__data[i].get_id()
        two=self.__data[i].get_title()
        three=self.__data[i].get_desc()
        four=self.__data[i].get_author()
        tup=[one, two, three, four]
        return tup

    def get_in(self):
        i=len(self.__data)-1
        one=self.__data[i].get_id()
        two=self.__data[i].get_title()
        three=self.__data[i].get_desc()
        four=self.__data[i].get_author()
        tup=[one, two, three, four]
        return tup

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

    def insert(self, pos, id, title, desc, author):
        self.__data.insert(pos, Book(title, desc, author))
        self.__data[pos].set_id(id)

    def set_id(self, pos, value):
        self.__data[pos].set_id(value)

class UndoBook:
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

    def get_title(self, i):
        return self.__actions[i][2]

    def get_desc(self, i):
        return self.__actions[i][3]

    def get_author(self, i):
        return self.__actions[i][4]

    def pop_last_elem(self):
        self.__actions.pop()


class RedoBook:

    def __init__(self):
        self.__undid=[]

    def __len__(self):
        return len(self.__undid)

    def add_undid(self, undid):
        self.__undid.append(undid)

    def get_type(self, i):
        return self.__undid[i][0]

    def get_id(self, i):
        return self.__undid[i][1]

    def get_title(self, i):
        return self.__undid[i][2]

    def get_desc(self, i):
        return self.__undid[i][3]

    def get_author(self, i):
        return self.__undid[i][4]

    def pop_last_elem(self):
        self.__undid.pop()