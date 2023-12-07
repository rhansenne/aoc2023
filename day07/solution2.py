values=['A','K','Q','T','9','8','7','6','5','4','3','2','J']
hands = [(l[0:l.index(' ')],int(l[l.index(' ')+1:])) for l in open('input.txt', 'r').readlines()]

def pairs(hand):
    p=0
    for c in hand:        
        if hand.count(c)==2:
            p+=1
    return p/2

def of_a_kind(hand,i):
    for c in hand:        
        if hand.count(c)==i:
            return True
    return False

def strength(hand):
    if of_a_kind(hand,5):
        return 1
    elif of_a_kind(hand,4):
        return 2
    elif of_a_kind(hand,3) and of_a_kind(hand,2):
        return 3
    elif of_a_kind(hand,3):
        return 4
    elif pairs(hand)==2:
        return 5
    elif pairs(hand)==1:
        return 6
    else:
        return 7

def strength_j_repl(hand):
    return min([strength(hand.replace('J',v)) for v in values[:-1]])

hands_sorted=sorted(hands, key=lambda hand: [strength_j_repl(hand[0])]+[values.index(c) for c in hand[0]])
print(sum([(len(hands)-i)*hand[1] for i,hand in enumerate(hands_sorted)]))