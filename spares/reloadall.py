"""
reloadall.py: transitively reload nested modules
"""

import types
from imp import reload                          #Only required in Python3

def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:             #To catch cycles and duplicates
        status(module)                                #Reload this module
        reload(module)                                #And visit children
        visited[module] = None
        for attrobj in module.__dict__.values():      #For all attrs
            if type(attrobj) == types.ModuleType:     #Recur if module
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

#Test: reload itself
if __name__ == '__main__':
    import reloadall
    reload_all(reloadall)
