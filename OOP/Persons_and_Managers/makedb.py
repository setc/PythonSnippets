#makedb.py
#And finally, we need a place to store those employees.
"""
In this module we use the shelve module to store the data
created using the other two modules.
"""

from person import Person, Manager

#Our registry of employees
bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()
