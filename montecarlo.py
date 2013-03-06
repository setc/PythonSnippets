#-------------------------------------------------------------------------------
# Name:        Montecarlo z(x,y)
# Purpose:      The following snippet of code is a function to calculate an
# integral using the Montecarlo method. There are already in NumPy modules
# better suited for this task. And more efficient ways to calculate the integral
# This is only a translation of an old program I did in Fortran to practice
# some Python.
#
# Author:      Sebastián Torrente
#-------------------------------------------------------------------------------

"""
Variables of the function are:
    lim_x: an array containing the lower and upper limits of the x variable
    lim_y: same as above but for the y variable.
    Note that in some cases the integral limits are not going to be as smooth as
    a simple square. We can get something like:
        x=[0.0,3.0]
        y=[0.0, f(y)=exp(x)]
        Use lambda functions in that case.
    func:   the function you want to calculate
    points: the number of points you want to use to calculate the integral
"""

import random

def montecarlo(lim_x,lim_y,func,points):
    """Montecarlo integral for a function z(x,y), for a future project I'll try
    to use arrays for the limits of the integral so you can make the integral in
    an arbitrary number of variables."""

    hits=0.0
    rangex=lim_x[1]-lim_x[0] #We don't need to calculate this all the time
    rangey=lim_y[1]-lim_y[0] #in the for loop.

    for i in range(1,points):

        x=lim_x[0]+rangex*random.random()
        y=lim_y[0]+rangey*random.random()

        hits=hits+func(x,y)

    return hits/points

if __name__ == '__main__':

    def z(x,y):
        return x*y+x+y

    lim_x=[0.0,5.0]
    lim_y=[0.0,5.0]
    points=1000000

    integral=montecarlo(lim_x,lim_y,z,points)
    print (integral)
