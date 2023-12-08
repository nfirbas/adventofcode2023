from math import lcm
links = {}

def readFile():
    f = open("./input.txt", "r")
    lines = f.readlines()
    instructions = lines[0].removesuffix("\n")

    for line in lines[2:]:
        links[line.split(" = ")[0]] = line.split(" = ")[1].removesuffix(")\n").removeprefix("(").split(", ")
    return instructions



def fist_star(instructions):
    current = "AAA"
    
    for i in range(0, 1000000000):
        current = links[current][int(instructions[int(i%len(instructions))]=="R")]
        if current == "ZZZ":
            break
    print(i+1)
    return


def second_star(instructions):
    current = list(filter(lambda x: x.endswith("A"), links.keys()))
    value = []
    
    for i in range(0, 1000000000):
        for j in range(0, len(current)):
            current[j] = links[current[j]][int(instructions[int(i%len(instructions))]=="R")]
        curr = list(filter(lambda x: not x.endswith("Z"), current))
        if len(curr) != len(current):
            value.append(i+1)
            if len(curr) == 0: break
            current = curr


    print(lcm(*value))
    return





if __name__ == "__main__":
    instructions=readFile()

    fist_star(instructions)
    second_star(instructions)