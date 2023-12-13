def print_grid(grid):
    for row in grid:
        for c in row:
            print(c,end='')
        print()

def find_reflection(l,r,grid):
    (match,change) = match_rows(grid[l],grid[r])
    # print(l,grid[l])
    # print(r,grid[r])
    # print(match,change)
    while l >= 0 and r < len(grid) and match:
        if l == 0 or r == len(grid)-1:
            #print("reflection",i+1)
            if part1:
                # print()
                return True
            else:
                # print()
                return change
        l-=1
        r+=1
        (match,new_change) = match_rows(grid[l],grid[r])
        # print(l,grid[l])
        # print(r,grid[r])
        # print(match,new_change,change)
        if change and new_change:
            # only one change allowed
            # print()
            return False
        else:
            # if previous or new have changed, store it for next round
            change = change or new_change
    #print(l,r)
    # print()
    return False

def match_rows(r1,r2):
    # returns whether rows match and if a change was made to get them to match.
    if part1:
        return (r1 == r2,False)
    if r1 == r2:
        # No change made
        return (True,False)
    # Need to make a signle change to match
    for i in range(0,len(r1)):
        tr1 = list(r1)
        tr1[i] = '.' if tr1[i] == '#' else '#'
        tr1 = ''.join(tr1)
        if tr1 == r2:
            return (True,True)
    for i in range(0,len(r2)):
        tr2 = list(r2)
        tr2[i] = '.' if tr2[i] == '#' else '#'
        tr2 = ''.join(tr2)
        if r1 == tr2:
            return (True,True)
    return (False,False)

def rotate_90(grid):
    temp_grid = [[] for _ in range(0,len(grid[0]))]
    for row in grid:
        for i,c in enumerate(row):
            #print(len(temp_grid),i)
            temp_grid[i].append(c)
    temp_grid = [''.join(row) for row in temp_grid]
    return temp_grid

with open("input.txt","r") as infile:
    grids = []
    cur_grid = []
    for l in infile:
        #print(l)
        if l == '\n':
            grids.append(cur_grid)
            cur_grid = []
        else:
            cur_grid.append(l.strip())
    grids.append(cur_grid)
#print(grids)

part1 = True
sum = 0
for grid in grids:
    reflection = None
    for i in range(0,len(grid)-1):
        if find_reflection(i,i+1,grid):
            reflection = (i+1)*100
            print("reflection v",reflection)
            break
    if not reflection:
        rgrid = rotate_90(grid)
        for i in range(0,len(rgrid)-1):
            if find_reflection(i,i+1,rgrid):
                reflection = i+1
                print("reflection h",reflection)
                break
    if not reflection:
        print("uhoh we have a problem")
        print_grid(grid)
    else:
        sum += reflection
print("== P1 ==")
print(sum)


part1 = False
sum = 0
for grid in grids:
    reflection = None
    for i in range(0,len(grid)-1):
        if find_reflection(i,i+1,grid):
            reflection = (i+1)*100
            print("reflection v",reflection)
            break
    if not reflection:
        rgrid = rotate_90(grid)
        for i in range(0,len(rgrid)-1):
            if find_reflection(i,i+1,rgrid):
                reflection = i+1
                print("reflection h",reflection)
                break
    if not reflection:
        print("uhoh we have a problem")
        print_grid(grid)
        print("")
        print_grid(rgrid)
    else:
        sum += reflection
print("== P2 ==")
print(sum)
