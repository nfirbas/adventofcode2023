
def readFile():
    f = open("./input.txt", "r")

    return  f.read().split(",")

def hash(c):
    t = 0
    for i, l in enumerate(c):
        t = ((t+ord(l))*17)%256
    return t

def first_star(codes):
    print(sum([hash(c) for i, c in enumerate(codes)]))
   


def second_star(codes):
    boxes = [[] for x in range(256)]
    strength = {}
    for i, c in enumerate(codes):
        if c[-1] == "-":
            l = c[:-1]
            if l in boxes[hash(l)]:
                boxes[hash(l)].remove(l)
        else:
            l = c[:-2]
            if l not in boxes[hash(l)]:
                boxes[hash(l)].append(l)
            strength[l] = int(c[-1])

    print(sum((i+1)*(j+1)*strength[l] for i in range(256) for j, l in enumerate(boxes[i])))



if __name__ == "__main__":
    codes=readFile()
    first_star(codes)
    second_star(codes)
