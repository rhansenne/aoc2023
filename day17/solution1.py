from dijkstar import Graph, find_path
from enum import Enum

class Dir(Enum):
    N=1
    E=2
    S=3
    W=4

grid = [[int(num) for num in line.strip()] for line in open('input.txt', 'r').readlines()]
height=len(grid)
width=len(grid[0])
G = Graph()
for i,r in enumerate(grid):
    for j,c in enumerate(r):
        for e in range(1,3):
            if j<width-1:
                G.add_edge((i,j,Dir.E,e),(i,j+1,Dir.E,e+1),grid[i][j+1])
        for e in range(1,4):
            if i<height-1:
                G.add_edge((i,j,Dir.E,e),(i+1,j,Dir.S,1),grid[i+1][j])
            if i>0:
                G.add_edge((i,j,Dir.E,e),(i-1,j,Dir.N,1),grid[i-1][j])
        for s in range(1,3):
            if i<height-1:
                G.add_edge((i,j,Dir.S,s),(i+1,j,Dir.S,s+1),grid[i+1][j])
        for s in range(1,4):
            if j<width-1:
                G.add_edge((i,j,Dir.S,s),(i,j+1,Dir.E,1),grid[i][j+1])
            if j>0:
                G.add_edge((i,j,Dir.S,s),(i,j-1,Dir.W,1),grid[i][j-1])
        for w in range(1,3):
            if j>0:
                G.add_edge((i,j,Dir.W,w),(i,j-1,Dir.W,w+1),grid[i][j-1])
        for w in range(1,4):
            if i<height-1:
                G.add_edge((i,j,Dir.W,w),(i+1,j,Dir.S,1),grid[i+1][j])
            if i>0:
                G.add_edge((i,j,Dir.W,w),(i-1,j,Dir.N,1),grid[i-1][j])
        for n in range(1,3):
            if i>0:
                G.add_edge((i,j,Dir.N,n),(i-1,j,Dir.N,n+1),grid[i-1][j])
        for n in range(1,4):
            if j<width-1:
                G.add_edge((i,j,Dir.N,n),(i,j+1,Dir.E,1),grid[i][j+1])
            if j>0:
                G.add_edge((i,j,Dir.N,n),(i,j-1,Dir.W,1),grid[i][j-1])

res=set()
for i in range(1,3):
    res.add(grid[0][1]+find_path(G, (0,1,Dir.E,1), (height-1,width-1,Dir.S,i)).total_cost)
    res.add(grid[0][1]+find_path(G, (0,1,Dir.E,1), (height-1,width-1,Dir.E,i)).total_cost)
    res.add(grid[1][0]+find_path(G, (1,0,Dir.S,1), (height-1,width-1,Dir.S,i)).total_cost)
    res.add(grid[1][0]+find_path(G, (1,0,Dir.S,1), (height-1,width-1,Dir.E,i)).total_cost)
print(min(res))