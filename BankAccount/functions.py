from get_set import get_day, get_trans, get_value, get_type, get_descr, set_value
import datetime
import re
import copy

#########################################################################################
#********************************   NON ui_functions    *****************************
#########################################################################################
    
def create_storage(storage):
    #input: dict storage
    #spec: creates a dict storage with keys from 0 to 30 meaning the number of day in month, stored in lists(empty for now)
    #return: -
    for i in range(31):
        storage[i] = []

def create_df_storage(storage):
    #input: dict storage
    #spec: creates a default storage 
    #return: -
    storage.clear()
    create_storage(storage)
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
    #spec: adds a transaction in the current day
    #return: -
    lst = []
    lst.append(value)
    lst.append(tr_type)
    lst.append(description)
    get_day(storage, datetime.date.today().day).append(lst) # add to the other entries in that day

def insert(storage, day, value, tr_type, description):
    #input: dict storage, integer value, string tr_type, string description
    #spec: inserts a transaction in day day
    #return: -
    lst = []
    lst.append(value)
    lst.append(tr_type)
    lst.append(description)
    index = 0
    get_day(storage, day).append(lst)

def remove(storage, day):
    #input: dict storage, integer day
    #spec: removes all the transactions in day day
    #return: -
    get_day(storage, day).clear()

def remove_to(storage, day, end_day):
    #input: dict storage, integer day, integer end_day
    #spec: removes all the transactions from day day to day end_day
    #return: -
    for i in range(day,end_day+1,):
         get_day(storage, i).clear()

def remove_type(storage, tr_type):
    #input: dict storage, string tr_type
    #spec: removes all the transactions of type tr_type
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
    #spec: replaces the value of transaction in day day with type tr_type and description description with value value
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
    #spec: sums up all the transactions values in day day of type tr_type
    #return: integer s
    s = 0
    for i in range(len(get_day(storage, day))):
            if(get_type(storage, day, i) == tr_type):
                s += get_value(storage, day, i)
    return s

def sum_type(storage, tr_type):
    #function that sums up all the transactions of type tr_type
    #input: dict storage, string tr_type
    #output: -
    s = 0
    for i in storage.keys():
        s += type_sum(storage, i, tr_type)
    print("sum of all " + tr_type + " tranzactions is " + str(s))

def max_tr(storage, tr_type, day):
    maximum = 0
    for i in range(len(get_day(storage, day))):
        if(get_type(storage, day, i) == tr_type):
            if(get_value(storage, day, i) > maximum):
                maximum = get_value(storage, day, i)
    print("The maximum " + tr_type + " tranzaction in day " + str(day) + " is " + str(maximum))

def filter_type(storage, tr_type):
    #function that keeps only tr_type tranzactions 
    #input: dict storage, str tr_type
    #output: -
    if(tr_type == "in"):
        remove_type(storage, "out")
    else:
        remove_type(storage, "in")

def filter(storage, tr_type, value):
    #function that keeps only tr_type tranzactions with values smaller than value
    #input: dict storage, str tr_type, int value
    #output: -
    filter_type(storage, tr_type)
    for i in range(31):
        length = len(get_day(storage, i))
        j = 0
        while(j < length):
            if(get_value(storage, i, j) >= value):
               get_day(storage, i).remove(get_trans(storage, i, j))
               length -= 1
            else:
                j += 1

def add_stack(stack, storage):
    dictionary = copy.deepcopy(storage)
    stack.append(dictionary)
    return stack

def undo(stack, storage):
    if(len(stack)==1):
        print("You cannot undo anymore!")
        for i in range(31):
            storage[i] = []
        return storage
    else:
        stack.pop()
        i = 0
        while(i < len(stack)):
            i += 1
        storage = stack[i-1]
    return storage
        
