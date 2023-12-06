from sympy import solveset, S
from sympy.abc import x
time,distance = [int(l[l.index(':')+1:].strip().replace(' ','')) for l in open('input.txt', 'r').readlines()]
s = solveset((x*(time-x))>distance, x,S.Integers)
print(s[-1]-s[0]+1)