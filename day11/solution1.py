import copy, itertools as it, numpy as np
image = np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])
coords=[]
exp=0
for i,row in enumerate(image):
    if np.all(row=='.'):
        exp+=1
    for j,c in enumerate(row):
        if c=='#':
            coords.append([i+exp,j])
coords_exp=copy.deepcopy(coords)
for j,col in enumerate(image.T):
    if np.all(col=='.'):   
        for c,co in enumerate(coords):
            if co[1]>j:
                coords_exp[c][1]+=1
total=sum([abs(g1[0]-g2[0])+abs(g1[1]-g2[1]) for g1,g2 in it.combinations(coords_exp,2)])
print(total)