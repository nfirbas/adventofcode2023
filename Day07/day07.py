from collections import Counter

table = dict(zip('23456789TJQKA', range(13)))
table2 = dict(zip('J23456789TQKA', range(13)))


def readFile():
    f = open("./input.txt", "r")
    lines = f.readlines()
    data = []
    for line in lines:
        data.append([line.split(" ")[0], int(line.split(" ")[1].replace("\n", ""))])
    return data

def first_sort(hands):
    return sorted(Counter(hands[0]).values(), reverse=True), [table[c] for c in hands[0]]

def fist_star(hands):
    sum = 0
    h = sorted(hands, key=first_sort)
    for i in range(0,len(h)):
        sum += (i+1)*h[i][1]
    
    print(sum)

def second_sort(hands):
    if hands[0] == "JJJJJ":
        hand_type = [5,]
    else:
        c = Counter(hands[0])
        jokers = c.pop('J', 0)
        hand_type = sorted(c.values(), reverse=True)
        hand_type[0] += jokers

    return hand_type, [table2[c] for c in hands[0]]

def second_star(hands):
    sum = 0
    h = sorted(hands, key=second_sort)
    for i in range(0,len(h)):
        sum += (i+1)*h[i][1]
    
    print(sum)



if __name__ == "__main__":
    content = readFile()

    fist_star(content)
    second_star(content)