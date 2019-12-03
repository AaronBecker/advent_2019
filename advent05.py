
delta = {
    'U' : (0, 1),
    'D' : (0, -1), 
    'L' : (-1, 0),
    'R' : (1, 0)
}

def advent05(input):
    wires = input.strip().split("\n")
    grid = {}
    intersects = []
    x, y = 0, 0
    for cmd in wires[0].split(","):
        d = delta[cmd[0]]
        dist = int(cmd[1:])
        for _ in range(dist):
            x += d[0]
            y += d[1]
            grid[(x, y)] = 1
    x, y = 0, 0
    for cmd in wires[1].split(","):
        d = delta[cmd[0]]
        dist = int(cmd[1:])
        for _ in range(dist):
            x += d[0]
            y += d[1]
            if (x, y) in grid:
                intersects.append((x, y))
    return min(abs(p[0]) + abs(p[1]) for p in intersects)
