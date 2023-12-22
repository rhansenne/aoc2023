workflows=[]
accepted=[]
for l in open('input.txt', 'r').readlines():
    if len(l)<=1:
        break
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
            if comp=='>':
                part_copy=part.copy()
                part_copy[cat]=(max(part[cat][0],val+1),part[cat][1])
                next_wf(target,part_copy)
                part[cat]=(part[cat][0],min(part[cat][1],val))
            elif comp=='<':
                part_copy=part.copy()
                part_copy[cat]=(part[cat][0],min(part[cat][1],val-1))
                next_wf(target,part_copy)
                part[cat]=(max(part[cat][0],val),part[cat][1])
        else:
            next_wf(rule,part)
            
def combs(part):
    comb=1
    for rng in part.values():
        comb*=max(0,rng[1]-rng[0]+1)
    return comb

next_wf("in",dict([(attr,[1,4000]) for attr in {'x','m','a','s'}]))
print(sum([combs(p) for p in accepted]))