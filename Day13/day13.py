def readFile():
    f = open("./input.txt", "r")
    lines = f.read().split("\n\n")
    return [l.split("\n") for l in lines]

def first_star(data):
    print(sum([get_vertical(d, 0) + get_horizontal(d, 0) for d in data]))

def second_star(lines):
    print(sum([get_vertical(l, 1) + get_horizontal(l, 1) for l in lines]))

def get_horizontal(field, original_bonus):
    for i in range(len(field)-1):
        j = 0
        bonus = original_bonus
        while i-j>= 0 and i+j+1 < len(field):
            bonus -= get_dif(field[i-j],field[i+j+1])
            j+=1
        if  bonus == 0:
           return (i+1)*100
    return 0

def get_vertical(field, original_bonus):
    for i in range(len(field[0])-1):
        j = 0
        bonus = original_bonus
        while i-j>= 0 and i+j+1 < len(field[0]):
            dif = get_dif(get_vertical_array(field, i-j),get_vertical_array(field, i+j+1))
            bonus -= dif
            j += 1
        if  bonus == 0:
            return i+1
    return 0


def get_vertical_array(field, index):
    return [d[index] for d in field]

def get_dif(a, b):
    return sum([a[i]!=b[i] for i, x in enumerate(a)])

if __name__ == "__main__":
    lines=readFile()
    first_star(lines)
    second_star(lines)