from ui import *


def test_books():
    b=BookList()
    b.add("a", "b", "c")
    b.add("b", "c", "d")
    assert b[0].get_title=="a"
    assert b[1].get_author=="d"
    y=0
    i=b.find(y)
    b.remove(i)
    assert b[1].get_desc==""
    b.update_title(0, "asd")
    assert b[0].get_title()=="asd"


def test_clients():
    c=ClientList
    x="gigel"
    c.add(x)

def tests():
    test_books()