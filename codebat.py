#-------------------------------------------------------------------------------
# Name:        Codebat Exercises
# Purpose:     Just some solutions of the http://codingbat.com exercises.
#
# Author:      SebastiÃ¡n Torrente
#
# Created:     05/10/2012
# Copyright:   (c) SebastiÃ¡n Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def double_char(string):
    """Take a string "abc" and returns a string with every character doubled"""
    double=""
    for char in str:
        double=double+char*2
    return double

def count_hi(string):
    """Return the number of times that the string "hi" appears anywhere in the
    given string. """
    return string.count('hi')

def count(string,str_count):
    """Return the number of times that the string str_count appears anywhere in
    the given string. Very trivial."""
#   Quite trivial, most probably I will delete it when this file gets too big.
    return string.count(str_count)

def cat_dog(str):
    """Return true if the string has the same number of 'cat' and 'dog'. This
    function is case sensitive"""
    return string.count('cat')==string.count('dog')

def end_other(a, b):
    """Given two strings, return True if either of the strings appears at the
    very end of the other string, ignoring upper/lower case differences (in
    other words, the computation should not be "case sensitive"). """
    if len(a) <= len(b):
        long_str = b
        short_str = a
    else:
        long_str = a
        short_str = b
    return long_str.lower().endswith(short_str.lower())

def count_code(string):
    """Return the number of times that the string "code" appears anywhere in the
    given string, except we'll accept any letter for the 'd', so "cope" and
    "cooe" count."""
    #Hardest one of the lot. You could do it counting with a for loop and
    #str[i:i+1]="co" str[i+3]="e". But there must be a most elegant way. Using
    #regex or the like.
    return True

def xyz_there(string):
    """Return True if the given string contains an appearance of "xyz" where th
    e xyz is not directly preceeded by a period (.). So "xxyz" counts but
    "x.xyz" does not. """
    #Now, there is a tricky one. I guess you can do it with a regex, but I'm not
    #so proficient in them now as I wish I was. So I'll try a dirty trick.
    return str.replace(".xyz","").count("xyz")!=0

def make_bricks(small, big, goal):
    """We want to make a row of bricks that is goal inches long. We have a
    number    of small bricks (1 inch each) and big bricks (5 inches each).
    Return True if it is possible to make the goal by choosing from the given
    bricks. This is a little harder than it looks and can be done without any
    loops."""
    #I really like this one. Is way simpler than it seems.
    return True


if __name__ == '__main__':
    main()
