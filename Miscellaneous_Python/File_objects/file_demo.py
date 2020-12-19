# READING FROM FILES
# open the file by using the open() function
file_path_0 = 'Miscellaneous_Python/File_objects/test1.txt'

file_0 = open(file_path_0, 'r') # r: read

print(file_0.name)

print(file_0.mode)

file_0.close()

print('\n****************************************\n')

''' Context Managers & the “with” Statement (online references):

    https://dbader.org/blog/python-context-managers-and-with-statement

    https://stackabuse.com/python-context-managers/

    https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

    https://alysivji.github.io/managing-resources-with-context-managers-pythonic.html

    https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

    https://www.geeksforgeeks.org/context-manager-in-python/

    https://www.geeksforgeeks.org/with-statement-in-python/

    https://medium.com/better-programming/context-managers-in-python-dbfaf568092
'''
# open the file by using context manager (recommended)
with open(file_path_0, 'r') as file_1:
    file_contents = file_1.read()

    print(file_contents)

print(file_1.closed)

print('\n****************************************\n')

with open(file_path_0, 'r') as file_2:
    file_contents = file_2.readlines()

    print(file_contents)

print('\n****************************************\n')

with open(file_path_0, 'r') as file_3:
    file_contents = file_3.readline()

    #  print() adds a new line after each output by default, so end='' removes that extra new line
    print(file_contents, end='')

    file_contents = file_3.readline()

    print(file_contents, end='')

print('\n****************************************\n')

with open(file_path_0, 'r') as file_4:
    for line in file_4:
        print(line, end='')

print('\n\n****************************************\n')

with open(file_path_0, 'r') as file_5:
    # specify the amount of data read from the file by passing in an int/None as an arg to read()
    # 100 -> the 1st 100 characters in the file
    file_contents = file_5.read(100) 

    print(file_contents, end='')

    file_contents = file_5.read(100) # the next 100 chars

    print(file_contents, end='')

    # when the end of the file is reached, read() returns an empty string
    file_contents = file_5.read(100) 

    print(file_contents, end='')

print('\n\n****************************************\n')

with open(file_path_0, 'r') as file_6:
    size_to_read = 10

    file_contents = file_6.read(size_to_read)

    # some kind of loop is used to iterate over a file, whose size/length is unknown
    # in the while loop below, with each iteration, 10 characters are read from test.txt at a time
    # those 10 characters are printed out & asterisk-separated between them throughout the output
    # the loop's condition returns true until the file's end is reached as read() then returns an empty string
    # that empty string renders the loop's condition false
    while len(file_contents) > 0:
        print(file_contents, end='*')

        file_contents = file_6.read(size_to_read)

print('\n\n****************************************\n')

with open(file_path_0, 'r') as file_7:
    size_to_read = 10

    file_contents = file_7.read(size_to_read)

    # when a file's read, read() advances its position every time throughout the file's contents
    # the tell() method returns the current position of read() in the file
    print(file_7.tell())

print('\n****************************************\n')

with open(file_path_0, 'r') as file_8:
    size_to_read = 10

    file_contents = file_8.read(size_to_read)

    print(file_contents, end='')

    # the 2nd read() picks up where the 1st one left off (the 10th position) & reads the next 10 chars
    # seek(0) moves the 2nd read() back to the beginning of the file
    file_8.seek(0)

    file_contents = file_8.read(size_to_read)

    print(file_contents, end='')

# WRITING TO FILES
file_path_1 = 'Miscellaneous_Python/File_objects/test2.txt'

# w: write
with open(file_path_1, 'w') as file_9:
    #pass

    file_9.write('Test')

    file_9.seek(0)

    #file_9.write('Test') # by calling seek(0), this 2nd 'Test' overwrites the 1st one

    file_9.write('B') # by calling seek(0), 'B' overwrites the 'T' in Test

# USING READ & WRITE MODES ON MULTIPLE FILES SIMULTANEOUSLY
# write the contents of test1.txt to test2.txt (this also overwrites the contents of test2.txt)
with open(file_path_0, 'r') as file_10:
    with open(file_path_1, 'w') as file_10_copy:
        for line in file_10:
            file_10_copy.write(line)

# COPYING AN IMAGE FILE
# for an image file like a jpg, that file must be opened in binary mode -> bytes are read from or written to the file, not text
img_path_0 = 'Miscellaneous_Python/File_objects/lain_1.jpg'

img_path_1 = 'Miscellaneous_Python/File_objects/lain_2.jpg'

# rb: read bytes | wb: write bytes
with open(img_path_0, 'rb') as img_0:
    with open(img_path_1, 'wb') as img_0_copy:
        for i in img_0:
            img_0_copy.write(i)

# USING A LOOP TO COPY AN IMAGE FILE (for finer control over what's being read from/written to a file)
img_path_2 = 'Miscellaneous_Python/File_objects/johan_1.jpg'

img_path_3 = 'Miscellaneous_Python/File_objects/johan_2.jpg'

with open(img_path_2, 'rb') as img_1:
    with open(img_path_3, 'wb') as img_1_copy:
        size_to_read = 5000

        img_1_size = img_1.read(size_to_read)

        while len(img_1_size) > 0:
            img_1_copy.write(img_1_size)

            img_1_size = img_1.read(size_to_read)
