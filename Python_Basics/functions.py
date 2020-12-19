# a func that takes no args & returns nothing when called
def greet_0():
    pass

greet_0()

print(greet_0())

print('\n-----------------------------------------------------------------------------------\n')

# functions that take no args & return nothing but instead print something out when called
def greet_1():
    print('Hi there')

greet_1()

def greet_2():
    print('eyyo wassup!')

greet_2()
greet_2()
greet_2()
greet_2()

print('\n-----------------------------------------------------------------------------------\n')

# a func that returns something when called
def greet_3():
    return 'this function returns some value'

print(greet_3())

print(greet_3().upper())

print('\n-----------------------------------------------------------------------------------\n')

# functions that take 1 or multiple positional args & return some data when called
def greet_4(time, name):
    return f'Good {time}, {name}!'

print(greet_4({}, {}).format('morning', 'Elliot Alderson'))

def greet_5(time, name):
    return 'Good {}, {}!'.format(time, name)

print(greet_5('afternoon', 'Angela Moss'))

print('\n-----------------------------------------------------------------------------------\n')

# specifying a default value for a param
def greet_6(name, greeting='Bonsoir'):
    return '{} {}!'.format(greeting, name)

print(greet_6('Elliot'))

print(greet_6('friend', greeting='Hello')) # overwrite the param's default value by using a keyword arg (greeting)

print('\n-----------------------------------------------------------------------------------\n')

# pass to a function an arbitrary number of args using *args & **kwargs
# args & kwargs are optionally conventional names, * and ** are called unpacking operators
# * works with positional arguments (Ex: lists or tuples) 
# ** works with default args & keyword/named args (Ex: dictionaries)
# order of args in a function def: standard args, *args, **kwargs
''' Online references:

https://realpython.com/python-kwargs-and-args/

https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/

https://www.programiz.com/python-programming/args-and-kwargs

https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters

https://book.pythontips.com/en/latest/args_and_kwargs.html

https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3

https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

https://www.geeksforgeeks.org/args-kwargs-python/

https://medium.com/swlh/python-args-and-kwargs-a82b6480f287
'''
def student_info(*args, **kwargs):
    print(args)

    print(kwargs)

student_info('computer science', 'economics', 'psychology', name='Jake Foley', gender='male', age=23)

print('\n****************************************\n')

courses = ['biology', 'art', 'finance', 'chemistry', 'physics']

info = {'name': 'Kathleen Cruise', 'gender': 'female', 'age': 21}

student_info(courses, info)

print('\n****************************************\n')

student_info(*courses, **info)

print('\n****************************************\n')

# *args & **kwargs demo
def get_total_0(*args):
    total = 0
    for val in args:
        total += val
    return total

list_0 = [23, 69, 7, 47, 3]

tuple_0 = (13, 5, 88, 51, 9)

print(get_total_0(*list_0))

print(get_total_0(*tuple_0))

print(get_total_0(*list_0, *tuple_0))

print('\n****************************************\n')

def get_total_1(a, b, c):
    return a + b + c

list_1 = [3, 6, 9]

print(get_total_1(*list_1))

print('\n****************************************\n')

# split a list into 3 different parts
list_2 = [1, 2, 3, 3.5, 4, 5, 6]

*a, b, c = list_2
print(a)
print(b)
print(c)

print('~~~~~~~~~~~~~~~~~~~~~~')

a, *b, c = list_2
print(a)
print(b)
print(c)

print('~~~~~~~~~~~~~~~~~~~~~~')

a, b, *c = list_2
print(a)
print(b)
print(c)

print('\n****************************************\n')

list_3 = [7, 8, 9, 10]
list_4 = [11, 12, 13, 14]

merged_list = [*list_3, *list_4]

print(merged_list)

print('\n****************************************\n')

dict_0 = {'A': 1, 'B': 2}

dict_1 = {'C': 3, 'D': 4}

merged_dict = {**dict_0, **dict_1}

print(merged_dict)

print('\n****************************************\n')

str_to_list_0 = [*'fsociety']

print(str_to_list_0)

*str_to_list_1, = 'Mr.Robot'

print(str_to_list_1)

print('\n-----------------------------------------------------------------------------------\n')

# number of days per month. The 1st element (0) is a placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    "Return true for leap years, false otherwise"
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_month_days(month, year):
    "Return number of days in that month of that year"
    if not 1 <= month <= 12:
        return 'Invalid month'
    
    if month == 2 and is_leap_year(year):
        return 29
    
    return month_days[month]

print(is_leap_year(2016))

print(get_month_days(2, 2020))

print(get_month_days(2, 2017))