#-------------------------------------------------------------------------------
# Name:        Wulin dice
# Purpose:      A legend of the Wulin dice roller.
#
# Author:      Sebastián Torrente
#
# Created:     02/10/2012
# Copyright:   (c) Sebastián Torrente 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def diceroll(dices=1):
    roll=[]
    for i in range(dices):
        roll.append(random.randint(1,10))
    return roll.sort()

def calcroll(roll):
    result=[]
    values=[1,2,3,4,5,6,7,8,9,10]
    for number in values:
        amount_of_number=roll.count(number)
        if amount_of_number!=0:
            result.append(amount_of_number*10+number)
    return result.sort()

def adbonus(roll,bonus):
    return roll+bonus



if __name__ == '__main__':
    tirada=diceroll(6)
    print (tirada)
    tirada2=diceroll(4)
    print (tirada2)
