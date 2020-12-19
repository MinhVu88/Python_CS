import sqlite3
from employee import Employee

# store data in a file
#connection = sqlite3.connect('Miscellaneous_Python/Python_SQLite/employee.db')

# store data in an in-memory database
''' Online references:
    https://www.sqlite.org/inmemorydb.html

    https://en.wikipedia.org/wiki/In-memory_database

    https://medium.com/@denisanikin/what-an-in-memory-database-is-and-how-it-persists-data-efficiently-f43868cff4c1

    https://raima.com/in-memory-database/

    https://hazelcast.com/glossary/in-memory-database/

    https://www.omnisci.com/learn/resources/technical-glossary/In-memory-database
'''
connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

# create the employee table by specifying the following sql command
cursor.execute(""" CREATE TABLE employees (
                   first_name text,
                   last_name text,
                   pay integer
              ) """)

# method 0: insert hardcoded values into employee.db without using any class instances & placeholders
cursor.execute("INSERT INTO employees VALUES ('Maynard', 'Keenan', 9000)")
cursor.execute("INSERT INTO employees VALUES ('Mike', 'Keenan', 7000)")
cursor.execute("INSERT INTO employees VALUES ('Judith', 'Keenan', 5000)")
connection.commit()
cursor.execute("SELECT * FROM employees WHERE last_name='Keenan'")
print(cursor.fetchall())

# 2 other methods of fetching data from a database
#print(cursor.fetchone())
#print(cursor.fetchmany(5))

# creating Employee instances
emp_1 = Employee('Adam', 'Jones', 3000)

emp_2 = Employee('Justin', 'Chancellor', 6000)

emp_3 = Employee('Dan', 'Carey', 8000)

# method 1: insert Employee instances into employee.db using placeholder (recommended)
cursor.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first_name, emp_1.last_name, emp_1.pay))

connection.commit()

# method 2: insert Employee instances into employee.db using placeholder (also recommended)
cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
              {'first': emp_2.first_name, 'last': emp_2.last_name, 'pay': emp_2.pay})

connection.commit()

cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
              {'first': emp_3.first_name, 'last': emp_3.last_name, 'pay': emp_3.pay})

connection.commit()

cursor.execute("SELECT * FROM employees WHERE last_name=?", ('Keenan',))
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees WHERE last_name=:last", {'last': 'Jones'})
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees WHERE last_name=:last", {'last': 'Chancellor'})
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees WHERE last_name=:last", {'last': 'Carey'})
print(cursor.fetchall())

connection.commit() # commit the current transaction

connection.close()