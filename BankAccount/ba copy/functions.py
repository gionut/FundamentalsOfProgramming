from get_set import get_day, get_trans, get_value, get_type, get_descr, set_value
import datetime
import re

#########################################################################################
#********************************   NON ui_functions    *****************************
#########################################################################################
    
def create_storage(storage):
    #input: dict storage
    #output: creates a dict storage with keys from 0 to 30 meaning the number of day in month, stored in lists(empty for now)
    #return: -
    for i in range(31):
        storage[i] = []

def create_df_storage(storage):
    #input: dict storage
    #output: creates a default storage 
    #return: -
    for i in range(datetime.date.today().day+1):
        get_day(storage, i).append([10, "out", "piggy_bank"])
    get_day(storage, 1).append([100, "out", "pizza"])
    get_day(storage, 2).append([300, "out", "donut"])
    get_day(storage, 12).append([2080, "in", "salary"])
    get_day(storage, 12).append([150, "out", "cinema"])
    get_day(storage, 19).append([100, "in", "grandma"])
    get_day(storage, 20).append([70, "out", "book"])
    get_day(storage, 20).append([300, "out", "shopping"])
    get_day(storage, 20).append([50, "out", "bus ticket"])
    get_day(storage, 20).append([50, "out", "bus ticket"]) 

def add(storage, value, tr_type, description):
    #input: dict storage, integer value, string tr_type, string description
    #output: adds a transaction in the current day
    #return: -
    lst = []
    lst.append(value)
    lst.append(tr_type)
    lst.append(description)
    get_day(storage, datetime.date.today().day).append(lst) # add to the other entries in that day

def insert(storage, day, value, tr_type, description):
    #input: dict storage, integer value, string tr_type, string description
    #output: inserts a transaction in day day
    #return: -
    lst = []
    lst.append(value)
    lst.append(tr_type)
    lst.append(description)
    index = 0
    get_day(storage, day).append(lst)

def remove(storage, day):
    #input: dict storage, integer day
    #output: removes all the transactions in day day
    #return: -
    get_day(storage, day).clear()

def remove_to(storage, day, end_day):
    #input: dict storage, integer day, integer end_day
    #output: removes all the transactions from day day to day end_day
    #return: -
    for i in range(day,end_day+1,):
         get_day(storage, i).clear()

def remove_type(storage, tr_type):
    #input: dict storage, string tr_type
    #output: removes all the transactions of type tr_type
    #return: -
    for i in range(31):
        length = len(get_day(storage, i))
        j = 0
        while(j < length):
            if(get_type(storage, i, j) == tr_type):
               get_day(storage, i).remove(get_trans(storage, i, j))
               length -= 1
            else:
                j += 1
                               
def replace(storage, cmd):
    #input: dict storage, string cmd
    #output: replaces the value of th transaction in day day with type tr_type and description description with value value
    #return: -
    day = int(cmd[1]) 
    value = int(cmd[5])
    tr_type = cmd[2]
    description = cmd[3]
    for i in range(len(get_day(storage, day))):
        if(get_descr(storage, day, i) == description):
            if(get_type(storage, day, i) == tr_type):
                set_value(storage, day, i, value)

def write(storage, i, j):
#input: dict storage, integer index
#output: string string containing the elements of the list(index key) from the storage all put together
    string = str(get_value(storage, i, j)) + " "    
    string += get_type(storage, i, j) + " " + get_descr(storage, i, j)
    return string

def type_sum(storage, day, tr_type):
    #input: dict storage, integer day, string tr_type
    #output: sums up all the transactions values in day day of type tr_type
    #return: -
    s = 0
    for i in range(len(get_day(storage, day))):
            if(get_type(storage, day, i) == tr_type):
                s += get_value(storage, day, i)
    return s




