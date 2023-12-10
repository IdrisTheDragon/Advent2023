
def find_start(grid):
    for y,row in enumerate(grid):
        for x,v in enumerate(row):
            if v[0] == 'S':
                print('start')
                return (y,x)

def print_grid(grid):
    for row in grid:
        for cel in row:
            print(cel[1] if cel[1] != None else '.',end = '')
        print()

grid = []
with open("example2.txt","r")as infile:
    for l in infile:
        l = l.strip()
        l = [ (v,None) for v in l ]
        grid.append(l)
#print(grid)
start = find_start(grid)
distance = 0
next = [start]
#print(next)
offsets = {
    (-1,0): ['|','F','7'],
    (1,0): ['|','J','L'],
    (0,1): ['-','J','7'],
    (0,-1): ['-','L','F']
}
types = {
    'S' : [(-1,0),(1,0),(0,1),(0,-1)],
    '|' : [(-1,0),(1,0)],
    '-' : [(0,1),(0,-1)],
    'J' : [(-1,0),(0,-1)],
    'F' : [(1,0),(0,1)],
    'L' : [(-1,0),(0,1)],
    '7' : [(1,0),(0,-1)]
}
while next:
    temp_next = []
    for (y,x) in next:
        if not (0 <= y < len(grid) and 0 <= x < len(grid[y])):
            continue
        if not grid[y][x][1] == None:
            continue

        for type,dirs in types.items():
            if grid[y][x][0] == type:
                grid[y][x] = (type, distance)

                for (yoff,xoff) in dirs:
                    if not (0 <= y+yoff < len(grid) and 0 <= x+xoff < len(grid[y+yoff])):
                        continue
                    if grid[y+yoff][x+xoff][0] in offsets[(yoff,xoff)]:
                        temp_next.append((y+yoff,x+xoff))
                break
    next = temp_next
    distance +=1
# print(grid)
print_grid(grid)
max = 0
for row in grid:
    for cel in row:
        if cel[1] and cel[1] > max:
            max = cel[1]
print(max)
