################################################################################
#***********************************    SET / GET   ****************************
################################################################################

def get_day(storage, day):
    #input: dict storage, integer day
    #output: list storage[day] containing the list of transactions in day day
    #return: storage[day]
    return storage[day]

def get_trans(storage, day, transaction):
    #input: dict storage, integer day, integer transaction
    #output: list storage[day][transaction] containing the transaction terms(value, type and description) in day day
    #return: storage[day][transaction]
    return storage[day][transaction]

def get_value(storage, day, transaction):
    #input: dict storage, integer day, integer transaction
    #output: integer storage[day][transaction][0] meaning the value of the transaction with the number transaction in day day
    #return: storage[day][transaction][0]
    return storage[day][transaction][0]

def get_type(storage, day, transaction):
    #input: dict storage, integer day, integer transaction
    #output: string storage[day][transaction][1] meaning the type of the transaction with the number transaction in day day
    #return: storage[day][transaction][1]
    return storage[day][transaction][1]

def get_descr(storage, day, transaction):
    #input: dict storage, integer day, integer transaction
    #output: string storage[day][transaction][2] meaning the description of the transaction with the number transaction in day day
    #return: storage[day][transaction][2]
    return storage[day][transaction][2]

def set_value(storage, day, transaction, value):
    #input: dict storage, integer day, integer transaction, integer value
    #output: integer storage[day][transaction][0] meaning the value of the transaction with the number transaction in day day
    #return: -
    #spec: the value of the transaction number transaction in day day is set to value
    storage[day][transaction][0] = value
