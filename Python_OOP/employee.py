import datetime

'''
******* => separate different lessons (based on the vids)

------- => separate different sections in a lesson

~~~~~~~ => separate different sub-sections in a section
'''

class Employee:    
    # pass is a null statement, which's generally used as a placeholder
    # While the Python interpreter ignores a comment entirely, pass is not ignored
    # However nothing happens when pass is executed, it results into no operation (NOP)
    # Suppose we have a loop, a function/method or a class that is not implemented yet but we want to implement it in the future.     
    # They cannot have an empty body, the interpreter would complain    
    # So, we use the pass statement to construct a body that does nothing   
    #pass

    # a class var is shared among all instances of a class
    annual_raise = 1.05
    number_of_emps = 0

    def __init__(self, first_name, last_name, pay):
        # define the atrributes/instance vars/pieces of data unique to each instance
        self.f_name = first_name # self.f_name = emp1.firstName
        self.l_name = last_name
        self.p = pay
        #self.email = first_name + last_name + '@blackmesa.com'

        # seeking a more thorough explanation for this.... 
        Employee.number_of_emps += 1

    # a regular method automatically takes an instance as its 1st param (self)
    def get_fullName(self):
        return '{} {}'.format(self.f_name, self.l_name)
    
    def apply_raise(self):
        #self.p = int(self.p * 1.05)

        # access a class var either thru the class itself (Employee.annual_raise) 
        # or thru an instance (self.annual_raise) (*)
        self.p = int(self.p * self.annual_raise)

    # @classmethod: a decorator that alters a method's functionalities 
    # a class method receives the class as its 1st arg, instead of the instance
    # cls is a conventional way to name the 1st param/arg that represents the class, 
    # like "self" to an instance in a regular method
    @classmethod 
    def set_raised_amt(cls, amount):
        cls.annual_raise = amount

    @classmethod
    def from_string(cls, emp_str):
        f_name, l_name, pay = emp_str.split('-')

        return cls(f_name, l_name, pay)
    
    # static methods don't take any arg as its 1st param that's passed to it automatically 
    # like class methods (cls) or regular methods (self)
    # a static method is declared in a class because it has some logical connections with that class
    # but doesn't depend on, access or operate on any specific instance or class variables
    @staticmethod
    def is_workday(day):
        # the weekday() method: Mon (0) | Tue (1) | Wed (2) | Thu (3) | Fri (4) | Sat (5) | Sun (6)
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        
        return True
    
    # special/magic/dunder methods are surrounded by double underscores (Ex: __init__())
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.f_name, self.l_name, self.p)
    
    def __str__(self):
        return 'Employee full name: {} - Email: {}'.format(self.get_fullName(), self.email)
    
    def __add__(self, other):
        return self.p + other.p
    
    def __len__(self):
        return(len(self.get_fullName()))
    
    # property decorators (Getters, Setters & Deleters) allow us to define a method & access it as if it were an attribute
    @property
    def email(self):
        return '{}{}@blackmesa.com'.format(self.f_name, self.l_name)
    
    @property
    def fullName(self):
        return '{} {}'.format(self.f_name, self.l_name)
    
    # define a setter
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')

        self.f_name = first

        self.l_name = last
    
    # define a deleter (a clean-up code), which will run whenever an attribute is removed
    @fullName.deleter
    def fullName(self):
        print('\n\tDelete Name')

        self.f_name = None

        self.l_name = None

'''
# creating the Employee instances manually (without __init__()) => not recommended
emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

# creating instance variables whose attributes are unique to each instance
emp1.firstName = 'Billy'
emp1.lastName = 'Howerdel'
emp1.email = 'billy@blackmesa.com'
emp1.pay = 1000

emp2.firstName = 'Adam'
emp2.lastName = 'Jones'
emp2.email = 'adam@blackmesa.com'
emp2.pay = 2000

print(f'\nemployee 1 email: {emp1.email} & employee 2 email: {emp2.email}')
'''

print('\n[ The current number of employees: ' + str(Employee.number_of_emps) + ' ]\n')

# initializing instances thru __init__() => recommeded, less error-prone
# args: (first_name, last_name, pay)
# self: the instance itself (emp3) is passed to __init__() automatically, implicitly
# => self can be omitted when initializing an instance this way
emp3 = Employee('Justin', 'Chancellor', 3000) 

print(emp3)
print(emp3.email)

emp4 = Employee('Danny', 'Carey', 4000)

print(emp4)
print(emp4.email)

print(f'\nemployee 3 email: {emp3.email} & employee 4 email: {emp4.email}')

# form an employee's full name manually without calling any specific method
print('\nemployee 3 full name: {} {}'.format(emp3.f_name, emp3.l_name))

# use a specific method to get an employee's full name
# the instance itself (emp4) is passed to get_fullName() automatically, implicitly
print('\nemployee 4 full name: ' + emp4.get_fullName())

emp5 = Employee('Paul', "D'Amour", 5000)

# call a method using the class name 
# => the instance itself (emp5) must be passed to the method call as an arg explicitly (emp5 = self)
# => Employee.get_fullName(emp5) = emp5.get_fullName()
print('\nemployee 5 full name: ' + Employee.get_fullName(emp5) + ' = ' + emp5.get_fullName())

print('\n************************************************************************************************************')

print('\nemployee 3 salary: $' + str(emp3.p))

emp3.apply_raise()

print('\nemployee 3 salary + the annual raise: $' + str(emp3.p))

# (*) why can we access annual_raise thru an instance? (self.annual_raise)
'''
- When we access an instance's attribute, Python will check that instance to see if it contains the attribute

- If it doesn't, then the class will be checked if it contains the attribute

- emp4 & emp5 don't contain annual_raise, hence we access annual_raise thru the class itself 
'''
print('\nEmployee.annual_raise: ' + str(Employee.annual_raise))

print('\nemp4.annual_raise: ' + str(emp4.annual_raise))

print('\nemp5.annual_raise: ' + str(emp5.annual_raise))

# check the actual attributes an instance or a class contains by printing out its namespace
# more about namespaces: https://www.programiz.com/python-programming/namespace 
print('\n+ The current attributes emp4 contains:')

for a in emp4.__dict__:
    print(f'\n\t-> {a} : {emp4.__dict__[a]}')

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('\n+ The attributes the class itself contains:')

for a in Employee.__dict__:
    print(f'\n\t-> {a} : {Employee.__dict__[a]}')

# altering the class's annual_raise also changes its instances' annual_raise
Employee.annual_raise = 1.03

print('\nEmployee.annual_raise: ' + str(Employee.annual_raise))

print('\nemp4.annual_raise: ' + str(emp4.annual_raise))

print('\nemp5.annual_raise: ' + str(emp5.annual_raise))

print('\n------------------------------------------------------------------------------------------------------------')

# altering an instance's annual_raise doesn't change the class's or any other instances' annual_raise
emp4.annual_raise = 1.07

print('\nEmployee.annual_raise: ' + str(Employee.annual_raise))

print('\nemp4.annual_raise: ' + str(emp4.annual_raise))

print('\nemp5.annual_raise: ' + str(emp5.annual_raise))

# furthermore the alteration creates an actual attribute named annual_raise in that instance
print('\n+ The current attributes emp4 contains:')

for a in emp4.__dict__:
    print(f'\n\t-> {a} : {emp4.__dict__[a]}')

print('\n[ The current number of employees: ' + str(Employee.number_of_emps) + ' ]\n')

print('\n************************************************************************************************************')

emp6 = Employee('Layne', 'Staley', 6000)

# calling the set_raised_amt() class method is equivalent to "Employee.annual_raise = 1.08"
# we're working with the class now, not the instances
# you can call the class method on an instance but it's pointless to do so
Employee.set_raised_amt(1.08) 

print('\nEmployee.annual_raise: ' + str(Employee.annual_raise))

print('\nemp5.annual_raise: ' + str(emp5.annual_raise))

print('\nemp6.annual_raise: ' + str(emp6.annual_raise))

print('\n------------------------------------------------------------------------------------------------------------')

# use a class method as an alternative constructor to provide multiple ways for creating instances
# an use case: someone's getting employee info in the form of a string separated by hyphens (-)
# and they need to parse the string before creating new employees
# they want to pass the string to a class method from which an employee can be created
emp_str_7 = 'Jerry-Cantrell-7000'

emp_str_8 = 'Chris-Cornell-8000'

emp_str_9 = 'Scott-Weiland-9000'

f_name, l_name, pay = emp_str_7.split('-')

emp7 = Employee(f_name, l_name, pay) # construct an instance without using a class method

print(f'\nemployee 7 email & pay: {emp7.email} | {emp7.p}')

emp8 = Employee.from_string(emp_str_8) # use from_string() as an alternative constructor

emp9 = Employee.from_string(emp_str_9)

print(f'\nemployee 8 email & pay: {emp8.email} | {emp8.p}')

print(f'\nemployee 9 email & pay: {emp9.email} | {emp9.p}')

print('\n------------------------------------------------------------------------------------------------------------')

my_date = datetime.date(2019, 12, 3)

print(Employee.is_workday(my_date)) # call the is_workday() static method

print('\n************************************************************************************************************')

# creating subclasses that inherit from the Employee class
class Developer(Employee):
    #pass

    annual_raise = 1.1

    def __init__(self, first_name, last_name, pay, prog_lang):
        # super().__init__() calls the superclass's __init__() -> recommended
        # or: Employee.__init__(self, first_name, last_name, pay) -> not really recommended
        super().__init__(first_name, last_name, pay)

        self.prog_lang = prog_lang 

dev1 = Developer('Forrest', 'Knight', 10000, 'Java')

dev2 = Employee('Corey', 'Schafer', 11000)

print(f'\ndeveloper 1 & 2 emails: {dev1.email} | {dev2.email}\n')

print(help(Developer))

print(f'\ndeveloper 1 salary: $ {dev1.p}')

dev1.apply_raise()

print(f'\ndeveloper 1 salary + the annual raise: $ {dev1.p}')

# note: changing a subclass's annual_raise doesn't affect any Employee instance's annual_raise
# dev1 (Developer): 10000 * 1.1 | dev2 (Employee): 11000 * 1.08
print(f'\ndeveloper 2 salary: $ {dev2.p}')

dev2.apply_raise()

print(f'\ndeveloper 2 salary + the annual raise: $ {dev2.p}')

print(f'\ndeveloper 1 email & programming language: {dev1.email} | {dev1.prog_lang}')

print('\n------------------------------------------------------------------------------------------------------------')

class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        # None is used as a default arg here because mutable data types (list or dictionary) shouldn't be passed to a method as default args
        super().__init__(first_name, last_name, pay)

        # if no arg is provided, the emp_list attribute is set to an empty list. Otherwise, it's set to employees
        if employees is None:
            self.emp_list = []
        else:
            self.emp_list = employees

    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
    
    def print_emps(self):
        for emp in self.emp_list:
            print('\n\t->', emp.get_fullName())

manager = Manager('Joni', 'Mitchell', 12000, [dev1])

print(f'\nmanager email: {manager.email}')

manager.add_emp(dev2)

manager.print_emps()

manager.remove_emp(dev2)

manager.print_emps()

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# the isinstance() built-in function checks if an instance belongs to a specific class
print(isinstance(manager, Manager))

print(isinstance(manager, Employee))

print(isinstance(manager, Developer)) # even though Manager & Developer both inherit from Employee, they're distinct classes

# the issubclass() built-in function checks if a class is another class's subclass
print(issubclass(Developer, Employee))

print(issubclass(Manager, Employee))

print(issubclass(Developer, Manager))

print(issubclass(Manager, Developer))

print(issubclass(Developer, Developer))

print(issubclass(Manager, Manager))

print(issubclass(Developer, object)) # all classes are subclasses of the object class in python

print('\n************************************************************************************************************')

# implement 2 common dunder methods defined in Employee: __repr__() & __str__()
print(manager)

print(repr(dev2))

print(emp7.__str__())

# implement dunder methods for arithmetic
print(int.__add__(1, 2))

print(str.__add__('a', 'b'))

print('employee 3 salary + employee 4 salary: ' + str(emp3 + emp4))

# the len() is also a special method
print(len('the length of this string'))

print('the length of this string'.__len__())

print(len(emp8))

print('\n************************************************************************************************************')

emp10 = Employee('Maynard', 'Keenan', 13000)    

print(f'\nemployee 10 1st name: {emp10.f_name} | email: {emp10.email} | full name: {emp10.get_fullName()}')

emp10.f_name = 'Jimmy'

print(f'\nemployee 10 1st name: {emp10.f_name} | email: {emp10.email} | full name: {emp10.get_fullName()}')

print(f'\nemployee 10 1st name: {emp10.f_name} | email: {emp10.email} | full name: {emp10.fullName}')

emp10.fullName = 'Corey Taylor'

print(f'\nemployee 10 1st name: {emp10.f_name} | email: {emp10.email} | full name: {emp10.fullName}')

del emp10.fullName

print(f'\nemployee 10 1st name: {emp10.f_name} | email: {emp10.email} | full name: {emp10.fullName}')