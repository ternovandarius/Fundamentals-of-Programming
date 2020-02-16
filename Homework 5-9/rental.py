from datetime import *

class Rental:
    r_id=0

    def __init__(self, bookId, clientId, rented_date, due_date):
        self.__rentalId=Rental.r_id
        Rental.r_id += 1
        self.__bookId=bookId
        self.__clientId=clientId
        self.__rented_date=rented_date
        self.__due_date=due_date
        self.__returned_date="not returned yet"

    def get_rental_id(self):
        return self.__rentalId

    def get_book_id(self):
        return self.__bookId

    def get_returned_date(self):
        return self.__returned_date

    def get_due_date(self):
        return self.__due_date

    def get_client_id(self):
        return self.__clientId

    def get_rented_date(self):
        return self.__rented_date

    def get_due_date(self):
        return self.__due_date

    def get_returned_date(self):
        return self.__returned_date

    def set_id(self, x):
        self.__rentalId=x

    def set_rental_returned_date(self):
        returned_date = date.today()
        self.__returned_date=returned_date

    def set_rented_date(self, x):
        self.__rented_date=x

    def set_due_date(self, x):
        self.__due_date=x

    def set_returned_date(self, x):
        self.__returned_date=x

    def set_unreturned(self):
        self.__returned_date="not returned yet"

    def set_id(self, value):
        self.__rentalId=value


    def list_rental(self):
        print(self.__rentalId, end=", ")
        print(self.__bookId, end=", ")
        print(self.__clientId, end=", ")
        print(self.__rented_date, end=", ")
        print(self.__due_date, end=", ")
        print(self.__returned_date)