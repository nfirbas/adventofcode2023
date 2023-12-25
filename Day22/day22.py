import numpy as np

def readFile():
    f = open("./input.txt", "r")
    out = []
    return [line.strip("\n") for line in f.readlines()]

def drop(bricks, eraly=False):
    dropped = set()
    seen = set()

    for i in range(len(bricks)):
        pts = bricks[i]

        while True:
            new_pts = {(p[0], p[1], p[2] - 1) for p in pts}
            if all(p not in seen and p[2] > 0 for p in new_pts):
                bricks[i] = new_pts
                pts = new_pts
                dropped.add(i)
                if eraly:
                    return 1
            else:
                break

        seen.update(pts)

    return len(dropped)


def first_start(lines):
    bricks = []

    for _,l in enumerate(lines):
        tmp = list(map(lambda x: tuple(map(int, x.split(","))), l.strip().split("~")))
        b = set([tmp[0], tmp[1]])

        idx_deltas = [c1 != c2 for c1, c2 in zip(tmp[0], tmp[1])]
        if any(idx_deltas):
            assert sum(idx_deltas) == 1
            idx = idx_deltas.index(True)
            for val in range(min(tmp[0][idx], tmp[1][idx]), max(tmp[0][idx], tmp[1][idx])):
                b.add(tuple(val if i == idx else c for i, c in enumerate(tmp[0])))
        bricks.append(b)

    bricks.sort(key=lambda x: min(p[2] for p in x))

    drop(bricks)
    total = 0
    total2 = 0

    for i in range(len(bricks)):
        new_bricks = bricks.copy()
        del new_bricks[i]
        total += not drop(new_bricks, True)
    for i in range(len(bricks)):
        new_bricks = bricks.copy()
        del new_bricks[i]
        total2 +=  drop(new_bricks)

    print(total)
    print(total2)

if __name__ == "__main__":
    data=readFile()
    first_start(data)