import itertools
records = [(l.split()[0],list(map(int, l.split()[1].split(',')))) for l in open('input.txt', 'r').readlines()]

def matches(str,pattern):
    for i,c in enumerate(pattern):
        if c!='?' and c!=str[i]:
            return False
    return True

arr=0
for rec in records:
    #max free floating dots in addition to mandatory separator dots between each groups
    max_extra=len(rec[0])-sum(rec[1])-len(rec[1])+1
    #possible permutations of number of free floating dots between groups
    perms = [p for p in itertools.product(range(max_extra+1),repeat=len(rec[1])+1) if sum(p)==max_extra]
    for p in perms:
        str=''
        for i,c in enumerate(p[:-1]):
            if i>0:
                str+='.' #mandatory separator dot
            str+=c*'.'+rec[1][i]*'#'
        str+=p[-1]*'.'
        if matches(str,rec[0]):
            arr+=1
print(arr)