import numpy as np
rocks=np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])

def roll_north(rocks):
    for i in range(len(rocks)):
        for j,r in enumerate(rocks[i]):
            if r=='O':
                newpos=i
                for k in reversed(range(0,i)):
                    if rocks[k][j]=='.':
                        newpos=k
                    else:
                        break
                rocks[i][j]='.'
                rocks[newpos][j]='O'

def calc_load(rocks):
    tot=0
    for i in range(len(rocks)):
        for j,r in enumerate(rocks[i]):
            if r=='O':
                tot+=len(rocks)-i
    return tot

def calc_cycle(rocks):
    for i in range(4):
        roll_north(rocks)
        rocks=np.rot90(rocks,3)
    return calc_load(rocks)

def get_sequence(lds):
    for i in range(1, len(lds)):
        if all(lds[j]==lds[j%i] for j in range(i,len(lds))):
            return lds[:i]
    return lds
    
loads=[]
for i in range(len(rocks)*10):
    loads.append(calc_cycle(rocks))

#ignore initial cycles (stabilization period) and then find repeating sequence
stabilization_cycles=len(rocks)
seq=get_sequence(loads[stabilization_cycles:])
print(seq[(1000000000-stabilization_cycles-1)%len(seq)])