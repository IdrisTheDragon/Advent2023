order = {"A":"m", "K":"l", "Q":"k", "J":"j", "T":"i", "9":"h", "8":"g", "7":"f", "6":"e", "5":"d", "4":"c", "3":"b", "2":"a"}

from collections import Counter

def card_rank(card):
    return order[card]

def hand_rank(hand):
    scards = sorted(hand,key=lambda x:card_rank(x), reverse=True)
    tcards = Counter(scards)
    #print(cards,scards,tcards)
    if max(tcards.values()) == 5:
        t="6"
    elif max(tcards.values()) == 4:
        t="5"
    elif max(tcards.values()) == 3:
        t= "4" if len(tcards) == 2 else "3"
    elif max(tcards.values()) == 2: 
        t = "2" if Counter(tcards.values())[2] == 2 else "1"
    else:
        t="0"
    # String with each char being a score, where each char in turn is used for resolving tie breaks.
    rank = t + ''.join([str(order[c]) for c in hand])
    #print(hand,rank)
    return rank

with open("input.txt","r") as infile:
    cards = []
    for l in infile:
        (hand,bet) = l.strip().split()
        cards.append((hand,bet))

    scards = sorted(cards,key =lambda x: hand_rank(x[0]))
    #print(scards)
    sum = 0
    for count, (hand,bet) in enumerate(scards):
        sum += (count+1)*int(bet)
    print("==P1==")
    print(sum)

order = {"A":"m", "K":"l", "Q":"k", "T":"j", "9":"i", "8":"h", "7":"g", "6":"f", "5":"e", "4":"d", "3":"c", "2":"b", "J":"a",}

def hand_rank_p2_helper(tcards,jcount):
    #print(tcards,jcount)
    # Five of a kind
    if jcount >= 4 or (jcount == 3 and tcards[0][1] == 2) or (jcount == 2 and tcards[0][1] == 3) or (jcount == 1 and tcards[0][1] == 4) or tcards[0][1] == 5:
        return "6"
    # 4 of a kind
    elif jcount == 3 or (jcount == 2 and tcards[0][1] == 2) or (jcount == 1 and tcards[0][1] == 3) or tcards[0][1] == 4:
        return "5"
    # Full house
    elif (tcards[0][1] == 3 and tcards[1][1] == 2) or (jcount == 1 and tcards[0][1] == 2 and tcards[1][1] == 2):
        return "4"
    # three of a kind
    elif tcards[0][1] == 3 or (jcount == 1 and tcards[0][1] == 2) or (jcount == 2 and tcards[0][1] == 1):
        return "3"
    # two pair
    elif (tcards[0][1] == 2 and tcards[1][1] == 2):
        return "2"
    # one pair
    elif tcards[0][1] == 2 or (jcount ==1 and tcards[0][1] == 1):
        return "1"
    else:
        return "0"

def hand_rank_p2(hand):
    tcards = dict(Counter(hand))
    
    jcount = tcards.pop('J') if 'J' in tcards else 0

    # sort cards counts based on count
    tcards = [(k, v) for k, v in tcards.items()]
    tcards = sorted(tcards,key=lambda x: x[1])
    tcards.reverse()

    #print(cards,scards,tcards)
    t = hand_rank_p2_helper(tcards,jcount)
    rank = t + ''.join([str(order[c]) for c in hand])
    #print(hand,rank)
    return rank

with open("input.txt","r") as infile:
    cards = []
    for l in infile:
        (hand,bet) = l.strip().split()
        cards.append((hand,bet))

    scards = sorted(cards,key =lambda x: hand_rank_p2(x[0]))
    #print(scards)
    sum = 0
    for count, (hand,bet) in enumerate(scards):
        sum += (count+1)*int(bet)
    print("==P2==")
    print(sum)
