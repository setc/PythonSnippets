#-------------------------------------------------------------------------------
# Name:        ex16
# Purpose:
#
# Author:      Sebastián Torrente
#
# Created:     12/08/2012
# Copyright:   (c) Sebastián Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sys import argv

script, filename=argv

print("We're going to earse %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target=open(filename, 'w')

print("Truncating the file. Good grief!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1=input("Line 1:")
line2=input("Line 2:")
line3=input("Line 3:")

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()