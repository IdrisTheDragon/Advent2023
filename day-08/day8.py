from math import lcm

# example1.txt and example3.txt for p2
with open("input.txt","r")as infile:
    lines = infile.readlines()
    steps = lines.pop(0).strip()
    lines.pop(0)
    instructions = {}
    for l in lines:
        (key, vs) = l.split("=")
        key = key.strip()

        vs = vs.strip()[1:-1].split(",")
        #print(key,vs)
        instructions[key] = (vs[0],vs[1].strip())
    #print(instructions)

node = 'AAA'
step = 0
while node != 'ZZZ':
    step_index = step%len(steps)
    step_dir = steps[step_index]
    node = instructions[node][0] if step_dir == 'L' else instructions[node][1]
    #print(node,step_index,step_dir)
    step +=1
print(step)

# example3.txt for p2
with open("input.txt","r")as infile:
    lines = infile.readlines()
    steps = lines.pop(0).strip()
    lines.pop(0)
    instructions = {}
    for l in lines:
        (key, vs) = l.split("=")
        key = key.strip()

        vs = vs.strip()[1:-1].split(",")
        #print(key,vs)
        instructions[key] = (vs[0],vs[1].strip())
    # print(instructions)

nodes = [node for node in instructions if node.endswith('A')]
previously_mapped = {}
step = 0
#print(step,nodes)
cycles = []
while len(list(filter(lambda node: not node.endswith('Z'),nodes))) != 0:
    step_index = step%len(steps)
    step_dir = steps[step_index]
    new_nodes = []
    for node in nodes:
        next = instructions[node][0] if step_dir == 'L' else instructions[node][1]
        if next.endswith("Z"):
            cycles.append(step + 1)
        new_nodes.append(next)
    if len(cycles) == len(nodes):
        break
    nodes = new_nodes
    step +=1
    #print(step,nodes)
print(lcm(*cycles))
