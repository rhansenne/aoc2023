from shapely.geometry import Polygon
trench=[l[l.index('#'):l.index(')')] for l in open('input.txt', 'r').readlines()]
i=j=0
coords=[]
for t in trench:
    length = int(t[1:6], 16)
    match t[-1]:
        case '0':
            i+=length
            coords.append((i,j))
        case '2':
            i-=length
            coords.append((i,j))
        case '3':
            j+=length
            coords.append((i,j))
        case '1':
            j-=length
            coords.append((i,j))
polygon=Polygon(coords)
print(polygon.length+polygon.area-(polygon.length-2)/2)