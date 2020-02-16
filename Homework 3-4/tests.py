from sub_1_add_insert import *
from sub_4_sum_prod import *
from sub_5_filter import *
from sub_6_undo import *

def test_read():
    x = "3+2i"
    assert read(x) == [3, 2]
    y = "-4-10i"
    assert read(y) == [-4, -10]

def test_create_complex():
    r = -4
    i = 25
    assert create_complex(r, i)==[-4, 25]

def test_get():
    c=[2, 3]
    assert get_Real(c)==2
    assert get_Imag(c)==3

def test_set():
    c=[-25, 30]
    set_Real(c, 12)
    set_Imag(c, 13)
    assert get_Real(c)==12
    assert get_Imag(c)==13

def test_add_insert():
    lst=[]
    c=create_complex(2, 0)
    d=create_complex(4, 1)
    e=create_complex(5, 5)
    add_to_list(lst, c)
    add_to_list(lst, d)
    insert_into_list(lst, e, 0)
    assert lst == [[5, 5], [2, 0], [4, 1]]

def test_list_real():
    lst=[[2, 0], [0, 1], [2, 3], [-4, 0], [2, 0]]
    assert list_real(lst, 1, 4) == [[-4, 0], [2, 0]]

def test_get_modulo():
    c=[3, 4]
    assert get_modulo(c)==5

def test_is_lower():
    c=create_complex(2, 3)
    m=10
    assert is_lower(c, m) == True

def test_find_lower():
    lst=[[1, 2], [0, 1], [-2, 3], [40, 14], [2, 9]]
    assert find_lower(lst, 5)==[[1, 2], [0, 1], [-2, 3]]

def test_is_equal():
    c=create_complex(3, 4)
    m=5
    assert is_equal(c, m) == True

def test_find_equal():
    lst=[[1, 2], [0, 1], [-2, 3], [4, 3], [2, 9]]
    assert find_equal(lst, 5)==[[4, 3]]

def test_is_greater():
    c=create_complex(2, 3)
    m=2
    assert is_greater(c, m) == True

def test_find_greater():
    lst=[[1, 2], [0, 1], [-2, 3], [40, 14], [2, 9]]
    assert find_greater(lst, 5)==[[40, 14], [2, 9]]

def test_remove():
    lst=[[1, 2], [0, 1], [-2, 3], [40, 14], [2, 9]]
    remove(lst, 1, 3)
    assert lst==[[1, 2], [2, 9]]

def test_replace():
    lst = [[1, 2], [0, 1], [-2, 3], [40, 14], [2, 9], [0, 1]]
    replace(lst, [0, 1], [7, 7])
    assert lst==[[1, 2], [7, 7], [-2, 3], [40, 14], [2, 9], [7, 7]]

def test_calc():
    lst = [[1, 2], [0, 1], [-2, 3], [40, 14], [2, 9]]
    assert calc_sum(lst, 1, 4) == [40, 27]
    assert calc_prod(lst, 0, 2) == [0, 6]

def test_filter_real():
    lst = [[1, 1], [2, 3], [4, 0], [5, 1], [6, 0]]
    lst=filter_real(lst)
    assert lst==[[4, 0], [6, 0]]

def test_undo():
    lst = [[1, 1], [2, 3]]
    biglst = [[[1, 1]], [[1, 1], [2, 3]]]
    tup = list_undo(lst, biglst)
    lst = tup[0]
    biglst = tup[1]
    assert lst == [[1, 1]]
    assert biglst == [[[1, 1]]]
    tup = list_undo (lst, biglst)
    lst = tup[0]
    biglst = tup[1]
    assert lst == []
    assert biglst == []

def test():
    test_read()
    test_create_complex()
    test_get()
    test_set()
    test_add_insert()
    test_list_real()
    test_get_modulo()
    test_is_lower()
    test_find_lower()
    test_is_equal()
    test_find_equal()
    test_is_greater()
    test_find_greater()
    test_remove()
    test_replace()
    test_calc()
    test_filter_real()
    test_undo()