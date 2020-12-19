# decorators that take args
def decor_func_0(prefix):
    def decor_func_1(func):
        def wrapper(*args, **kwargs):
            print(prefix, 'Executed before', func.__name__)

            result = func(*args, **kwargs)

            print(prefix, 'Executed after', func.__name__, '\n')

            return result
        return wrapper
    return decor_func_1

@decor_func_0('LOG:')
def display_info(name, age):
    print('display_info() ran with args: {} & {}'.format(name, age))

display_info('Thom Yorke', 25)

display_info('Jonny Greenwood', 27)