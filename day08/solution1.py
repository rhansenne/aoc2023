doc=open('input.txt', 'r').readlines()
instr=doc[0].strip()
network=dict([(l[0:3],(l[7:10],l[12:15])) for l in doc[2:]])
node='AAA'
steps=0
while node != 'ZZZ':
    node = network[node][0] if instr[steps%len(instr)]=='L' else network[node][1]
    steps+=1
print(steps)