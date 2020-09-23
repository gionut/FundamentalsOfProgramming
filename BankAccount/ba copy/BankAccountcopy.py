import datetime
import re
from get_set import get_day, get_trans, get_value, get_type, get_descr, set_value
from functions import create_storage, create_df_storage, add, insert, remove, remove_to, remove_type, replace, write, type_sum

################################################################################       
#********************************* VALIDATION *********************************
################################################################################

def validate_cmd(cmd):
    commands = { 1:"add", 2:"insert", 3:"remove", 4:"replace", 5:"list" }
    while True:
        if(cmd[0] == "add" or cmd[0] == "insert" or cmd[0] == "remove" or cmd[0] == "replace" or cmd[0] == "list" or cmd[0] == "default"):
            break
        else:
            print("invalid command!\n")
            cmd = ui_read_command()
            
    if(cmd[0] == "add"):
        cmd = validate_add(cmd)
    elif(cmd[0] == "insert"):
        cmd = validate_insert(cmd)
    elif(cmd[0] == "remove"):
        cmd = validate_remove(cmd)
    elif(cmd[0] == "replace"):
        cmd = validate_replace(cmd)
    elif(cmd[0] == "list"):
        cmd = validate_list(cmd)
    elif(cmd[0] == "default"):
        pass
    elif(cmd[0] == "exit"):
        pass
    return cmd

def validate_add(cmd):
    while True:
        try:
            int(cmd[1])
            if(len(cmd) != 4 or (cmd[2] != "in" and cmd[2] != "out") ):
                raise Exception
            return cmd
        except:
            print("add command must be : add <value> <type> <description>")
            cmd = ui_read_command()
                
def validate_insert(cmd):
     while True:
        try:
            int(cmd[1])
            int(cmd[2])
            if(len(cmd)!= 5 or int(cmd[1])<0 or int(cmd[1])>30 or (cmd[3] != "in" and cmd[3] != "out")):
                raise Exception
            return cmd
        except:
                print("insert command must be : insert <day> <value> <type> <description>")
                cmd = ui_read_command()

def validate_remove(cmd):
    l = len(cmd)
    while True:
        try:
            if(l != 2 and l != 4):
                raise Exception
            break
        except:
            print("remove command must be : remove <day> or\n"
              "                         remove <type> or\n"
              "                         remove <start day> to <end day> or")
            cmd = ui_read_command()
    if(l == 2):
        while True:
            try:
                day = 0
                if(not(cmd[1] == "in" or cmd[1] == "out")):
                    int(cmd[1])
                    if(int(cmd[1])<0 or int(cmd[1])>30):
                        day = 1
                        raise Exception
                return cmd
            except Exception:
                print("remove command must be : remove <day> or\n"
                      "                         remove <type> or\n"
                      "                         remove <start day> to <end day> or")
                cmd = ui_read_command()
    elif(l == 4):
        while True:
            try:
                if((type(cmd[1]) == "int" and cmd[1]>=0 and cmd[1]<=30) and (type(cmd[2]) == "int" and cmd[2]>=0 and cmd[2]<=30)):
                    break
            except Exception:
                print("remove command must be : remove <day> or\n"
                      "                         remove <type> or\n"
                      "                         remove <start day> to <end day> or")
                cmd = ui_read_command()
        
def validate_replace(cmd):
    while True:
        try:
            int(cmd[1])
            if(not(len(cmd) == 6 and int(cmd[1])>=0 and int(cmd[1])<=30 and (cmd[2] == "in" or cmd[2] == "out") and cmd[4] == "with" and int(cmd[5]))):
                raise Exception
            return cmd
        except Exception:
            print("replace command must be : replace <day> <type> <description> with <value>")
            cmd = ui_read_command()

def validate_list(cmd):
    l = len(cmd)
    if(l == 1):
        return cmd
    elif(l == 2):
        while True:
            try:
                if(not(cmd[1] == "in" or cmd[1] == "out")):
                    raise Exception
                return cmd
            except Exception:
                print("list command must be : list or\n"
                      "                       list <type> or\n"
                      "                       list [ < | = | > ] <value> or\n"
                      "                       list balance <day>")
                cmd = ui_read_command()
    elif(l == 3 and cmd[1] == "balance"):
        while True:
            try:
                int(cmd[2])
                if(not(int(cmd[2])>=0 and int(cmd[2])<=30)):
                    raise Exception
                return cmd
            except Exception:
                print("list command must be : list or\n"
                      "                       list <type> or\n"
                      "                       list [ < | = | > ] <value> or\n"
                      "                       list balance <day>")
                cmd = ui_read_command()
    elif(l == 3):
        while True:
            try:
                int(cmd[2])
                if(not((cmd[1] == "<" or cmd[1] == ">" or cmd[1] == "="))):
                    raise Exception
                return cmd       
            except Exception:
                print("list command must be : list or\n"
                      "                       list <type> or\n"
                      "                       list [ < | = | > ] <value> or\n"
                      "                       list balance <day>")
                cmd = ui_read_command()
            

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





################################################################################                                        
#************************************* ui_functions *****************************
################################################################################
    
def ui_read_command():
    comm = input("get command: ")
    cmd = re.split("\s", comm)
    return cmd

def ui_list_balance(storage, day):
    in_tr = type_sum(storage, day, "in")
    out_tr = type_sum(storage, day, "out")
    print(in_tr - out_tr)

def ui_list_less_value(storage, value):
    for i in range(31):
        ok = 1
        for j in range(len(get_day(storage, i))):
               if(get_value(storage, i, j) < value):
                   if(ok):
                       print("\nday ", i, "\n---------------------------------------------------")
                       ok = 0
                   print(write(storage, i, j))
        if(not ok):
            print("\n")

def ui_list_more_value(storage, value):
    for i in range(31):
        ok = 1
        for j in range(len(get_day(storage, i))):
               if(get_value(storage, i, j) > value):
                   if(ok):
                       print("\nday ", i, "\n---------------------------------------------------")
                       ok = 0
                   print(write(storage, i, j))
        if(not ok):
            print("\n")

def ui_list_equal_value(storage, value):
    for i in range(31):
        ok = 1
        for j in range(len(get_day(storage, i))):
               if(get_value(storage, i, j) == value):
                   if(ok):
                       print("\nday ", i, "\n---------------------------------------------------")
                       ok = 0
                   print(write(storage, i, j))
        if(not ok):
            print("\n")
            
def ui_list(storage):
    for i in range(31):
        ok = 1
        for j in range(len(get_day(storage, i))):
              if(ok):
                   print("\nday ", i, "\n---------------------------------------------------")
                   ok = 0
              print(write(storage, i, j))
        if(not ok):
            print("\n")

def ui_list_type(storage, tr_type):
    for i in range(31):
        ok = 1
        for j in range(len(get_day(storage, i))):
               if(get_type(storage, i ,j) == tr_type):
                   if(ok):
                       print("\nday ", i, "\n---------------------------------------------------")
                       ok = 0
                   print(write(storage, i, j))
        if(not ok):
            print("\n")

def ui_list_value(storage, sign, value):
     if(sign == "<"):
         ui_list_less_value(storage, value)
     elif(sign == ">"):
         ui_list_more_value(storage, value)
     else:
         ui_list_equal_value(storage, value)         

def ui_add(storage, cmd):
    value = int(cmd[1])
    tr_type = cmd[2]
    description = cmd[3]
    add(storage, value, tr_type, description)

def ui_insert(storage, cmd):
    day = int(cmd[1])
    value = int(cmd[2])
    tr_type = cmd[3]
    description = cmd[4]
    insert(storage, day, value, tr_type, description)
            
def ui_menu():
    cmd = ui_read_command()
    cmd = validate_cmd(cmd)
    if(cmd[0] == "add"):
        ui_add(storage, cmd)
        ui_menu()
    if(cmd[0] == "insert"):
        ui_insert(storage, cmd)
        ui_menu()
    if(cmd[0] == "remove"):
        if(len(cmd) == 4):
                remove_to(storage, int(cmd[1]), int(cmd[3]))
        elif(cmd[1] == "in" or cmd[1] == "out"):
             remove_type(storage, cmd[1])
        else:
            remove(storage, int(cmd[1]))        
        ui_menu()
    if(cmd[0] == "replace"):
        replace(storage, cmd)
        ui_menu()
    if(cmd[0] == "default"):
        create_df_storage(storage)
        ui_menu()
    if(cmd[0] == "list"):
        if(len(cmd)==1):
            ui_list(storage)
        elif(len(cmd) == 2):
            ui_list_type(storage, cmd[1])
        elif(cmd[1] == "balance"):
            ui_list_balance(storage, int(cmd[2]))
        else:
            ui_list_value(storage, cmd[1], int(cmd[2]))
        ui_menu()
    if(cmd[0] == "exit"):
        exit()




################################################################################       
#********************************* main_function *********************************
################################################################################

if __name__ == "__main__":
    storage = {}
    create_storage(storage)
    all_tests()
    ui_menu()
    
