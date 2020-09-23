import datetime
import re
from get_set import get_day, get_trans, get_value, get_type, get_descr, set_value
from functions import create_storage, create_df_storage, add, insert, remove, remove_to, remove_type, replace, write, type_sum


################################################################################
#***********************************   TESTS    ********************************
################################################################################

def test_get_day():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    assert get_day(storage, 23) == [[100, "out", "pizza"],[1000, "in", "salary"]], 'should get [[100, "out", "pizza"],[1000, "in", "salary"]]'

def test_get_trans():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    
    assert get_trans(storage, 23, 0) == [100, "out", "pizza"], 'should get [100, "out", "pizza"]'
    assert get_trans(storage, 23, 1) == [1000, "in", "salary"], 'should get [1000, "in", "salary"]'

def test_get_value():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    assert get_value(storage, 23, 0) == 100, 'should get 100'
    assert get_value(storage, 23, 1) == 1000, 'should get 1000'

def test_get_type():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    assert get_type(storage, 23, 0) == "out", 'should get "out"'
    assert get_type(storage, 23, 1) == "in", 'should get "in"'

def test_get_descr():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    assert get_descr(storage, 23, 0) == "pizza", 'should get "pizza"'
    assert get_descr(storage, 23, 1) == "salary", 'should get "salary"'

def test_get_descr():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    assert get_descr(storage, 23, 0) == "pizza", 'should get "pizza"'
    assert get_descr(storage, 23, 1) == "salary", 'should get "salary"'

def test_set_value():
    storage = {23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    set_value(storage, 23, 0, 150)
    set_value(storage, 23, 1, 1050)
    assert get_value(storage, 23, 0) == 150, 'should get 150'
    assert get_value(storage, 23, 1) == 1050, 'should get 1050'

def test_create_storage():
    storage = {}
    create_storage(storage)
    assert len(storage) == 31, 'should be "30"'
    for i in range(31):
        assert storage[i] == [], 'should be empty []'

def test_add():
    day = datetime.date.today().day
    storage = {day:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    add(storage, 150, "out", "jewlery")
    assert get_trans(storage, day, 2) == [150, "out", "jewlery"]

def test_insert():
    day = 23
    storage = {day:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    insert(storage, 23, 150, "out", "jewlery")
    assert get_trans(storage, day, 2) == [150, "out", "jewlery"]

def test_remove():
    storage = {22:[], 23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    remove(storage, 23)
    assert len(storage[23]) == 0

def test_remove_to():
    storage = {21:[1000, "in", "salary"],22:[[100, "out", "pizza"]], 23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    remove_to(storage, 21, 22)
    assert len(storage[21]) == 0
    assert len(storage[22]) == 0

def test_remove_type():
    storage = {22:[], 23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    remove(storage, 23)
    remove(storage, 22)
    assert len(storage[23]) == 0
    assert len(storage[22]) == 0

def test_replace():
    storage = {22:[], 23:[[100, "out", "pizza"],[1000, "in", "salary"]]}
    replace(storage, ["replace", "23", "in", "salary", "with", "1050"])
    assert get_value(storage, 23, 1) == 1050
    
def test_type_sum():
    storage = {21:[1000, "in", "salary"],22:[[100, "out", "pizza"]], 23:[[100, "out", "pizza"],[150, "out", "lunch"],[1000, "in", "salary"]]}
    assert type_sum(storage, 23, "in") == 1000
    assert type_sum(storage, 23, "out") == 250

def all_tests():
    test_get_day()
    test_get_trans()
    test_get_value()
    test_get_type()
    test_get_descr()
    test_set_value()
    test_create_storage()
    test_add()
    test_insert()
    test_remove()
    test_remove_to()
    test_remove_type()
    test_replace()
    test_type_sum()
    "all tests passed"




