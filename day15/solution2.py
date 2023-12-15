def hash(s):
    v=0
    for c in s:
        v=((v+ord(c))*17)%256
    return v

lens_focus={}
boxes={}
for i in range(256):
    boxes[i]=[]
for step in open('input.txt', 'r').readline().split(','):
    if '=' in step:
        label=step.split('=')[0]
        box=boxes[hash(label)]
        if not label in box:
            box.append(label)
        lens_focus[label]=int(step.split('=')[1])
    else:
        label=step.split('-')[0]
        box=boxes[hash(label)]
        if label in box:
            box.remove(label)
focus_power=0
for box,lenses in boxes.items():
    for i,lens in enumerate(lenses):
        focus_power+=(box+1)*(i+1)*lens_focus[lens]
print(focus_power)