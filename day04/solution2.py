cards=[]
for l in open('input.txt', 'r').readlines():
    numbers = [set(x.strip().split(' ')) for x in l[l.index(':')+1:].split('|')]
    left=set(filter(None, numbers[0]))
    right=set(filter(None, numbers[1]))
    cards.append([left,right])

def get_winning_cards(i):
    won=len(cards[i][0].intersection(cards[i][1]))
    for j in range (i+1, i+won+1):
        won+=get_winning_cards(j)
    return won
        
res=len(cards)
for i in range(len(cards)):
    res+=get_winning_cards(i)
print(res)