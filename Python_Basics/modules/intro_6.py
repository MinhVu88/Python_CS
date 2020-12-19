from my_module import find_index, test
import sys

courses = ['mathematics', 'fine arts', 'architecture', 'chemistry', 'physics', 'psychology', 
           'literature', 'engineering', 'philosophy', 'history', 'design', 'law']

index = find_index(courses, 'philosophy')

print(index)

print(test)

print('\n-----------------------------------------------------------------------------------\n')

for i in sys.path:
    print(i)