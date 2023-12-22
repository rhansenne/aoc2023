from enum import Enum
import math

class Dir(Enum):
    N=1
    E=2
    S=3
    W=4
    
grid=[[int(d) for d in l.strip()] for l in open('input.txt', 'r').readlines()]
minheat=math.inf
minheats={}

def next(i,j,dir,samedir,heat):
    global minheat
    heat+=grid[i][j]
    if heat>=minheat:
        return    
    if (i,j) in minheats:
        if heat<=minheats[(i,j)]:
            minheats[(i,j)]=heat
        else:
            return
    else:
        minheats[(i,j)]=heat
    if i==len(grid)-1 and j==len(grid[0])-1:
        minheat=heat
        return
    match dir:
        case Dir.E:
            if samedir<3 and j<len(grid[0])-1:
                next(i,j+1,Dir.E,samedir+1,heat)
            if i<len(grid)-1:
                next(i+1,j,Dir.S,1,heat)                
            if i>0:
                next(i-1,j,Dir.N,1,heat)                                
        case Dir.S:
            if samedir<3 and i<len(grid)-1:
                next(i+1,j,Dir.S,samedir+1,heat)
            if j<len(grid[0])-1:
                next(i,j+1,Dir.E,1,heat)                
            if j>0:
                next(i,j-1,Dir.W,1,heat)                                                
        case Dir.W:
            if samedir<3 and j>0:
                next(i,j-1,Dir.W,samedir+1,heat)
            if i<len(grid)-1:
                next(i+1,j,Dir.S,1,heat)                
            if i>0:
                next(i-1,j,Dir.N,1,heat)                                
        case Dir.N:
            if samedir<3 and i>0:
                next(i-1,j,Dir.N,samedir+1,heat)
            if j<len(grid[0])-1:
                next(i,j+1,Dir.E,1,heat)                
            if j>0:
                next(i,j-1,Dir.W,1,heat)                  
                
next(0,0,Dir.E,0,-grid[0][0])
print(minheat) 