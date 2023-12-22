from math import lcm
modules=dict()
flipflop=dict()
conj=dict()

for l in open('input.txt', 'r').readlines():
    sender=l[:l.index(' ')]
    if sender[0]=='%':
        sender=sender[1:]
        flipflop[sender]=False #off
    elif sender[0]=='&':
        sender=sender[1:]
        conj[sender]=dict()
    modules[sender]=[m.strip() for m in l[l.index('>')+2:].split(',')]

for s,l in modules.items():
    for r in l:
        if r in conj:
            conj[r][s]=False #low pulse

# identify frequency of high pulses sent per module
high_pulse_freq=dict()
for m in modules.keys():
    high_pulse_freq[m]=[]
for i in range(1,10000):
    queue=[]
    queue.append(('broadcaster',False))
    while queue:
        sender,high = queue.pop(0)
        if high:
            high_pulse_freq[sender].append(i)
        for receiver in modules[sender]:
            if receiver in flipflop and not high:
                if flipflop[receiver]:
                    flipflop[receiver]=False
                    queue.append((receiver,False))
                else:
                    flipflop[receiver]=True
                    queue.append((receiver,True))
            elif receiver in conj:
                conj[receiver][sender]=high
                if not False in conj[receiver].values():
                    queue.append((receiver,False))
                else:
                    queue.append((receiver,True))

# identify module sending pulses to rx
s=[*modules.keys()][[*modules.values()].index(['rx'])]
# we assume this is a conjunction module (may not be the case for other input files!)
# and therefore need to identify when at the earliest all its inputs send a high pulse
freqs=[]
for m,v in modules.items():
    if s in v:
        freqs.append(high_pulse_freq[m][0])
print(lcm(*freqs))