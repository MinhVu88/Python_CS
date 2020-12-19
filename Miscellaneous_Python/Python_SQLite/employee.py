class Employee:
    """A sample Employee class"""
    def __init__(self, firstName, lastName, pay):
        self.first_name = firstName
        self.last_name = lastName
        self.pay = pay
    
    @property
    def get_email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)
    
    @property
    def get_fullName(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def __repr__(self):
        return 'Employee: {} {} | Pay: ${}'.format(self.first_name, self.last_name, self.pay)