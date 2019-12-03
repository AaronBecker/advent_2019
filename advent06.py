
delta = {
    'U' : (0, 1),
    'D' : (0, -1), 
    'L' : (-1, 0),
    'R' : (1, 0)
}

def advent06(input):
    wires = input.strip().split("\n")
    grid = {}
    x, y, steps, mindelay = 0, 0, 0, 1000000000
    for cmd in wires[0].split(","):
        d = delta[cmd[0]]
        dist = int(cmd[1:])
        for _ in range(dist):
            x += d[0]
            y += d[1]
            steps += 1
            if not (x, y) in grid:
                grid[(x, y)] = steps
    x, y, steps = 0, 0, 0
    for cmd in wires[1].split(","):
        d = delta[cmd[0]]
        dist = int(cmd[1:])
        for _ in range(dist):
            x += d[0]
            y += d[1]
            steps += 1
            if (x, y) in grid and mindelay > grid[(x, y)] + steps:
                mindelay = grid[(x, y)] + steps
    return mindelay
