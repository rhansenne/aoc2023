import re
records = [[int(s) for s in re.findall(r'\d+', l)] for l in open('input.txt', 'r').readlines()]
res=1
for i, time in enumerate(records[0]):
    ways=0
    for hold in range(time+1):
        if hold*(time-hold)>records[1][i]:
            ways+=1
    res*=ways
print(res)