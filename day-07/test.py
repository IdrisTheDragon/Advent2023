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
    

from collections import Counter

hands = {
    "JJJJJ":6,
    "JJJJ5":6,
    "JJJ55":6,
    "JJ555":6,
    "J5555":6,
    "1JJJ5":5,
    "1JJ55":5,
    "1J555":5,
    "11555":4,
    "12JJ5":3,
    "12J55":3,
    "11224":2,
    "11234":1,
    "1J234":1,
    "12345":0
}

for hand,expected in hands.items():
    tcards = dict(Counter(hand))

    jcount = tcards.pop('J') if 'J' in tcards else 0

    tcards = [(k, v) for k, v in tcards.items()]
    tcards = sorted(tcards,key=lambda x: x[1])
    tcards.reverse()

    #print(cards,scards,tcards)


    t = hand_rank_p2_helper(tcards,jcount)
    assert int(t) == expected, f"{hand} expected {expected} but got {t}"

