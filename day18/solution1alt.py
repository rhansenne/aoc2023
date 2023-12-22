#version without Shapely (polygon area and perimeter calculation inline)
from math import sqrt

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

def area(xy):
    x_list,y_list=[e[0] for e in xy],[e[1] for e in xy]
    a1,a2=0,0
    x_list.append(x_list[0])
    y_list.append(y_list[0])
    for j in range(len(x_list)-1):
        a1 += x_list[j]*y_list[j+1]
        a2 += y_list[j]*x_list[j+1]
    l=abs(a1-a2)/2
    return l

def perimeter(points):
    firstx,firsty = points[0]
    prevx,prevy = firstx, firsty
    res = 0
    for i in range(1, len(points)):
        nextx,nexty = points[i]
        res = res + sqrt((prevx-nextx)*(prevx-nextx)+(prevy-nexty)*(prevy-nexty))
        prevx = nextx
        prevy = nexty
    res = res + sqrt((prevx-firstx)*(prevx-firstx)+(prevy-firsty)*(prevy-firsty))
    return res

area=area(coords)
perim=perimeter(coords)
print(perim+area-(perim-2)/2)