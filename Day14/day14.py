import time
def readFile():
    f = open("./input.txt", "r")
    return [list(line.strip("\n")) for line in f.readlines()]

def first_star(data):
    for i, row in enumerate(data):
        for j, point in enumerate(row):
            if point == "O": 
                data = move_north(i,j, data)

    print(sum([len([i for i in row if i=="O"])*(len(data)-i) for i, row in enumerate(data)]))

def second_star(data):
    loads = {}
    for x in range(1,1_000_000_000):
        data = cycle(data)
        h = ','.join(str(item) for innerlist in data for item in innerlist)
        if h in loads.keys():
            break
        loads[h] = (x,sum([len([i for i in row if i=="O"])*(len(data)-i) for i, row in enumerate(data)]))
    
    for k,(c,v) in loads.items():
        if c==((1_000_000_000-(loads[h][0]-1))%(x-loads[h][0])+loads[h][0]-1):
            break
    print(v)

def cycle(data):
    for x in range(4):
        for i, row in enumerate(data):
            for j, point in enumerate(row):
                if point == "O": 
                    data = move_north(i,j, data)
        data = rotate(data)
    return data


def rotate(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def move_north(y, x, data):
    if y-1 < 0:
        return data
    if data[y- 1][x] in ['#', 'O']:
        return data
    
    data[y][x] = "."
    data[y-1][x] = "O"
    
    return move_north(y-1, x, data)

if __name__ == "__main__":
    lines=readFile()
    first_star(lines)
    lines=readFile()
    second_star(lines)
