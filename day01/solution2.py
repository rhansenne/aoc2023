import re
repl = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', \
        '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
keys='|'.join(repl.keys())
regex = re.compile(keys)
regexrev = re.compile(keys[::-1])
res=0
for l in open('input.txt', 'r').readlines():
    l = regex.sub(lambda m: repl[m.group()], l, 1)
    l = regexrev.sub(lambda m: repl[m.group()[::-1]], l[::-1], 1)
    l=l[::-1]
    res += 10 * int(re.findall(r'\d', l)[0]) + int(re.findall(r'\d', l)[-1])
print(res)