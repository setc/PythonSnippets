#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sebastián Torrente
#
# Created:     11/08/2012
# Copyright:   (c) Sebastián Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sys import argv

script, user_name=argv
prompt='>'

print("Hi %s, I'm like the %s script." % (user_names, script))
print("I'd like to ask you a few questions.")

print("Do you like me %s?" % user_name)
likes=input(prompt)

print("Where do you live %s?" % user_name)
computer=input(prompt)

print("""
Alrgiht, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

