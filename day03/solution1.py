import itertools
s = [[*l.strip()] for l in open('input.txt', 'r').readlines()]

def issymbol(i,j):
    if i<0 or i>=len(s) or j<0 or j>=len(s[0]) or s[i][j]=='.' or s[i][j].isdigit():
        return False
    return True

res=0
for i,row in enumerate(s):
    j=0
    while j<len(row):
        num=0
        adj_symbol=False
        while j<len(row) and row[j].isdigit():
            num=10*num+int(row[j])
            for offset in itertools.product((0,-1,1), repeat=2):
                if issymbol(i+offset[0],j+offset[1]):
                    adj_symbol=True
            j+=1
        if adj_symbol:
            res+=num
        j+=1    
print(res)    