workflows=[]
parts=[]
accepted=[]
empty_line_reached=False
for l in open('input.txt', 'r').readlines():
    if len(l)<=1:
        empty_line_reached=True 
        continue
    if empty_line_reached:
        part={}
        for cat in l[1:l.index('}')].split(','):
            part[cat[0]]=int(cat[2:])
        parts.append(part)
    else:
        workflows.append((l[:l.index('{')],l[l.index('{')+1:l.index('}')].split(',')))

def next_wf(wf_name,part):
    if len(wf_name)>1:
        for wf in workflows:
            if wf[0]==wf_name:
                exec_workflow(wf,part)
    elif wf_name=='A':
        accepted.append(part)
    return

def exec_workflow(workflow,part):
    for rule in workflow[1]:
        if ':' in rule:
            cat=rule[0]
            comp=rule[1]
            val=int(rule[2:rule.index(':')])
            target=rule[rule.index(':')+1:]
            if comp=='>' and part[cat]>val:
                next_wf(target,part)
                return
            elif comp=='<' and part[cat]<val:
                next_wf(target,part)
                return
        else:
            next_wf(rule,part)
            
for part in parts:
    next_wf("in",part)
print(sum([sum(part.values()) for part in accepted]))