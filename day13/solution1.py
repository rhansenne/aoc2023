import numpy as np
patterns=[]
p=[]
for l in open('input.txt', 'r').readlines():
    if len(l)<=1:
        patterns.append(np.array(p))
        p=[]
    else:
        p.append([*l.strip()])
patterns.append(np.array(p))

def reflected(p):
    for i in range(len(p)-1):
        refl=True
        for j in range(0,min(i+1,len(p)-i-1)):
            if not np.array_equal(p[i-j],p[i+j+1]):
                refl=False
                break
        if refl:
            return i+1
    return 0

print(sum([100*reflected(p)+reflected(np.rot90(p,3)) for p in patterns]))