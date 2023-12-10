import math
posses = []


def readFile():
    f = open("./input.txt", "r")
    return [list(line.strip("\n")) for line in f.readlines()]

def find_start(pipes):
    for i in range(0, len(pipes)-1): 
        for j in range(0, len(pipes[i])-1):
            if pipes[i][j] == "S": return [i, j]

def next_pipe_location(prev, curr, pipes):
    if pipes[curr[0]][curr[1]] == "|":
        if prev[0]>curr[0]: return [-1, 0]
        else: return [1, 0]

    if pipes[curr[0]][curr[1]] == "-":
        if prev[1]>curr[1]: return [0, -1]
        else: return [0, 1]

    if pipes[curr[0]][curr[1]] == "L":
        if prev[0]==curr[0]: return [-1, 0]
        else: return [0, 1]

    if pipes[curr[0]][curr[1]] == "J":
        if prev[0]==curr[0]: return [-1, 0]
        else: return [0, -1]

    if pipes[curr[0]][curr[1]] == "7":
        if prev[0]==curr[0]: return [1, 0]
        else: return [0, -1]

    if pipes[curr[0]][curr[1]] == "F":
        if prev[0]==curr[0]: return [1, 0]
        else: return [0, 1]

def next_pipe_location(prev, curr, pipes):
    if pipes[curr[0]][curr[1]] == "|":
        if prev[0]>curr[0]: return [-1, 0]
        else: return [1, 0]

    if pipes[curr[0]][curr[1]] == "-":
        if prev[1]>curr[1]: return [0, -1]
        else: return [0, 1]

    if pipes[curr[0]][curr[1]] == "L":
        if prev[0]==curr[0]: return [-1, 0]
        else: return [0, 1]

    if pipes[curr[0]][curr[1]] == "J":
        if prev[0]==curr[0]: return [-1, 0]
        else: return [0, -1]

    if pipes[curr[0]][curr[1]] == "7":
        if prev[0]==curr[0]: return [1, 0]
        else: return [0, -1]

    if pipes[curr[0]][curr[1]] == "F":
        if prev[0]==curr[0]: return [1, 0]
        else: return [0, 1]

def find_first_pipe(start, pipes):    
    #if the start is on the edge, this trows a panic :) 
    if pipes[start[0]-1][start[1]] in "|7F":
        return [start[0]-1, start[1]]
    
    if pipes[start[0]][start[1]+1] in "-J7":
        return [start[0], start[1]+1]
    
    if pipes[start[0]+1][start[1]] in "|LJ":
        return [start[0]+1, start[1]]
    
def start_tail(start, pipes):
    path = ""
    if pipes[start[0]-1][start[1]] in "|7F":
        path += "T"
    
    if pipes[start[0]][start[1]+1] in "-J7":
        path += "R"
    
    if pipes[start[0]+1][start[1]] in "|LJ":
        path += "D"

    
    if path == "T": return "J" 
    if path == "R": return "-" 
    if path == "D": return "7" 
    if path == "TR": return "L" 
    if path == "TD": return "|" 
    if path == "RD": return "F" 

def first_star(pipes):
    prev = find_start(pipes)
    posses.append(prev)
    curr = find_first_pipe(prev, pipes)
    i = 1
    while pipes[curr[0]][curr[1]] != "S":
        i+=1
        posses.append(curr)
        prev, curr = curr, list(map(sum, zip(*[next_pipe_location(prev, curr, pipes), curr])))
   
    print(math.ceil(i/2))

def second_star(pipes):
    start = find_start(pipes)
    pipes[start[0]][start[1]] = start_tail(start, pipes)
   
    for y in range(len(pipes)):
        for x in range(len(pipes[0])):
            if not [y, x] in posses:
                pipes[y][x] = '.'

    count = 0
    for y, line in enumerate(pipes):
        out = False
        for x, c in enumerate(line):
            if c in "|JL":
                out = not out
            elif c == '.' and out:
                count += 1
    print(count)


if __name__ == "__main__":
    pipes=readFile()
    first_star(pipes)
    second_star(pipes)
   