def extrapolate(h):
    if sum(h)==0:
        return 0
    return h[-1]+extrapolate([y-x for x,y in zip(h,h[1:])])

hist=[[int(d) for d in l.split(' ')] for l in open('input.txt', 'r').readlines()]
print(sum([extrapolate(h) for h in hist]))