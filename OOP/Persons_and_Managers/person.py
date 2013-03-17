#person.py
#Advanced Persons & Managers
#
#This is the class example in Learn Python with employees and managers.
#Something good to have at hand as a reference

"""
This module contain the Person class.
"""

from classtools import AttrDisplay

class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job = None, pay = 0):
        """
        Initiate the class. The three fields are:
        name: Name of the employee
        job : His/her job
        pay : How much it gains per month
        """
        self.name = name
        self.job  = job
        self.pay  = pay

#    def __str__(self):  ##Phased out due to the use of AttrDisplay
#        """
#        Format: [Name: John Doe, Job: Barbarian, Pay: 5000]
#        """
#        return '[Name: %s, Job: %s, Pay: %s]' % (self.name, self.job, self.pay)

    def firstName(self):
        """
        Return the first name of the employee.
        """
        return self.name.split()[0]

    def lastName(self):
        """
        Return the last name of the employee.
        """
        return self.name.split()[-1]

    def giveRaise(self, percent):
        """
        Update the pay by adding a raise based on percentage
        """
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    Managers get better raises, oh lalá.
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
        
        
if __name__ == '__main__':                              #Test de class
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)
#    print(bob.name," current pay is: ", bob.pay)
#    print(sue.name," current pay is: ", sue.pay)
    print(bob)
    print(sue)
    print("Bob Smit First Name is: ", bob.firstName())
    print("Sue Jones Last Name is: ", sue.lastName())
    sue.giveRaise(.10)
#    print("After a raise of 10% sue earns ",sue.pay)
    print(sue)
#    tom = Manager('Tom Jones', 'mgr', 50000)
    tom = Manager('Tom Jones', 50000)
    #Is not unusual to get a raise
    tom.giveRaise(.10)
    print('Tom Jones last name is: ', tom.lastName())
    print(tom)
