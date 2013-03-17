#updatedb.py
"""
Update a Person object in the database. More precisely, gives a raise.
"""

import shelve
db = shelve.open('persondb')        #We reopen the database

for key in sorted(db):              #And we print the data
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.10)                  #Sue sure is getting a lot of raises
db['Sue Jones'] = sue               #Employee of the year, that's for sure
db.close()
