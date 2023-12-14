rocks=[[*l.strip()] for l in open('input.txt', 'r').readlines()]
tot=0
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
            tot+=len(rocks)-newpos
print(tot)