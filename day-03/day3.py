

def identify_neighbours(grid,rid,cid,cell):
    symbols = []
    cells = [(rid,cid)]
    firstneighbours = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    restneighbours = [(1,1),(0,1),(-1,1)]
    first =True
    while len(cells) > 0:
        (rid,cid) = cells.pop(0)
        if first:
            neighbours = firstneighbours
            first = False
        else:
            neighbours = restneighbours

        for (nrid,ncid) in neighbours:
            newrid = rid+nrid
            newcid = cid+ncid
            if not 0 <= newrid < len(grid) or not 0 <= newcid < len(grid[0]):
                continue
            
            if grid[newrid][newcid].isdigit() and nrid == 0 and ncid == 1:
                cell += grid[newrid][newcid]
                cells.append((newrid,newcid))
            elif not grid[newrid][newcid].isdigit() and not grid[newrid][newcid] == '.':
                symbols.append((newrid,newcid,(grid[newrid][newcid])))
    #print(cell,symbols)

    return (int(cell),symbols)



with open("input.txt","r") as infile:
    grid = []
    for l in infile:
        l=l.strip()
        grid.append([*l])
#print(grid)

print("== P1 ==")
found =False
sum = 0
numbers = []
for rid,row in enumerate(grid):
    for cid,cell in enumerate(row):
        if cell.isdigit() and not found:
            (number,symbols) = identify_neighbours(grid,rid,cid,cell)
            if len(symbols) > 0:
                sum += number
                numbers.append((number,symbols))
            found = True
        elif not cell.isdigit() and found:
            found = False
print(sum)
            
print("== P2 ==")
potentialgears = {}

for (number,symbols) in numbers:
    for (rid,cid,symbol) in symbols:
        if symbol == '*':
            if not (rid,cid) in potentialgears:
                potentialgears[(rid,cid)] = []
            potentialgears[(rid,cid)].append(number)
#print(potentialgears)
sum=0
for k,v in potentialgears.items():
    if len(v) == 2:
        sum+=v[0]*v[1]
print(sum)
