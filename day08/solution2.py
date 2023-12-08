import math
doc=open('input.txt', 'r').readlines()
instr=doc[0].strip()
network=dict([(l[0:3],(l[7:10],l[12:15])) for l in doc[2:]])
steps=set()
for node in filter(lambda n: n[2] == 'A', network.keys()): 
    step=0
    while node[2] != 'Z':
        node = network[node][0] if instr[step%len(instr)]=='L' else network[node][1]
        step+=1
    steps.add(step)
print(math.lcm(*steps))