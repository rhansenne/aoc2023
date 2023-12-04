res=0
for l in open('input.txt', 'r').readlines():
    numbers = [set(x.strip().split(' ')) for x in l[l.index(':')+1:].split('|')]
    left=set(filter(None, numbers[0]))
    right=set(filter(None, numbers[1]))
    winning=len(left.intersection(right))
    if winning>0:
        res+=pow(2,winning-1)
print(res)