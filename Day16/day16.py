import sys
sys.setrecursionlimit(2000000)

WEST = [-1,0]
EAST = [1,0]
NORTH = [0,-1]
SOUTH = [0,1]

def readFile():
    f = open("./input.txt", "r")
    return [line.strip("\n") for line in f.readlines()]

def first_star(direction, x, y, field):
    visited = {}
    move(direction,x,y,field, visited)
    print(len(visited))
    return len(visited)

def second_star(field):
    r = []
    for f in range(len(field)):
        r.append(first_star(EAST, 0, f, field))
        r.append(first_star(WEST, len(field[f])-1, f, field))
    for f in range(len(field)):
        r.append(first_star(SOUTH, f, 0, field))
        r.append(first_star(NORTH, f, len(field)-1, field))
    print(max(r))
def move(direction, x, y, field, visited):
    if x < 0 or x >= len(field[0]) or y < 0 or y >= len(field):
        return
    
    key = str(x) + "|" + str(y)
    if key in visited:
        if direction in visited[key]: return
        visited[key].append(direction)
    else:
        visited[key] = [direction]
    
    if field[y][x] in "./\\":
        direction = mirror(field[y][x], direction)
        move(direction, x + direction[0], y + direction[1], field, visited)
    if field[y][x] in "-|":
        d = splitter( field[y][x], direction)
        for i, a in enumerate(d):
            move(a, x + a[0], y + a[1], field, visited)

def mirror(mirror, d):
    if mirror == "/":
        if d == EAST: return NORTH 
        if d == SOUTH: return WEST
        if d == WEST: return SOUTH
        if d == NORTH: return EAST
    if mirror == "\\":
        if d == EAST: return SOUTH 
        if d == SOUTH: return EAST
        if d == WEST: return NORTH
        if d == NORTH: return WEST
    return d

def splitter(splitter, direction):
    if splitter == "|" and direction in [WEST, EAST]:
        return [NORTH, SOUTH]
    if splitter == "-" and direction in [NORTH, SOUTH]:
        return [WEST, EAST]
    return [direction]


if __name__ == "__main__":
    field=readFile()
    first_star(EAST, 0, 0,field)
    second_star(field)
#7798
#8026