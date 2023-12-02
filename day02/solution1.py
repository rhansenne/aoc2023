import re
result=0
for line in open('input.txt', 'r').readlines():    
    game = re.split(':|,|;', line)
    nr = int(game[0].split(' ')[1])
    for dice in game[1:]:
        m = re.match(r" (\d+) ((blue)|(green)|(red)).*", dice)
        cnt=int(m.group(1))
        color=m.group(2)
        if (color=='red' and cnt>12) or (color=='green' and cnt>13) or (color=='blue' and cnt>14):
            break
    else:
        result+=nr
print(result)        