import urllib,re
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
seed="12345"
for i in range(400):
    text=urllib.urlopen(url+seed).read()
    seed="".join(re.findall(r"nothing is (\d+)",text))
    try :
        int(seed)
        print "   Next:",seed
    except :
        print "   Last:",text
        break
