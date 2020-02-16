from client import *

class ClientList:

    def __init__(self):
        self.__undolist=UndoClient
        self.__data=[]

    def test(self):
        self.__data.append(Client("Joe"))
        self.__data.append(Client("Jack"))
        self.__data.append(Client("Jill"))
        self.__data.append(Client("Maria"))
        self.__data.append(Client("Mike"))

    def add(self, name):
        self.__data.append(Client(name))

    def get_in(self):
        l = len(self.__data) - 1
        x = self.__data[l].get_id()
        y = self.__data[l].get_name()
        return (x, y)

    def get_in_targeted(self, i):
        x=self.__data[i].get_id()
        y=self.__data[i].get_name()
        return (x,y)

    def set_fwd_id(self):
        Client.set_fwd_id()

    def print_elem(self, i):
        self.__data[i].print_client()

    def return_len(self):
        return len(self.__data)

    def list(self):
        for i in range(0, len(self.__data)):
            self.__data[i].print_client()

    def find(self, x):
        for i in range (0, len(self.__data)):
            y= self.__data[i].get_id()
            y=int(y)
            if y == x:
                return i
        return -1

    def search_id(self, s_id):
        ok=False
        for i in range (0, len(self.__data)):
            x=s_id.lower()
            y=self.__data[i].get_id()
            y=str(y)
            y=y.lower()
            if x in y:
                ok=True
                self.__data[i].print_client()
        if ok==False:
            print("The selected id does not exist!")

    def set_back_id(self):
        Client.set_back_id()

    def search_name(self, s_name):
        ok=False
        for i in range (0, len(self.__data)):
            x=s_name.lower()
            y=self.__data[i].get_name()
            y=str(y)
            y=y.lower()
            if x in y:
                ok=True
                self.__data[i].print_client()
        if ok==False:
            print("The selected name does not exist!")


    def remove(self, i):
        self.__data.remove(self.__data[i])

    def undo_remove(self, i):
        self.__data.remove(self.__data[i])

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

    def insert(self, pos, id, name):
        self.__data.insert(pos, Client(name))
        self.__data[pos].set_id(id)


    def update_name(self, i, new_name):
        try:
            self.__data[i].set_name(new_name)
        except Exception as e:
            print (e)



class UndoClient:

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

    def get_name(self, i):
        return self.__actions[i][2]

    def pop_last_elem(self):
        self.__actions.pop()

class RedoClient:

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

    def get_name(self, i):
        return self.__undid[i][2]

    def pop_last_elem(self):
        self.__undid.pop()