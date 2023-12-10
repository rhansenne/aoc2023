sketch=[[*l.strip()] for l in open('input.txt', 'r').readlines()]
i=j=-1
cur=prv=(-1,-1)
for lnr,l in enumerate(sketch):
    for cnr,c in enumerate(l):
        if c=='S':
            i,j=lnr,cnr
steps=0            
while True:
    cur=i,j
    if sketch[i][j] in ('S','-','L','F') and j+1<len(sketch[0]) and sketch[i][j+1] in ('S','-','J','7') and (i,j+1)!=prv:
        j+=1
    elif sketch[i][j] in ('S','|','7','F') and i+1<len(sketch) and sketch[i+1][j] in ('S','|','L','J') and (i+1,j)!=prv:
        i+=1
    elif sketch[i][j] in ('S','-','J','7') and j>0 and sketch[i][j-1] in ('S','-','L','F') and (i,j-1)!=prv:
        j-=1
    else:
        i-=1
    if sketch[i][j]=='S':
        break
    prv=cur
    steps+=1
print((steps+1)/2)    