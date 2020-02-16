class Book:
    b_id=0

    def __init__(self, title, desc, author):
        self.__bookId=Book.b_id
        Book.b_id += 1
        self.__title=title
        self.__desc=desc
        self.__author=author

    def get_id(self):
        return self.__bookId

    def get_title(self):
        return self.__title

    def get_desc(self):
        return self.__desc

    def get_author(self):
        return self.__author

    def set_title(self, new_title):
        self.__title=new_title

    def set_desc(self, new_desc):
        self.__desc=new_desc

    def set_author(self, new_author):
        self.__author=new_author

    def set_id(self, value):
        self.__bookId=value

    def print_book(self):
        print(self.__bookId, end=", ")
        print(self.__title, end=", ")
        print(self.__desc, end=", ")
        print(self.__author)