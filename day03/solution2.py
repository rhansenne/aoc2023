import itertools
s = [[*l.strip()] for l in open('input.txt', 'r').readlines()]

def isgear(i,j):
    if i<0 or i>=len(s) or j<0 or j>=len(s[0]) or s[i][j]!='*':
        return False
    return True

gears={}
for i,row in enumerate(s):
    j=0
    while j<len(row):
        num=0
        adj_gear=None
        while j<len(row) and row[j].isdigit():
            num=10*num+int(row[j])
            for offset in itertools.product((0,-1,1), repeat=2):
                if isgear(i+offset[0],j+offset[1]):
                    adj_gear=(i+offset[0],j+offset[1])
            j+=1
        if adj_gear is not None:
            if adj_gear in gears:
                gears[adj_gear].append(num)
            else:
                gears[adj_gear]=[num]
        j+=1
        
res=0
for nums in gears.values():
    if len(nums)==2:
        res+=nums[0]*nums[1]
print(res)    