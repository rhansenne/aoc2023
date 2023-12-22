import numpy as np
mp=np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])
ln=len(mp)
s_co=np.where(mp == 'S')
mp[s_co[0][0]][s_co[1][0]]='.'
mpx=mp.copy()

#expand the field in both dimensions (enough to analyze the progression in # of reached tiles)
factor=15 
for i in range(factor-1):
    mpx= np.concatenate((mpx,mp),axis=1)
mp=mpx
for i in range(factor-1):
    mpx= np.concatenate((mpx,mp),axis=0)
mpx[s_co[0][0]*factor+int(factor/2)][s_co[1][0]*factor+int(factor/2)]='o' 
mp=mpx

#store number of reached tiles per step
r=[]
for steps in range(factor*int(ln/2)):
    print('analyzing',steps+1,'of',factor*int(ln/2))
    mp_nxt=mp.copy()
    reached=np.where(mp_nxt == 'o')
    for rng in range(len(reached[0])):
        i=reached[0][rng]
        j=reached[1][rng]
        if i>0 and mp[i-1][j]!='#':
            mp_nxt[i-1][j]='o'
        if i<len(mp)-1 and mp[i+1][j]!='#':
            mp_nxt[i+1][j]='o'
        if j>0 and mp[i][j-1]!='#':
            mp_nxt[i][j-1]='o'
        if j<len(mp[0])-1 and mp[i][j+1]!='#':
            mp_nxt[i][j+1]='o'
        mp_nxt[i][j]='.'
    mp=mp_nxt 
    nw=np.count_nonzero(mp=='o')
    r.append(nw)

#find an arithmethic progression in this sequence.
#the repetition should occur every 'height/width of matrix' steps
#predict next results based on the progression pattern
i=ap=0
steps=26501365
found=False
for stp in range(steps):
    if i<len(r): 
        if i-3*ln>=0 and (r[i]-r[i-ln])-(r[i-ln]-r[i-2*ln])==(r[i-ln]-r[i-2*ln])-(r[i-2*ln]-r[i-3*ln]):
            ap=(r[i]-r[i-ln])-(r[i-ln]-r[i-2*ln])
            found=True
        i+=1
    else:
        if not found:
            break
        r.append(ap+(r[i-ln]-r[i-2*ln])+r[i-ln])
        r.pop(0)
if found:        
    print('Reached after',26501365,'steps:',r[-1])
else:
    print('No arithmetic progression identified - increase field expansion factor')
            