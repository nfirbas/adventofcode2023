def readFile():
    f = open("./input.txt", "r")
    return [line.rstrip('\n') for line in f]

def find_symbol(engine_schematic, h, w, i, j):
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        r, c = i + dr, j + dc
        if 0<=r<h and 0<=c < w:
            if (not engine_schematic[r][c].isdigit()) and (not engine_schematic[r][c] == "."):
                return True
    return False


def find_gear(engine_schematic, h, w, i, j):
    hash_map = {}
    for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        r, c = i + dr, j + dc
        if 0<=r<h and 0<=c < w:
            if engine_schematic[r][c] == "*":
                hash_map[str(r)+":"+str(c)] = 1
    return hash_map

def first_star(engine_schematic):
    sum = 0
    h = len(engine_schematic)
    w = len(engine_schematic[0])

    for i in range(0,h):
        number_start = -1      
        symbol = False
        for j in range(0, w):
            if engine_schematic[i][j].isdigit():
                if number_start == -1: number_start = j
                if not symbol: symbol = find_symbol(engine_schematic, h,w,i,j)
            
            if (not engine_schematic[i][j].isdigit()) or w-1== j:
                if number_start != -1:
                    if w-1== j and engine_schematic[i][j].isdigit(): j+=1
                    if symbol: sum += int(''.join(engine_schematic[i][number_start:j]))
                    number_start = -1
                    symbol = False
        
    print(sum)

def join_dic(a, b):
    for bi, bv in b.items():
        if bi in a:
            a[bi] = a[bi]*bv
        else:
            a[bi]=bv
    return a

def second_star(engine_schematic):
    h = len(engine_schematic)
    w = len(engine_schematic[0])

    main_map = {}

    for i in range(0,h):
        number_start = -1      
      
        hash_map = {}
        for j in range(0, w):
            if engine_schematic[i][j].isdigit():
                if number_start == -1: number_start = j
                hash_map.update(find_gear(engine_schematic, h,w,i,j))
            
            if (not engine_schematic[i][j].isdigit()) or w-1== j:
                if number_start != -1:
                    if w-1== j and engine_schematic[i][j].isdigit(): j+=1
                    num = int(''.join(engine_schematic[i][number_start:j]))
                    hash_map = dict.fromkeys(hash_map,-num)
                    main_map = join_dic(main_map, hash_map)
                    hash_map.clear()
                    number_start = -1
                  
           
        
    print(sum(v for v in main_map.values() if v > 0))


if __name__ == "__main__":
    engine_schematic = readFile()

    first_star(engine_schematic)
    second_star(engine_schematic)
#72246648