def square(x):
    return x * x

def cube(y):
    return y * y * y

f_0 = square(5)

print(f_0)

# assign a function to a variable
# square -> the square function | square() -> call & execute the square function
f_1 = square 

print(f_1, square)

print(f_1(5)) # f_1 now can be treated as a function -> it can be called & executed

print('\n-----------------------------------------------------------------------------------\n')

# pass a function as an arg to another function
def my_map(func, arg_list):
    result = []

    for i in arg_list:
        result.append(func(i)) # here square/cube is called & executed inside the append() method
    
    return result

# here square & cube are passed as args to my_map() but not called & executed yet
# on the other hand, my-map() is called & executed & its result is assigned to squares
squares = my_map(square, [1, 2, 3, 4, 5])

print(squares)

cubes = my_map(cube, [6, 7, 8, 9, 10])

print(cubes)

print('\n-----------------------------------------------------------------------------------\n')

# return a function from another function
def log(msg):
    def log_message():
        print('Log:', msg)
    return log_message # the log_message function is returned here but not called & executed yet

# the returned log_message function is assigned to the greet var
greet = log('Eyyo wassup dude!') 

greet() # hence greet now can be treated as a function -> it can be called & executed

print('\n****************************************\n')

def print_html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

h1 = print_html_tag('h1')

print(h1)

h1('Test headline')

h1('Test another headline')

p = print_html_tag('p')

p("""In my shadow
   My shadow
   Change is coming through
   My shadow
   My shadow
   Shedding skin
   I've been picking
   My scabs again""")