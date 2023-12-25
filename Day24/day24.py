from itertools import combinations
import z3

def readFile():
    f = open("./input.txt", "r")
    data = []
    for line in f.readlines():
        data.append((tuple(map(int, line.strip("\n").split(" @ ")[0].split(","))), tuple(map(int, line.strip("\n").split(" @ ")[1].split(",")))))
    return data

def first_start(hails):
    formulas = {}
    for hail in hails:
        pos, vel = hail
        x, y, z = pos
        a, b, c = vel
        t = a / b
        u = x - t * y
        f = (1, -t, -u)
        formulas[hail] = f

    r = 0
    groups = combinations(hails, 2)

    for group in groups:
        f1 = formulas[group[0]]
        f2 = formulas[group[1]]

        x1, y1, _ = group[0][0]
        x2, y2, _ = group[1][0]
        vel1 = group[0][1]
        vel2 = group[1][1]

        a1, b1, c1 = f1
        a2, b2, c2 = f2

        b = b2 - b1
        c = c2 - c1
        if b != 0:
            y = -c / b
            x = (-b1 * y - c1) / a1

            if 200000000000000 <= x <= 400000000000000 and 200000000000000 <= y <= 400000000000000:
                sign1 = (1 if vel1[0] > 0 else -1, 1 if vel1[1] > 0 else -1)
                sign2 = (1 if vel2[0] > 0 else -1, 1 if vel2[1] > 0 else -1)

                test1 = (1 if x - x1 > 0 else -1, 1 if y - y1 > 0 else -1)
                test2 = (1 if x - x2 > 0 else -1, 1 if y - y2 > 0 else -1)

                if sign1 == test1 and sign2 == test2:
                    r += 1
    print(r)


def second_start(hails):
    px, py, pz, vx, vy, vz = z3.Ints("px py pz vx vy vz")
    times = [z3.Int("t" + str(i)) for i in range(len(hails))]

    s = z3.Solver()
    for i, (pos, vel) in enumerate(hails):
        s.add(px + vx * times[i] == pos[0] + vel[0] * times[i])
        s.add(py + vy * times[i] == pos[1] + vel[1] * times[i])
        s.add(pz + vz * times[i] == pos[2] + vel[2] * times[i])
    s.check()
    ans = s.model().evaluate(px + py + pz)

    print(ans.as_long())


if __name__ == "__main__":
    data=readFile()
    first_start(data)
    second_start(data)