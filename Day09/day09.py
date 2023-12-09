from math import lcm
links = {}

def readFile():
    f = open("./input.txt", "r")
    return [list(map(int, line.split(" "))) for line in f.readlines()]

def first_star(values):
    print(sum([get_next(x) for x in values]))

def first_second(values):
    print(sum([get_prev(x) for x in values]))

def get_next(values):
    if len(values) == 0 or all(v == 0 for v in values):
        return 0
    
    return values[len(values)-1]+get_next([values[i+1]-values[i] for i in range(0, len(values)-1)])

def get_prev(values):
    if len(values) == 0 or all(v == 0 for v in values):
        return 0
    
    return values[0]+get_prev([values[i]-values[i+1] for i in range(0, len(values)-1)])



if __name__ == "__main__":
    values=readFile()
    first_star(values)
    first_second(values)