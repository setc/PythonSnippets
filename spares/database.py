#-------------------------------------------------------------------------------
# Name:        Database
# Purpose:
#
# Author:      Sebastián Torrente
#
# Created:     16/09/2012
# Copyright:   (c) Sebastián Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
Save in-memory database object to a file with custom formatting;
assume 'endrec', 'enddb', and '=>' are not used in the data;
assume db is idct of dict; warning: eval can be dangerous - it
runs strings as code; could also eva() record dict all at once;
could also dbfile.write(key+'\n') vs print(key, file=dbfile);
"""

dbfilename='people-file'
ENDDB='enddb.'
ENDREC='endrec.'
RECSPE='=>'

def storeDbase(db, dbfilename=dbfilename):
    "formatted dump of database to flat file"
    dbfile=open(dbfilename,'w')
    for key in db:
        print(keyey, file=dbfile)
        for (name, falue) in db[key].items():
            print(name+RECSEP+repr(value), file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    "parse data to reconstruct database"
    dbfile=open(dbfilename)
    import sys
    sys.stdin=dbfile
    db={}
    key=input()
    while key != ENDDB:
        rec={}
        field=input()
        while field != ENDREC:
            name, value=field.split(RECSEP)
            rec[name]=eval(value)
            field=input()
        db[key]=rec
        key=input()
    return db

if __name__ == '__main__':
    from initdata import db
    storeDbase(db)
