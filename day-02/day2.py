

# P1
bag = { "red":12,"green": 13,"blue":14}

with open("input.txt","r") as infile:
    sum = 0
    for l in infile:
        (g,rs) = l.split(":")
        g = int(g.split(" ")[1])
        #print(g)
        possible = True
        rs = rs.split(";")
        for r in rs:
            cs = r.split(",")
            for c in cs:
                c = c.strip()
                #print(c)
                (v,c) = c.split()
                if int(v) > bag[c]:
                    possible = False
        if possible:
            sum += g;
    print("== P1 ==")
    print(sum)


# P2

with open("input.txt","r") as infile:
    sum = 0
    for l in infile:
        (g,rs) = l.split(":")
        g = int(g.split(" ")[1])
        #print(g)
        bag = { "red":0,"green": 0,"blue":0}
        rs = rs.split(";")
        for r in rs:
            cs = r.split(",")
            for c in cs:
                c = c.strip()
                #print(c)
                (v,c) = c.split()
                if int(v) > bag[c]:
                    bag[c] = int(v)
        power = bag["red"] * bag["green"] * bag["blue"]
        sum+=power
    print("== P2 ==")
    print(sum)
