time,distance = [int(l[l.index(':')+1:].strip().replace(' ','')) for l in open('input.txt', 'r').readlines()]
ways=0
for hold in range(time+1):
    if hold*(time-hold)>distance:
        ways+=1
print(ways)