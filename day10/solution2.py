from shapely.geometry import Point
from shapely.geometry import Polygon

def tile_to_line(i,j):
    match sketch[i][j]:
        case '-':
            return [(i+0.5,j),(i+0.5,j+1)]
        case '|':
            return [(i,j+0.5),(i+1,j+0.5)]
        case 'L':
            return [(i,j+0.5),(i+0.5,j+1)]
        case 'J':
            return [(i,j+0.5),(i+0.5,j)]
        case '7':
            return [(i+0.5,j),(i+1,j+0.5)]
        case 'F':
            return [(i+0.5,j+1),(i+1,j+0.5)]
        case _: 
            return []

sketch=[[*l.strip()] for l in open('input.txt', 'r').readlines()]
i=j=-1
cur=prv=(-1,-1)
for lnr,l in enumerate(sketch):
    for cnr,c in enumerate(l):
        if c=='S':
            i,j=lnr,cnr
loop=[]  
poly=[]          
while True:
    cur=i,j
    loop.append(cur)
    poly+=tile_to_line(i,j)
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
inside=0
polygon = Polygon(poly)
for i in range(len(sketch)):
    for j in range(len(sketch[0])):
        if (i,j) not in loop:
            if polygon.contains(Point(i,j)):
                inside +=1
print(inside)