modules=dict()
flipflip=dict()
conj=dict()

for l in open('input.txt', 'r').readlines():
    sender=l[:l.index(' ')]
    if sender[0]=='%':
        sender=sender[1:]
        flipflip[sender]=False #off
    elif sender[0]=='&':
        sender=sender[1:]
        conj[sender]=dict()
    modules[sender]=[m.strip() for m in l[l.index('>')+2:].split(',')]

for s,l in modules.items():
    for r in l:
        if r in conj:
            conj[r][s]=False #low pulse

lows=highs=0
for i in range(1000):
    lows+=1
    queue=[]
    queue.append(('broadcaster',False))
    while queue:
        sender,high = queue.pop(0)
        for receiver in modules[sender]:
            if high:
                highs+=1
            else:
                lows+=1 
            if receiver in flipflip and not high:
                if flipflip[receiver]:
                    flipflip[receiver]=False
                    queue.append((receiver,False))
                else:
                    flipflip[receiver]=True
                    queue.append((receiver,True))
            elif receiver in conj:
                conj[receiver][sender]=high
                if not False in conj[receiver].values():
                    queue.append((receiver,False))
                else:
                    queue.append((receiver,True))
print(highs*lows)