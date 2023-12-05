almanac = open('input.txt', 'r').readlines()
seeds = [int(s) for s in almanac[0][7:].split(' ')]
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append((seeds[i],seeds[i+1]))  
unmapped = ranges.copy()
remapped = []
for a in almanac:
    if len(a)>1 and not ':' in a:
        m = [int(c) for c in a.strip().split(' ')]
        for i,r in enumerate(ranges):
            unmapped.remove(r)
            unmapped.append((min(r[0],m[1]),min(r[1],m[1]-r[0])))
            remapped.append((max(r[0],m[1])+m[0]-m[1],min(m[1]+m[2]-max(r[0],m[1]),r[0]+r[1]-max(r[0],m[1]))))
            unmapped.append((max(r[0],m[1]+m[2]),min(r[1],r[1]-m[1]-m[2]+r[0])))
        unmapped = list(filter(lambda x: x[1]>0, unmapped)) 
        remapped = list(filter(lambda x: x[1]>0, remapped))
        ranges = unmapped.copy()
    else:
        ranges = unmapped + remapped
        unmapped = ranges.copy()
        remapped = []
print(min([r[0] for r in ranges]))