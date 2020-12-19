import random, math, datetime, calendar, os, antigravity

courses = ['mathematics', 'fine arts', 'architecture', 'chemistry', 'physics', 'psychology', 
           'literature', 'engineering', 'philosophy', 'history', 'design', 'law']

random_course = random.choice(courses)

print(random_course)

print('\n-----------------------------------------------------------------------------------\n')

# convert degrees to radians
degrees_to_radians = math.radians(90)

print(degrees_to_radians)

print(math.sin(degrees_to_radians))

print('\n-----------------------------------------------------------------------------------\n')

today = datetime.date.today()

print(today)

print(calendar.isleap(2020))

print('\n-----------------------------------------------------------------------------------\n')

print(os.getcwd())

# get the location of a standard lib module/a python files by printing out its dunder file attribute
print(os.__file__)