from itertools import combinations

def readFile():
    f = open("./input.txt", "r")
    return [list(line.strip("\n")) for line in f.readlines()]


def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

def first_star(star_map):
    galaxies = []
    appended = False
    for i, line in enumerate(star_map):
        if appended: appended = False
        elif '#' not in line:
            star_map.insert(i, ['.'] * len(star_map[0]))
            appended = True

    appended = False
    for i, col in enumerate(zip(*star_map)):
        if appended: appended = False
        elif '#' not in col:
            for j, row in enumerate(star_map):  
                star_map[j].insert(i, ".")
            appended = True

    for i, row in enumerate(star_map):
        for j, item in enumerate(row):
            if item == "#":
                galaxies.append([i, j])
    print(sum([distance(a, b) for a, b in combinations(galaxies, 2)]))


def coords_after_expansion(a,col, rows,multi ):
    empty_cols_before = sum([1 for col in col if col < a[1]])
    empty_rows_before = sum([1 for row in rows if row < a[0]])
    return [a[0] + empty_rows_before * (multi - 1),
            a[1] + empty_cols_before * (multi - 1)]

def second_star(star_map):
    galaxies = []
    rows = []
    cols = []
    
    for i, line in enumerate(star_map):
        if '#' not in line:
            rows.append(i)

    for i, col in enumerate(zip(*star_map)):
        if '#' not in col:
            cols.append(i)
    
    for i, row in enumerate(star_map):
        for j, item in enumerate(row):
            if item == "#":
                galaxies.append(coords_after_expansion([i,j], cols, rows,1_000_000))

    print(sum([distance(a, b) for a, b in combinations(galaxies, 2)]))


if __name__ == "__main__":
    star_map=readFile()
    first_star(star_map)
    star_map=readFile()
    second_star(star_map)
   