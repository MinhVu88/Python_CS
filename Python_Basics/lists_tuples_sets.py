# lists (mutable)
courses_0 = ['mathematics', 'fine arts', 'chemistry', 'physics', 'finance', 'logistics', 'computer science']

print(courses_0)

print(len(courses_0))

print(courses_0[2])

print(courses_0[-1])

print(courses_0[0:2])

print(courses_0[:3])

print(courses_0[3:])

print('\n****************************************\n')

courses_0.append('psychology') # the append() method

print(courses_0)

print('\n****************************************\n')

courses_0.insert(2, 'architecture') # the insert() method

print(courses_0)

print('\n****************************************\n')

courses_1 = ['literature', 'engineering']

courses_0.extend(courses_1) # the extend() method

print(courses_0)

print('\n****************************************\n')

courses_0.remove('logistics') # the remove() method

print(courses_0)

print('\n****************************************\n')

popped = courses_0.pop()

print(popped)

print(courses_0)

print('\n****************************************\n')

courses_0.reverse() # the reverse() method

print(courses_0)

print('\n****************************************\n')

courses_0.sort() # the sort() method

print(courses_0)

nums = [23, 51, 47, 3, 7, 88, 9, 6, 13]

print(nums)

nums.sort()

print(nums)

courses_0.sort(reverse=True)

nums.sort(reverse=True)

print(courses_0)

print(nums)

print('~~~~~~~~~~~~~~~~~~~~~~')

# the sorted() function doesn't alter the original list in any way, it just returns a sorted version of the list
sorted_courses = sorted(courses_0) 

print(sorted_courses)

print('\n****************************************\n')

print(min(nums))

print(max(nums))

print(sum(nums))

print('\n****************************************\n')

print(courses_0.index('computer science')) # the index() method

# the 'in' operator returns a boolean value (t/f) that indicates whether an item exists in a list
print('astronomy' in courses_0)

print('physics' in courses_0)

print('~~~~~~~~~~~~~~~~~~~~~~')

for course in courses_0:
    print(course)

print('~~~~~~~~~~~~~~~~~~~~~~')

for index, course in enumerate(courses_0):
    print(index, course)

print('~~~~~~~~~~~~~~~~~~~~~~')

for i, num in enumerate(nums, start=3):
    print(i, num)

print('\n****************************************\n')

# turn a list into a string by using the join() method
courses_str = ', '.join(courses_0)

print(courses_str)

# turn a string into a list by using the split() method
courses_list = courses_str.split(', ')

print(courses_list)

print('\n-----------------------------------------------------------------------------------\n')

# tuples (immutable)
courses_1 = ('literature', 'engineering', 'philosophy', 'history', 'design', 'law')

courses_2 = courses_1

print(courses_1)

print(courses_2)
'''
courses_1[0] = 'anthropology' # Error as tuples are immutable

print(courses_1)

print(courses_2)
'''

print('\n-----------------------------------------------------------------------------------\n')

# sets (unordered & no duplicate items)
bands_0 = {'Tool', 'Puscifer', 'A Perfect Circle', 'Radiohead', 'Blur', 'Tool', 'Oasis'}

print(bands_0)

print('Blur' in bands_0)

bands_1 = {'Rammstein', 'Soundgarden', 'Alice In Chains', 'Nirvana', 'Tool', 'Pulp', 'Oasis'}

print(bands_0.intersection(bands_1))

print(bands_0.difference(bands_1))

print(bands_1.difference(bands_0))

print(bands_0.union(bands_1))

print('\n-----------------------------------------------------------------------------------\n')

# how to create empty lists/tuples/sets
empty_list_0 = []

empty_list_1 = list()

empty_tuple_0 = ()

empty_tuple_1 = tuple()

empty_set_0 = {} # this actually creates an empty dictionary, not an empty set

empty_set_1 = set()