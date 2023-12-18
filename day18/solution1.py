from shapely.geometry import Polygon
trench=[(l[0],int(l.split()[1])) for l in open('input.txt', 'r').readlines()]
i=j=0
coords=[]
for p in trench:
    match p[0]:
        case 'R':
            i+=p[1]
            coords.append((i,j))
        case 'L':
            i-=p[1]
            coords.append((i,j))
        case 'U':
            j+=p[1]
            coords.append((i,j))
        case 'D':
            j-=p[1]
            coords.append((i,j))
polygon=Polygon(coords)
print(polygon.length+polygon.area-(polygon.length-2)/2)