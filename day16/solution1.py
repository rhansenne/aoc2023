import sys
sys.setrecursionlimit(10000)

layout=[[*l.strip()] for l in open('input.txt', 'r').readlines()]
energized={}

def energize_next(i,j,NS,EW):
    if i<0 or i>=len(layout) or j<0 or j>=len(layout[0]):
        return
    if (i,j) in energized:
        if (NS,EW) in energized[(i,j)]:
            return #avoid endless loop
        energized[(i,j)].append((NS,EW))
    else:
        energized[(i,j)]=[(NS,EW)]
    match layout[i][j]:
        case '.':
            energize_next(i+NS,j+EW,NS,EW)
        case '\\':
            if NS==1:
                energize_next(i,j+1,0,1)
            elif NS==-1:
                energize_next(i,j-1,0,-1)
            elif EW==1:
                energize_next(i+1,j,1,0)
            else:
                energize_next(i-1,j,-1,0)
        case '/':
            if NS==1:
                energize_next(i,j-1,0,-1)
            elif NS==-1:
                energize_next(i,j+1,0,1)
            elif EW==1:
                energize_next(i-1,j,-1,0)
            else:
                energize_next(i+1,j,1,0)
        case '-':
            if NS!=0:
                energize_next(i,j-1,0,-1)
                energize_next(i,j+1,0,1)
            else:
                energize_next(i+NS,j+EW,NS,EW)
        case '|':
            if EW!=0:
                energize_next(i-1,j,-1,0)
                energize_next(i+1,j,1,0)
            else:
                energize_next(i+NS,j+EW,NS,EW)

energize_next(0,0,0,1)        
print(len(energized))