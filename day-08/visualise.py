import graphviz
dot = graphviz.Digraph("G", engine="neato")
dot.format = "svg"

#dot.attr(rankdir="LR", size="8,5")

# example3.txt for p2
with open("input.txt","r")as infile:
    lines = infile.readlines()
    steps = lines.pop(0).strip()
    lines.pop(0)
    for l in lines:
        (key, vs) = l.split("=")
        key = key.strip()

        vs = vs.strip()[1:-1].split(",")
        dot.edge(key, vs[0])
        dot.edge(key, vs[1].strip())
    # print(instructions)
    dot.render(f"out/day-08.gv")
