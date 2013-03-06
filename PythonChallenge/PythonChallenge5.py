# -*- coding: cp1252 -*-
#-------------------------------------------------------------------------------
# Name:        Python Challenge 5
# Purpose:     Using a pickle object.
#
# Author:      Sebastián Torrente
#
# Created:     19/12/2012
# Note:        This one needed some research, because the jump
#              form 'peak hell' to 'pickle'
#-------------------------------------------------------------------------------

import pickle, urllib2

fileurl = 'http://www.pythonchallenge.com/pc/def/banner.p'

picklefile = pickle.load(urllib2.urlopen(fileurl))

for data in picklefile:
    print(data)

#Ok, so we have a lot of lines with two elements tuples, each one
#with a ' '  or a '#' as a first element and a number. It may be
#text art.

art = [] #Each element of this list is a line that we will draw
         #later.

for data in picklefile:
    for dataduo in data:
        art.append(dataduo[0]*dataduo[1]) #We create a line with
                                          #each element repeated
                                          #its number of times.
    art.append('\n')

print("".join(art))
