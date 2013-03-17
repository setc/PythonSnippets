#person.py
#Advanced Persons & Managers
#
#This is the class example in Learn Python with employees and managers.
#Something good to have at hand as a reference

"""
This module contain the person class.
"""

class Person:
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
        