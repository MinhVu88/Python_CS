import sqlite3
from employee import Employee

connection = sqlite3.connect(':memory:')

cursor = connection.cursor()

cursor.execute(""" CREATE TABLE employees (
                   first_name text,
                   last_name text,
                   pay integer
              ) """)

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
def insert_emp(emp):
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", 
                      {'first': emp.first_name, 'last': emp.last_name, 'pay': emp.pay})

def get_emps(lastName):
    cursor.execute("SELECT * FROM employees WHERE last_name=:last", {'last': lastName})

    return cursor.fetchall()

def remove_emp(emp):
    with connection:
        cursor.execute("DELETE from employees WHERE first_name=:first AND last_name=:last", 
                      {'first': emp.first_name, 'last': emp.last_name})

def update_pay(emp, pay):
    with connection:
        cursor.execute("UPDATE employees SET pay=:pay WHERE first_name=:first AND last_name=:last", 
                      {'first': emp.first_name, 'last': emp.last_name, 'pay': pay})

emp_1 = Employee('Elliot', 'Alderson', 2012)

emp_2 = Employee('Darlene', 'Alderson', 2006)

emp_3 = Employee('Edward', 'Alderson', 1963)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

emps = get_emps('Alderson')
print(emps)

update_pay(emp_1, 280652)

remove_emp(emp_3)

print(get_emps('Alderson'))

connection.close()