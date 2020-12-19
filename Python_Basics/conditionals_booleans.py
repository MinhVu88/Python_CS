''' Comparison operators:

    Equal ----> ==

    Not equal ----> !=

    Greater than ----> >

    Less than ----> <

    Greater/equal ----> >=

    Less/equal ----> <=

    Object identity ----> is
'''

if True:
    print('true')

if False:
    print('false')

print('\n****************************************\n')

language0 = 'Python'

if language0 == 'Python':
    print(language0)

print('~~~~~~~~~~~~~~~~~~~~~~')

language1 = 'Java'

if language1 == 'JavaScript':
    print(language1)
else:
    print('No match')

print('~~~~~~~~~~~~~~~~~~~~~~')

language2 = 'C++'

if language2 == 'Java':
    print('Java')
elif language2 == 'C':
    print('C')
elif language2 == 'C++':
    print('C++')
else:
    print('No match')

print('\n****************************************\n')

# Boolean operators: and, or & not
user = 'Admin'

logged_in = True

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

logged_in = False

if user == 'Admin' and logged_in:
    print('Admin page')
else:
    print('Bad creds')

print('~~~~~~~~~~~~~~~~~~~~~~')

if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad creds')

print('~~~~~~~~~~~~~~~~~~~~~~')

if not logged_in:
    print('Welcome')
else:
    print('Plz log in')

print('\n****************************************\n')

# the differences bw equal operator (==) & object identity (is)
a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)

# a & b are 2 distinct objects in memory, even though they contain identical elements
print(a is b) 

# use the id() function to get an object's location in memory
print('a\'s location in memory: ', id(a))

print('b\'s location in memory: ', id(b))

c = b

print(b == c)

print(b is c)

print(id(b) == id(c))

print('\n****************************************\n')

''' False values:
    - False
    - None
    - Zero of any numeric type
    - Any empty sequence ----> '', (), []
    - Any empty mapping ----> {}
'''

if False:
    print('True')
else:
    print('False')

print('~~~~~~~~~~~~~~~~~~~~~~')

if None:
    print('True')
else:
    print('False')

print('~~~~~~~~~~~~~~~~~~~~~~')

if 0:
    print('True')
else:
    print('False')

if -1:
    print('True')
else:
    print('False')

if 1:
    print('True')
else:
    print('False')

print('~~~~~~~~~~~~~~~~~~~~~~')

if '' or [] or ():
    print('True')
else:
    print('False')

print('~~~~~~~~~~~~~~~~~~~~~~')

if {}:
    print('True')
else:
    print('False')