
def print_grid(grid):
    for row in grid:
        for c in row:
            print(c,end='')
        print()

with open("input.txt","r") as infile:
    grid = []
    grid0 = []
    expanded_rows = []
    for i,l in enumerate(infile):
        l = l.strip()
        # expand row
        if len(set(l)) == 1:
            expanded_rows.append(i)
            #print("expand dim1")
            #grid.append(l)
        grid.append(l)
        grid0.append(l)

#print_grid(grid0)
#print()
#print_grid(grid)


# rotate by 90
grid2 = [[] for i in range(0,len(grid))]
for row in grid:
    for i,c in enumerate(row):
        grid2[i].append(c)
#print()
#print_grid(grid2)
grid3 = []
# expand row
expanded_cols = []
for i,row in enumerate(grid2):
    if len(set(row)) == 1:
        #print("expand dim2")
        expanded_cols.append(i)
        #grid3.append(row)
    grid3.append(row)

#print()
#print_grid(grid3)
#print()

# rotate by 90
grid4 = [[] for i in range(0,len(grid))]
for row in grid3:
    for i,c in enumerate(row):
        grid4[i].append(c)

print(len(grid0),len(grid),len(grid2[0]),len(grid3[0]))
print(len(grid0[0]),len(grid[0]),len(grid2),len(grid3))

coords = []

for y,row in enumerate(grid4):
    for x,cel in enumerate(row):
        if cel == '#':
            coords.append((y,x))
sum_p1 = 0
sum_p2 = 0
for i,c1 in enumerate(coords):
    for j,c2 in enumerate(coords[i:]):
        yexpansion = [1 for v in expanded_rows if  min(c1[0],c2[0])< v < max(c1[0],c2[0])]
        xexpansion = [1 for v in expanded_cols if  min(c1[1],c2[1])< v < max(c1[1],c2[1])]
        ydiff = abs(c1[0] - c2[0])

        xdiff = abs(c1[1] - c2[1])
        #print(i+1,j+i+1,ydiff+xdiff)
        expansion_p1 = 2 - 1
        sum_p1 += ydiff + xdiff + len(yexpansion)*expansion_p1 + len(xexpansion)*expansion_p1
        expansion_p2 = 1000000 - 1
        sum_p2 += ydiff + xdiff + len(yexpansion)*expansion_p2 + len(xexpansion)*expansion_p2

print(sum_p1,sum_p2)
