


def readFile():
    f = open("./input.txt", "r")
    return [line.strip("\n").split(" ") for line in f.readlines()]

def shoeLace(points):
    area = 0
    j = -1
    for i in range(len(points)):
        area += (points[j][0]+points[i][0]) * (points[j][1]-points[i][1])
        j = i
    return abs(area)/2

def first_start(digs):
    x, y = 0,0
    route = []
    path = 0

    for i, d in enumerate(digs):
        if d[0] == "R": x+=int(d[1])
        if d[0] == "L": x-=int(d[1])
        if d[0] == "U": y-=int(d[1])
        if d[0] == "D": y+=int(d[1])
        path+=int(d[1])
        route.append([x, y])
    print(shoeLace(route)+(path/2+1))

def second_star(digs):
    x, y = 0,0
    route = []
    path = 0

    for i, dig in enumerate(digs):
        d = dig[2]
        move = int("0x"+ d[2:-2], 0)
        if d[-2] == "0": x+=move
        if d[-2] == "2": x-=move
        if d[-2] == "3": y-=move
        if d[-2] == "1": y+=move
        path+=move
        route.append([x, y])
    print(shoeLace(route)+(path/2+1))


    

if __name__ == "__main__":
    digs=readFile()
    first_start(digs)
    second_star(digs)
