import re
from functools import reduce
result=0
for line in open('input.txt', 'r').readlines():    
    game = re.split(':|,|;', line)
    nr = int(game[0].split(' ')[1])
    d={'red':0, 'green':0, 'blue':0}
    for dice in game[1:]:
        m = re.match(r" (\d+) ((blue)|(green)|(red)).*", dice)
        d[m.group(2)]=max(d[m.group(2)],int(m.group(1)))
    result+=reduce((lambda x, y: x * y), d.values())
print(result)        