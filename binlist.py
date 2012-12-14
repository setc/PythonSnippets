#Test for the add8 function.

# SPECIFICATION:
#
# add8 emulates an 8-bit hardware adder.
# it takes 17 bits, representing two 8-bit
# numbers and a carry bit.
#
# TASK:
#
# Write test() such that it achieves 100% 
# statement coverage of the add8 function.

def add8(a0,a1,a2,a3,a4,a5,a6,a7,b0,b1,b2,b3,b4,b5,b6,b7,c0):
    s1 = False
    if (a0 != b0) != c0:
        s1 = True
    c1 = False
    if (a0 and b0) != (c0 and (a0 != b0)):
        c1 = True
    s2 = False
    if (a1 != b1) != c1:
        s2 = True
    c2 = False
    if (a1 and b1) != (c1 and (a1 != b1)):
        c2 = True
    s3 = False
    if (a2 != b2) != c2:
        s3 = True
    c3 = False
    if (a2 and b2) != (c2 and (a2 != b2)):
        c3 = True
    s4 = False
    if (a3 != b3) != c3:
        s4 = True
    c4 = False
    if (a3 and b3) != (c3 and (a3 != b3)):
        c4 = True
    s5 = False
    if (a4 != b4) != c4:
        s5 = True
    c5 = False
    if (a4 and b4) != (c4 and (a4 != b4)):
        c5 = True
    s6 = False
    if (a5 != b5) != c5:
        s6 = True
    c6 = False
    if (a5 and b5) != (c5 and (a5 != b5)):
        c6 = True
    s7 = False
    if (a6 != b6) != c6:
        s7 = True
    c7 = False
    if (a6 and b6) != (c6 and (a6 != b6)):
        c7 = True
    s8 = False
    if (a7 != b7) != c7:
        s8 = True
    c8 = False
    if (a7 and b7) != (c7 and (a7 != b7)):
        c8 = True
    return (s1,s2,s3,s4,s5,s6,s7,s8,c8)

#I'm aware that this function return the digits in the inverted order that the one used
#in add8. I haven't changed it because it makes no difference in the end (we are testing
#all the results and because I may use binlist in the future.
def binlist(n):
    """
    Take an integer between 0 and 256, turn it into a binary and return the
    the digits in a list.
    """
    if type(n) != int:
        raise Exception("Parameter not an integer")
    if n < 0 or n > 256:
        raise Exception("Number outside or range [0,256]")
    
    #Turning the number into a list.
    prevlist = list(str(bin(n)[2:]))
    for i in range(len(prevlist)):
        assert prevlist[i].isdigit()
        prevlist[i] = int(prevlist[i])

    #Adding the remaining zeroes.
    invertlist = prevlist[::-1]
    while len(invertlist) < 8:
        invertlist.append(0)
    deflist = invertlist[::-1]
    assert len(deflist) == 8

    return deflist

def testbin():
    for i in range(256):
        (binlist(i))

def testbin2():
    binlist(-3)

def testbin3():
    binlist(500)

def testbin4():
    binlist("a")
    
testbin()

#def test():
#    for i in range(256):
#        ibin = binlist(i)
#        for j in range(256):
#            jbin = binlist(j)
#            c0 = 0
#            add8(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]
#                ,j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],c0)
            

#test()
