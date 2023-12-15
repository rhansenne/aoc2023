def hash(s):
    v=0
    for c in s:
        v=((v+ord(c))*17)%256
    return v

print(sum([hash(s) for s in open('input.txt', 'r').readline().split(',')]))