
def iszeros(h):
    return all(n == 0 for n in h)


with open("input.txt", "r") as infile:
    sum_p1 = 0
    sum_p2 = 0
    for l in infile:
        nums = [int(n) for n in l.strip().split()]
        history = [nums]
        #print(history)
        while not iszeros(history[-1]):
            next_history = []
            for i in range(1,len(history[-1])):
                next_history.append(history[-1][i]-history[-1][i-1])
            history.append(next_history)
        for i in range(len(history)-1,0,-1):
            history[i-1].append(history[i-1][-1] + history[i][-1])
        for i in range(len(history)-1,0,-1):
            history[i-1].insert(0,(history[i-1][0] - history[i][0]))
        # print(history)
        # print(history[0][-1],history[0][0])
        sum_p1 += history[0][-1]
        sum_p2 += history[0][0]
    print(sum_p1,sum_p2)
