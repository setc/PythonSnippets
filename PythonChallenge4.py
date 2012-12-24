#Python Challenge 4
#Firs impression: clever bastards :)
#Time to parse som urls

baseurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

init_url = '12345'

def dig_the_url(url, init, depth):
    """
    Take a base url, parse init, read the resulting url and then read the
    numbers at the end of the new url. Repeat the process depth times.
    """
    import urllib2
    import re

    url = str(url)
    end = str(init)
    depth = int(depth)
    
    for i in range(depth):
        text = urllib2.urlopen(url+end).read()
        end="".join(re.findall(r"nothing is (\d+)", text))

        try:
            int(end)
            print(end)
        except:
            print(text)
            break

dig_the_url(baseurl,init_url,300)
dig_the_url(baseurl,16044/2,300)


    
