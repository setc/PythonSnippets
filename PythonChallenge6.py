import zipfile, re

channel = zipfile.ZipFile('channel.zip', 'r')
index = '90052'
path=[]

while True:
    path.append(index)
    datafile = file.read(index + '.txt')
    print(index + '  ',data)
    index = "".join(re.findall('[0-9.]', datafile))
    if len(index) == 1:
        break

print ''.join([file.getinfo(i+'txt').comment for i in path])
