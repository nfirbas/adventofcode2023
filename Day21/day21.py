import numpy as np

def readFile():
    f = open("./input.txt", "r")
    return [list(line.strip("\n")) for line in f.readlines()]


class Location:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        self.string = str(x)+"|"+str(y)

def first_start(data, steps):
    locations = {}
    loc = Location(len(data[0])//2,len(data)//2)
    locations[loc.string] = loc
    for x in range(steps):
        newLocations = {}
        for _, loc in enumerate(locations.values()):
            for _, step in enumerate([[0,1], [0,-1], [-1,0],[1,0]]):
                if data[loc.y+step[0]][loc.x+step[1]] != "#":
                    newLoc = Location(loc.x+step[1],loc.y+step[0])
                    newLocations[newLoc.string] = newLoc
        locations = newLocations
        
    print(len(locations))
    return (len(locations))
   

def second_star(data):
    data  = expand_matrix(data,11)
    y = [first_start(data, steps) for steps in [65, 196, 327]]
    x = np.array([0, 1, 2])

    target = (26501365 - 65) // 131
    coefficients = np.polyfit(x, y, 2)
    result = np.polyval(coefficients, target)
    print(np.round(result, 0))

def expand_matrix(data, factor):
    return [
        [
            data[i % len(data)][j % len(data[0])]
            for j in range(factor * len(data[0]))
        ]
        for i in range(factor * len(data))
    ]

if __name__ == "__main__":
    data=readFile()
    first_start(data, 64)
    second_star(data)