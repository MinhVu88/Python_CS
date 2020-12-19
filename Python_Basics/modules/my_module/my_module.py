print('Imported my_module.py')

test = 'Test String'

def find_index(searched_list, target):
    "find a value's index in a sequence"
    for index, value in enumerate(searched_list):
        if value == target:
            return index
    return -1