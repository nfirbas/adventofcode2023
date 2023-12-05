import numpy as np
from tqdm import trange

def readFile():
    f = open("./input.txt", "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    # lines = [l for l in lines if l != '']
    seeds = [int(s) for s in lines[0].split()[1:]]

    maps = []
    for line in lines[2:]:
        if 'map' in line:
            maps.append([])
        elif line != '':
            maps[-1].append([int(l) for l in line.split()])

    return [seeds, maps]

def resolve_map(map, index):
    for entry in map:
        if index < (entry[1] + entry[2]) and index >= entry[1]:
            return index + entry[0] - entry[1]
    return index 



def resolve_map_reverse(map, index):
    for entry in map:
        if index < (entry[0] + entry[2]) and index >= entry[0]:
            return index - entry[0] + entry[1]
    return index

def first_star(seeds, maps):
    result = []
    for seed in seeds:
        for map in maps:
            seed = resolve_map(map, seed)
        result.append(seed)
    return np.min(result)

def second_star(seeds, maps):
    maps.reverse()
    for i in trange(0, 100000000, 1000, disable=True):
        seed = i
        for m in maps:
            seed = resolve_map_reverse(m, seed)
        for seeed, rang in np.array(seeds).reshape((-1, 2)):
            if seed >= seeed and seed < seeed + rang:
                iter_1 = i
                break
        else: continue
        break

    for i in trange(iter_1 - 1000, iter_1 + 1, disable=True):
        seed = i
        for map in maps:
            seed = resolve_map_reverse(map, seed)
        for seeed, rang in np.array(seeds).reshape((-1, 2)):
            if seed >= seeed and seed < seeed + rang:
                return i
                break
        else: continue
        break

if __name__ == "__main__":
    content = readFile()

    print(first_star(content[0], content[1]))
    print(second_star(content[0], content[1]))