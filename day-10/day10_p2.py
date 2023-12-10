
def find_start(grid):
    for y,row in enumerate(grid):
        for x,v in enumerate(row):
            if v[0] == 'S':
                return (y,x)

def print_grid(grid):
    for row in grid:
        for cel in row:
            print(cel[1] if cel[1] != None else '.',end = '')
        print()

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
def neighbouring_cells(y,x,grid,distance):
    temp_next = []
    for type,dirs in types.items():
        if grid[y][x][0] == type:
            grid[y][x] = (type, distance)

            for (yoff,xoff) in dirs:
                if not (0 <= y+yoff < len(grid) and 0 <= x+xoff < len(grid[y+yoff])):
                    continue
                if grid[y+yoff][x+xoff][0] in offsets[(yoff,xoff)]:
                    temp_next.append((y+yoff,x+xoff))
            return temp_next

grid = []
with open("input.txt","r")as infile:
    for l in infile:
        l = l.strip()
        l = [ (v,None) for v in l ]
        grid.append(l)
#print(grid)
start = find_start(grid)

next = [start]
#print(next)

paths = [[start,cell] for cell in neighbouring_cells(start[0],start[1],grid,0)]
distance = 1
next = True
while next:
    next = False
    for i in range(0,len(paths)):
        #print(paths[i])
        (y,x) = paths[i][-1]
        if not grid[y][x][1] == None:
            continue
        neighbours = neighbouring_cells(y,x,grid,distance)
        next = True
        #print((y,x),neighbours)
        for n in neighbours:
            if n[0] == paths[i][-2][0] and paths[i][-2][1] == n[1]:
                #print("not added",n)
                pass
            else:
                #print("added",n)
                paths[i].append(n)
                break
    distance +=1
# print(grid)
#print_grid(grid)
max = 0
max_cell = None
for p in paths:
    path_end = p[-1]
    path_end_value = grid[path_end[0]][path_end[1]][1]
    if path_end_value > max:
        max = path_end_value
        max_cell = path_end

print(max)
max_paths = []
for p in paths:
    for c in p:
        if c == max_cell:
            max_paths.append(p)
print(len(max_paths))

start_types = {
    ((-1,0),(1,0)): '|',
    ((1,0),(-1,0)): '|',
    ((0,1),(0,-1)): '-',
    ((0,-1),(0,1)): '-',
    ((1,0),(0,1)):'F',
    ((0,1),(1,0)):'F',
    ((-1,0),(0,1)):'L',
    ((0,1),(-1,0)):'L',
    ((-1,0),(0,-1)):'J',
    ((0,-1),(-1,0)):'J',
    ((1,0),(0,-1)):'7',
    ((0,-1),(1,0)):'7',
}

start_type_vkey = (
    (max_paths[0][1][0]-start[0],max_paths[0][1][1]-start[1]),
    (max_paths[1][1][0]-start[0],max_paths[1][1][1]-start[1])
)
start_type = start_types[start_type_vkey]
#print(start_type)
grid[start[0]][start[1]] = (start_type,0)


max_paths[1].reverse()
edge_path = []
edge_path.extend(max_paths[0])
edge_path.extend(max_paths[1][2:-1])
#print(edge_path)
edge_path.reverse()
inside = []
for y,row in enumerate(grid):
    for x,v in enumerate(row):
        if (y,x) in edge_path:
            continue
        right = 0
        dir = None
        edges = []
        for c in edge_path:
            if c[0] == y and c[1] > x:
                cel_t = grid[c[0]][c[1]][0]
                # if (y,x) == (4,4):
                    # print(cel_t,edges,right)
                if cel_t == '|':
                    right+=1
                    edges.append((cel_t,c))
                elif cel_t == 'F':
                    edges.append((cel_t,c))
                    if dir == 'J':
                        right+=1
                        dir = None
                    elif dir == '7':
                        dir = None
                    else:
                        dir = 'F'
                elif cel_t == 'L':
                    edges.append((cel_t,c))
                    if dir == '7':
                        right+=1
                        dir = None
                    elif dir == 'J':
                        dir = None
                    else:
                        dir = 'L'
                elif cel_t == 'J':
                    edges.append((cel_t,c))
                    if dir == 'F':
                        right+=1
                        dir = None
                    elif dir == 'L':
                        dir = None
                    else:
                        dir = 'J'
                elif cel_t == '7':
                    edges.append((cel_t,c))
                    if dir == 'L':
                        right+=1
                        dir = None
                    elif dir == 'F':
                        dir = None
                    else:
                        dir = '7'

        if right > 0 and not right%2 == 0:
            inside.append((y,x))
#print(inside)
print(len(inside))
