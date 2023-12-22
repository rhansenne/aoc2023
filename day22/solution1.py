bricks=[]
for l in open('input.txt', 'r').readlines():
    co1=[int(c) for c in l[:l.index('~')].split(',')]
    co2=[int(c) for c in l.strip()[l.index('~')+1:].split(',')]
    bricks.append([co1,co2])

def overlap(a,b):
    return not (a[1][0] < b[0][0]
                or a[0][0] > b[1][0]
                or a[1][1] < b[0][1]
                or a[0][1] > b[1][1])
    
    return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]

#sort by lowest bottom Z
bricks=sorted(bricks, key=lambda b: min(b[0][2],b[1][2]))
#ranges of squares occupied by tops of dropped bricks
occupied=dict()
sole_supports=set()
maxz=max(max(b[0][2],b[1][2]) for b in bricks)
for z in range(maxz):
    occupied[z]=set()
for b in bricks:
    #drop brick as far down as possible
    bottom=min(b[0][2],b[1][2])
    for z in reversed(range(1,bottom)):
        overl=False
        supports=[]
        for sq in occupied[z]:
            if overlap(sq,(b[0],b[1])):
                overl=True
                supports.append(sq)
        if not overl:
            b[0][2]-=1
            b[1][2]-=1
        else:
            if len(supports)==1:
                sole_supports.add(supports[0])
            break        
    #update occupied coordinates
    top=max(b[0][2],b[1][2])
    occupied[top].add((tuple(b[0]),tuple(b[1])))
print(len(bricks)-len(sole_supports))