import numpy as np
mp=np.array([[*l.strip()] for l in open('input.txt', 'r').readlines()])
for steps in range(64):
    mp_nxt=mp.copy()
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if mp[i][j] in ('o','S'):
                if i>0 and mp[i-1][j]!='#':
                    mp_nxt[i-1][j]='o'
                if i<len(mp)-1 and mp[i+1][j]!='#':
                    mp_nxt[i+1][j]='o'
                if j>0 and mp[i][j-1]!='#':
                    mp_nxt[i][j-1]='o'
                if j<len(mp[0])-1 and mp[i][j+1]!='#':
                    mp_nxt[i][j+1]='o'
                mp_nxt[i][j]='.'
    mp=mp_nxt    
print(np.count_nonzero(mp=='o'))