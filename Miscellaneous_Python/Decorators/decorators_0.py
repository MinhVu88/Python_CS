# prerequisites: 1st-class functions & closures
# a decorator is a func that takes another func as its arg, adds some kind of functionality & returns another func
# a decorator doesn't alter the source code of the func that's passed to it as an arg
def decor_func_0(func):
    def wrapper_func():
        return func()
    return wrapper_func

def display_0():
    print('display_0() ran')

display_func_0 = decor_func_0(display_0)

display_func_0()

print('\n****************************************\n')

def decor_func_1(func):
    def wrapper_func():
        print('wrapper_func() executed this before {}'.format(func.__name__))

        return func()
    return wrapper_func

def display_1():
    print('display_1() ran')

display_func_1 = decor_func_1(display_1)

display_func_1()

print('\n****************************************\n')

def decor_func_2(func):
    def wrapper_func():
        print('wrapper_func() executed this before {}'.format(func.__name__))

        return func()
    return wrapper_func

# @decor_func_2 -> display_2 = decor_func_2(display_2)
@decor_func_2
def display_2():
    print('display_2() ran')

display_2()

print('\n****************************************\n')

def decor_func_3(func):
    def wrapper_func(*args, **kwargs):
        print('wrapper_func() executed this before {}'.format(func.__name__))

        return func(*args, **kwargs)
    return wrapper_func

@decor_func_3
def display_3():
    print('display_3() ran')

@decor_func_3
def display_info_0(name, age):
    print('display_info_0() ran with args: ({}, {})'.format(name, age))

display_info_0('Nikola Tesla', 23)

display_3()

print('\n****************************************\n')

class decor_class_0(object):
    def __init__(self, func):
        self.func = func
    
    # __call__() behaves just like the inner wrapper_func() does
    def __call__(self, *args, **kwargs):
        print('__call__() executed this before {}'.format(self.func.__name__))

        return self.func(*args, **kwargs)

def decor_func_4(func):
    def wrapper_func(*args, **kwargs):
        print('wrapper_func() executed this before {}'.format(func.__name__))

        return func(*args, **kwargs)
    return wrapper_func

#@decor_func_4
@decor_class_0
def display_4():
    print('display_4() ran')

#@decor_func_4
@decor_class_0
def display_info_1(name, age):
    print('display_info_1() ran with args: ({}, {})'.format(name, age))

display_info_1('Nikola Tesla', 23)

display_4()

print('\n-----------------------------------------------------------------------------------\n')

# some practical examples
from functools import wraps # to preserve info of display_info_4

# common use case #1: provide logging functionality (keep track of how many times a func runs & what args are passed to it)
def decor_logger(func):
    import logging

    logging.basicConfig(filename='{}.log'.format(func.__name__), level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {} & kwargs: {}'.format(args, kwargs))

        return func(*args, **kwargs)
    
    return wrapper

@decor_logger
def display_info_2(name, age):
    print('display_info_2() ran with args: ({}, {})'.format(name, age))

display_info_2('Wernher von Braun', 47)

print('\n****************************************\n')

# common use case #2: provide timing functionality (measure how long a function runs)
def decor_timer(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()

        result = func(*args, **kwargs)

        t2 = time.time() - t1

        print('{} ran in {} seconds'.format(func.__name__, t2))

        return result
    
    return wrapper

import time

@decor_timer
def display_info_3(name, age):
    time.sleep(1)

    print('display_info_3() ran with args: ({}, {})'.format(name, age))

display_info_3('Leonardo da Vinci', 88)

print('\n****************************************\n')

# chaining decors together on a function
'''
@decor_timer -> display_info_4 = decor_timer(display_info_4)

@decor_logger
@decor_timer
             => display_info_4 = decor_logger(decor_timer(display_info_4))

             => decor_timer(display_info_4) or @decor_timer runs 1st & returns its wrapper func

             => That wrapper func is passed to decor_logger() as its arg, not display_info_4

             => Then decor_logger() or @decor_logger runs & returns its wrapper func

             => That's why wrapper.log is created, instead of display_info_4.log
'''
#@decor_timer
@decor_logger
@decor_timer
def display_info_4(name, age):
    time.sleep(1)

    print('display_info_4() ran with args: ({}, {})'.format(name, age))

print(display_info_4.__name__)

display_info_4('Isaac Newton', 25)