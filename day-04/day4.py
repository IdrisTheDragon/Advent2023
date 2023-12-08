
# P1
with open("input.txt","r") as infile:
    sum = 0
    cards = {}
    for game in infile:
        (round,numbers) = game.split(':')
        round = int(round.split()[1])
        (winning,have) = numbers.split("|")
        winning = winning.strip().split()
        have = have.strip().split()
        #print(winning,have)
        matches = set(winning).intersection(set(have))
        #print(matches)
        if len(matches) > 0:
            # print(len(matches),1*pow(2,len(matches)-1))
            sum += 1*pow(2,len(matches)-1)
        cards[round] = [matches,1]
    print("== P1 ==")
    print(sum)

print("== P2 ==")
total = 0
for round,(matches,count) in cards.items():
    total += count
    #print(round,count)
    for i in range(0,len(matches)):
        cards[round+i+1][1] += count
print(total)
