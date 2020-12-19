import sys

sys.path.append('D:\VS Code Programs\CoreySchafer\PythonBasics\modules\my_module')

from my_module import find_index, test

courses = ['mathematics', 'fine arts', 'architecture', 'chemistry', 'physics', 'psychology', 
           'literature', 'engineering', 'philosophy', 'history', 'design', 'law']

index = find_index(courses, 'philosophy')

print(index)

print(test)

print('\n-----------------------------------------------------------------------------------\n')

for i in sys.path:
    print(i)