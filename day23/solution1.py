mp=[[*l.strip()] for l in open('input.txt', 'r').readlines()]
mx=1
queue=[]
queue.append((1,1,set((0,0))))
while queue:
    m = queue.pop(0) 
    i=m[0]
    j=m[1]
    visited=m[2]
    if (i,j) in visited:
        continue
    visited.add((i,j))
    if i==len(mp)-2 and j==len(mp[0])-2:
        if len(visited)>mx:
            mx=len(visited)
        continue
    if mp[i][j]=='.':
        if i>0 and mp[i-1][j]!='#':
            queue.append((i-1,j,visited.copy()))
        if i<len(mp)-1 and mp[i+1][j]!='#':
            queue.append((i+1,j,visited.copy()))
        if j>0 and mp[i][j-1]!='#':
            queue.append((i,j-1,visited.copy()))
        if j<len(mp[0])-1 and mp[i][j+1]!='#':
            queue.append((i,j+1,visited.copy()))
    elif mp[i][j]=='>' and j<len(mp[0])-1 and mp[i][j+1]!='#':
        queue.append((i,j+1,visited.copy()))
    elif mp[i][j]=='<' and j>0 and mp[i][j-1]!='#':
        queue.append((i,j-1,visited.copy()))
    elif mp[i][j]=='v' and i<len(mp)-1 and mp[i+1][j]!='#':
        queue.append((i+1,j,visited.copy()))
    elif mp[i][j]=='^' and i>0 and mp[i-1][j]!='#':
        queue.append((i-1,j,visited.copy()))   
print(mx)