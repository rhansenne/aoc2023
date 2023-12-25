from shapely.geometry import LineString

hail=[]
for l in open('input.txt', 'r').readlines():
    pos=[int(c) for c in l[:l.index('@')].split(',')]
    vel=[int(c) for c in l.strip()[l.index('@')+1:].split(',')]
    hail.append([pos,vel])

mn=200000000000000
mx=400000000000000

def hail_to_line(h):
    co1=h[0][:2]
    co2=[h[0][0]+h[1][0]*mx,h[0][1]+h[1][1]*mx]
    return LineString([co1,co2])

cnt=0
for i in range(len(hail)):
    for j in range(i+1,len(hail)):
        h1=hail_to_line(hail[i])
        h2=hail_to_line(hail[j])
        p = h1.intersection(h2)
        if not p.is_empty and mn<=p.x<=mx and mn<=p.y<=mx:
            cnt+=1
print(cnt)