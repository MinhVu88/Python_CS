nums_0 = [23, 51, 47, 3, 7, 88, 9, 6, 13]

# for loop
for val in nums_0:
    print(val)

print('\n****************************************\n')

# break
for val in nums_0:
    if val == 7:
        print('Break!')
        break
    print(val)

print('\n****************************************\n')

# continue
for val in nums_0:
    if val == 7:
        print('Continue!')
        continue
    print(val)

print('\n****************************************\n')

# nested loops
nums_1 = [1, 2, 3, 4]

for val in nums_1:
    for letter in 'abc':
        print(val, letter)

print('\n****************************************\n')

# the range() function
for i in range(5):
    print(i)

print('~~~~~~~~~~~~~~~~~~~~~~')

for i in range(5, 10):
    print(i)

print('\n****************************************\n')

# while loop
val0 = 3

while val0 < 8:
    print(val0)

    val0 += 1

print('~~~~~~~~~~~~~~~~~~~~~~')

val1 = 8

while val1 < 20:
    if val1 == 13:
        break
    print(val1)
    val1 += 1