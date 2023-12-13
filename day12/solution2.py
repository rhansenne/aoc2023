from functools import lru_cache
records = [[l.split()[0],list(map(int, l.split()[1].split(',')))] for l in open('input.txt', 'r').readlines()]
for r in records:
    r[0]=4*(r[0]+'?')+r[0]
    r[1]=5*r[1]

def positions(str,group):
    pos=[]
    for i in range(0,len(str)-group+1):
        match=True
        for j in range(0,group):
            if str[i:][j] == '.':
                match=False
                continue
        if len(str[i:])>group and str[i:][group]=='#':
            match=False
        if match:
            pos.append(i)
        if str[i]=='#':
            break
    return pos

@lru_cache(maxsize=None)
def get_matches(str,groups):
    res=0
    for pos in positions(str,groups[0]):
        if len(groups)>1:
            res+=get_matches(str[pos+groups[0]+1:],tuple(groups[1:]))
        elif not '#' in str[pos+groups[0]:]:
            res+=1
    return res
 
print(sum([get_matches(r[0],tuple(r[1])) for r in records]))