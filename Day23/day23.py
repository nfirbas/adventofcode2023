import sys
sys.setrecursionlimit(10000)

from collections import defaultdict

def readFile():
    f = open("./input.txt", "r")
    out = []
    return [list(line.strip("\n")) for line in f.readlines()]


def next_move(curr, field, part1):
    x, y = curr
    if part1:
        if field[y][x] == "<": return [(x-1, y)]
        if field[y][x] == ">": return [(x+1, y)]
        if field[y][x] == "^": return [(x, y-1)]
        if field[y][x] == "v": return [(x, y+1)]
    return [(x,y) for (x,y)in [(x+1, y),(x-1, y),(x, y+1),(x, y-1)] if x>=0 and x<len(field[0])-1 and y >= 0 and y <= len(field)-1 and field[y][x] != "#"]

def DFS(start, end, init_dist, vus, field):
    if start == end:
        yield init_dist

    for v in next_move(start,field,True):
        if v not in vus:
            vus.add(v)
            yield from DFS(v, end, init_dist + 1, vus, field)
            vus.remove(v)

def first_start(field):
    print(max(DFS((1,0),(len(field[0])-2, len(field)-1),0,{(1,0)}, field)))

def second_start(field):
    end = (len(field[0])-2, len(field)-1)
    c_graph = [(1,0)] + [(x, y) for y in range(len(field)) for x in range(len(field[0])) if len(next_move((x,y), field, False)) > 2  ] + [end]


    G = defaultdict(list)
    for b in c_graph:
        for v in next_move(b, field, False):
            previous, cur = b, v
            d = 1
            while cur not in c_graph:
                previous, cur = cur, [p for p in next_move(cur, field, False) if p != previous][0]
                d += 1
            G[b].append((cur, d))      

    print(max(DFS2((1,0),end,0,{(1,0)}, G)))

def DFS2(start, end, init_dist, vus, G):
    if start == end:
        yield init_dist
    for v, d in G[start]:
        if v not in vus:
            vus.add(v)
            yield from DFS2(v, end, init_dist + d, vus, G)
            vus.remove(v)

if __name__ == "__main__":
    data=readFile()
    first_start(data)
    second_start(data)