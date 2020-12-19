def outer_func_0():
    message = 'Hi!'

    def inner_func():
        # message is considered a free var as it's not defined in inner_funct() but still accessible within the func
        print(message)

    return inner_func()

outer_func_0()

print('\n-----------------------------------------------------------------------------------\n')

# a closure is an inner function that remembers & has access to vars local to the scope in which they're created
# even after the outer function has finished executing
def outer_func_1():
    message = 'Hi!'

    def inner_func():
        # message is considered a free var as it's not defined in inner_funct() but still accessible within the func
        print(message)
    
    return inner_func

my_func = outer_func_1()

print(my_func)

print(my_func.__name__)

my_func()
my_func()
my_func()

print('\n****************************************\n')

def outer_func_2(msg):
    message = msg

    def inner_func():
        print(message)
    
    return inner_func

greet1 = outer_func_2('Eyyo wassup dude')

greet1()

greet2 = outer_func_2('Oi! How u doin\' biatch')

greet2()

print('\n****************************************\n')

def outer_func_3(msg):
    def inner_func():
        print(msg)
    return inner_func

message = outer_func_3('Hasta la vista baby')

message()

print('\n-----------------------------------------------------------------------------------\n')

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def log(func):
    def log_func(*args):
        logging.info("Running '{}' with args {}".format(func.__name__, args))

        print(func(*args))
    
    return log_func

def add(x, y):
    return x + y

addition = log(add) # addition becomes log_func(*args)

addition(23, 47)

addition(51, 69)

def sub(x, y):
    return x - y

subtraction = log(sub) # subtraction becomes log_func(*args)

subtraction(7, 88)

subtraction(-73, 96)