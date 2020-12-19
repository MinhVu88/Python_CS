member = {'name': 'MJK', 'age': 46, 'roles': ['vocalist', 'bassist', 'soldier' 'interior designer', 'wine maker']}

members = {1: 'Adam jones', 2: 'Maynard Keenan', 3: 'Justin Chancellor', 4: 'Dan Carey', 
           5: 'Paul D\'Amour', 6: 'Bill Manspeaker', 7: 'Harry Manback'}

print(members[1])

print(member)

print(member['name'])

print(member['roles'])

print('\n****************************************\n')

#print(member['gender']) # accessing a nonexistent key gives KeyError

print(member.get('age')) # use the dict's get() method to returns the value

print(member.get('gender')) # use get() to return None for a nonexistent key, instead of the Traceback

print(member.get('gender', 'Not Found')) # specify a custom message for a nonexistent key

print('\n****************************************\n')

# alter some keys' values
member['gender'] = 'male'

member['name'] = 'Maynard Keenan'

print(member)

print('\n****************************************\n')

# use the dict's update() method to update 1 or multiple values
member.update({'name': 'Maynard James Keenan', 'age': 56, 'location': 'Arizona'})

print(member)

print(members)

print('\n****************************************\n')

# use the del keyword to delete a key-value pair
del members[5]

del members[6]

print(members)

print('\n****************************************\n')

# the dict's pop() method removes a key & also returns its value which can be assigned to a var
asshole = members.pop(7)

print(asshole)

print(members)

print('\n****************************************\n')

print('There are', len(members), 'members in Tool')

print('\n****************************************\n')

# retrieve all the keys using the keys() method
print(member.keys())

# retrieve all the values using the values() method
print(member.values())

# retrieve all the key-value pairs using the items() method
print(member.items())

print('\n****************************************\n')

for key in member:
    print(key)

print('~~~~~~~~~~~~~~~~~~~~~~')

for key in members.keys():
    print(key)

print('~~~~~~~~~~~~~~~~~~~~~~')

for val in members.values():
    print(val)

print('~~~~~~~~~~~~~~~~~~~~~~')

for key, val in member.items():
    print(key,':', val)