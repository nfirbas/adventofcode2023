from itertools import count
from queue import PriorityQueue

NORTH = 0 - 1j
SOUTH = 0 + 1j
EAST = 1 + 0j
WEST = -1 + 0j

def readFile():
    f = open("./input.txt", "r")
    return {
        complex(x, y): loss for y, l in enumerate(f.readlines()) for x, loss in enumerate(map(int, l.strip()))
    }

def first_start(field, mini, maxi):
    unique = count()
    paths = PriorityQueue()
    end = max(field, key=abs)
    h = int(abs(end))

    paths.put((h, 0, 1, next(unique), EAST, 0 + 0j))
    paths.put((h, 0, 1, next(unique), SOUTH, 0 + 0j))
    history = set()
    while not paths.empty():
            _, heat, length, _, dir, pos = paths.get()
            hist = (length, dir, pos)
            if hist in history:
                continue
            history.add(hist)
            if pos == end and length > mini:
                print(heat)
                return
            pos += dir
            if pos in field:
                heat += field[pos]
                h = int(abs(end - pos)) + heat
                if length >= mini:
                    paths.put((h, heat, 1, next(unique), dir * 1j, pos))
                    paths.put((h, heat, 1, next(unique), dir * -1j, pos))
                if length < maxi:
                    paths.put((h, heat, length + 1, next(unique), dir, pos))

if __name__ == "__main__":
    field=readFile()
    first_start(field, 0,3)
    first_start(field, 4,10)
