starting_speed = 0
increase_per_milli = 1

print("== P1 ==")
with open("input.txt","r") as infile:
    l = infile.readlines()
    times = l[0].split(":")[1].strip().split()
    distance =  l[1].split(":")[1].strip().split()
    #print(times,distance)
    sum = 1
    for time,distance in zip(times,distance):
        time = int(time)
        distance = int(distance)
        #print(time,distance)
        distances = []
        for t in range(0,time):
            speed = starting_speed + t*increase_per_milli
            travelled_distance = speed*(time-t)
            distances.append(travelled_distance)
        #print(distances)
        winning = [d for d in distances if d > distance]
        #print(winning)
        sum *= len(winning)
    print(sum)

print("== P2 ==")
with open("input.txt","r") as infile:
    l = infile.readlines()
    time = l[0].split(":")[1].strip().replace(" ","")
    distance =  l[1].split(":")[1].strip().replace(" ","")
    #print(time,distance)
    time = int(time)
    distance = int(distance)
    #print(time,distance)
    distances = []
    for t in range(0,time):
        speed = starting_speed + t*increase_per_milli
        travelled_distance = speed*(time-t)
        distances.append(travelled_distance)
    #print(distances)
    winning = [d for d in distances if d > distance]
    print(len(winning))
