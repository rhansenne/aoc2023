import re
print(sum([10 * int(re.findall(r'\d', l)[0]) + int(re.findall(r'\d', l)[-1]) for l in open('input.txt', 'r').readlines()]))