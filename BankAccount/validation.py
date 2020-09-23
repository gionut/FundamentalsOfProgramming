import datetime
import re
from get_set import get_day, get_trans, get_value, get_type, get_descr, set_value
from functions import create_storage, create_df_storage, add, insert, remove, remove_to, remove_type, replace, write, type_sum, sum_type, max_tr, filter_type, filter, add_stack, undo
from tests import all_tests
import copy
from ui_functions import ui_read_command, ui_add, ui_insert, ui_list, ui_list_balance, ui_list_less_value, ui_list_more_value,ui_list_equal_value,ui_list_type,ui_list_value,ui_menu

################################################################################       
#********************************* VALIDATION *********************************
################################################################################

def validate_cmd(cmd):
    commands = { 1:"add", 2:"insert", 3:"remove", 4:"replace", 5:"list", 6: "exit", 7:"sum", 8:"max", 9:"filter", 10:"undo" }
    while True:
        if(cmd[0] == "print" or cmd[0] == "add" or cmd[0] == "insert" or cmd[0] == "remove" or cmd[0] == "replace" or cmd[0] == "list" or cmd[0] == "default" or cmd[0] == "exit" or cmd[0] == "sum" or cmd[0] == "max" or cmd[0] == "filter" or cmd[0] == "undo"):
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
    elif(cmd[0] == "sum"):
        cmd = validate_sum(cmd)
    elif(cmd[0] == "max"):
        cmd = validate_max(cmd)
    elif(cmd[0] == "filter"):
        cmd = validate_filter(cmd)
    #elif(cmd[0] == "undo"):
        #cmd = validate_undo(cmd)
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
            l = len(cmd)
    if(l == 2):
        while True:
            try:
                if(not(cmd[1] == "in" or cmd[1] == "out")):
                    int(cmd[1])
                    if(int(cmd[1])<0 or int(cmd[1])>30):
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
                if(not(cmd[2] == "to" and int(cmd[1]) and int(cmd[1])>=0 and int(cmd[1])<=30 and int(cmd[3]) and int(cmd[3])>=0 and int(cmd[3])<=30)):
                    raise Exception
                return cmd
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
            
def validate_sum(cmd):
    while True:
        try:
            if(not(len(cmd) == 2 and (cmd[1] == "in" or cmd[1] == "out"))):
                raise Exception
            return cmd
        except Exception:
            print("sum command must be : sum <type>")
            cmd = ui_read_command()

def validate_max(cmd):
    while True:
        try:
            if(not(len(cmd) == 3 and (cmd[1] == "out" or cmd[1] == "in") and int(cmd[2]) and int(cmd[2]) >= 0 and int(cmd[2]) <= 30)):
                raise Exception
            return cmd
        except Exception:
            print("max command must be : max <type> <day>")
            cmd = ui_read_command()

def validate_filter(cmd):
    l = len(cmd)
    while True:
        try:
            if(l != 2 and l != 3):
                raise Exception
            break
        except Exception:
            print("filter command must be : filter <type> or\n"
                  "                         filter <type> <value>")
            cmd = ui_read_command()
            l = len(cmd)
    if(l == 2):
        while True:
            try:
                if(not(cmd[1] == "in" or cmd[1] == "out")):
                    raise Exception
                return cmd
            except Exception:
                print("filter command must be : filter <type> or\n"
                      "                         filter <type> <value>")
                cmd = ui_read_command()
    if(l == 3):
        while True:
            try:
                if(not((cmd[1] == "out" or cmd[1] == "in") and int(cmd[2]))):
                    raise Exception
                return cmd
            except Exception:
                print("filter command must be : filter <type> or\n"
                      "                         filter <type> <value>")
                cmd = ui_read_command()
