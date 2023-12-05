almanac = open('input.txt', 'r').readlines()
seeds = [int(s) for s in almanac[0][7:].split(' ')]
conv = seeds.copy()
for a in almanac:
    if len(a)>1 and not ':' in a:
        mapping = [int(c) for c in a.strip().split(' ')]
        for i,s in enumerate(seeds):
            if s >= mapping[1] and s < (mapping[1]+mapping[2]):
                conv[i] =  mapping[0] + s - mapping[1]
    else:
        seeds = conv.copy()
print(min(conv))        