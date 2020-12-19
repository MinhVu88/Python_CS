def square_nums_0(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result

nums_0 = [1, 2, 3, 4, 5]

print(square_nums_0(nums_0))

print('\n****************************************\n')

# apply generator by using the 'yield' keyword (recommended)
def square_nums_1(nums):
    for i in nums:
        yield(i * i)

nums_1 = [6, 7, 8, 9, 10]

print(square_nums_1(nums_1)) # printing out the generator object

print('~~~~~~~~~~~~~~~~~~~~~~')

nums_1_val = square_nums_1(nums_1)

print(next(nums_1_val))
print(next(nums_1_val))
print(next(nums_1_val))
print(next(nums_1_val))
print(next(nums_1_val))

#print(next(nums_1_val)) # Error: StopIteration -> the whole generator has been exhausted, no values left to retrieve

print('~~~~~~~~~~~~~~~~~~~~~~')

for num in square_nums_1(nums_1):
    print(num)

print('\n****************************************\n')

# apply list comprehension (without generator)
nums_2 = [num * num for num in [11, 12, 13, 14, 15]]

print(nums_2)

for num in nums_2:
    print(num)

print('~~~~~~~~~~~~~~~~~~~~~~')

# list comprehension with generator
nums_3 = (num * num for num in [16, 17, 18, 19, 20])

print(nums_3)

for num in nums_3:
    print(num)

nums_4 = list((num * num for num in [16, 17, 18, 19, 20])) # convert a generator into a list

print(nums_4)