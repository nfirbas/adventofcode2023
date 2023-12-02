def readFile():
    f = open("./input.txt", "r")
    return f.readlines()


def first_star(lines):
    sum = 0
    limit = {'red' : 12, 'green' : 13, 'blue' : 14}
    for line in lines:
        ok = True
        for draw in line.replace(";", ",").replace("\n", "").split(": ")[1].split(", "):
            cubes = draw.split(' ')
            if limit[cubes[1]] < int(cubes[0]):
                ok = False

        if ok==False:
            continue
        sum += int(line.replace("Game ", "").split(":")[0])
    print(sum)

def second_star(lines):
    sum = 0
    for line in lines:
        limit = {'red' : 1, 'green' : 1, 'blue' : 1}
        for draw in line.replace("\n", "").split(": ")[1].split(", "):
            for game in draw.split('; '):
                cubes=game.split(",")
                for cube in cubes:
                    cube = cube.split(' ')
                    limit[cube[1]] = max(int(cube[0]), limit[cube[1]])
                    
        sum += limit["red"] * limit["green"] * limit["blue"]
    print(sum)



if __name__ == "__main__":
    lines = readFile()

    first_star(lines)
    second_star(lines)
