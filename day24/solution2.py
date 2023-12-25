from sympy import solve, Symbol

hail=[]
for l in open('input.txt', 'r').readlines():
    pos=[int(c) for c in l[:l.index('@')].split(',')]
    vel=[int(c) for c in l.strip()[l.index('@')+1:].split(',')]
    hail.append([pos,vel])

def co_after_n_ns(hail,n):
    return tuple(map(lambda x,y:x+n*y ,hail[0],hail[1]))

# build and solve equations to find the times when the first 3 hailstones are hit 
t0 = Symbol('t0')
t1 = Symbol('t1')
t2 = Symbol('t2')
equations=[]
for i in range(3): # for each axis
    co0=hail[0][0][i]+hail[0][1][i]*t0 #co of hail 0 at time t0
    co1=hail[1][0][i]+hail[1][1][i]*t1 #co of hail 1 at time t1
    co2=hail[2][0][i]+hail[2][1][i]*t2 #co of hail 2 at time t2
    e=co2-co1-(co1-co0)*(t2-t1)/(t1-t0) # these points should be colinear 
    equations.append(e)
s=solve(equations,[t0,t1,t2])
t0,t1,t2=s[0]

# retrace to the point at time 0 on the throw trajectory line
p1=co_after_n_ns(hail[0],t0)
p2=co_after_n_ns(hail[1],t1)
throw_co=tuple(map(lambda x,y:x-(y-x)*t0/(t1-t0),p1,p2))
print(sum(throw_co))