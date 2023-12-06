import re

def readFile():
    f = open("./input.txt", "r")
    lines = f.readlines()
    time = [int(num) for num in re.findall(r'\b\d+\b', lines[0])]
    distance = [int(num) for num in re.findall(r'\b\d+\b', lines[1])]
    return [time, distance]


def first_star(time, distance):
    answer = 1

    for i in range(0, len(time)):
        answer *= possibilities(time[i], distance[i])
    return answer

def second_star(time, distance):
    return possibilities( int(''.join([str(x) for x in time])), int(''.join([str(x) for x in distance])))


def possibilities(time, distance):
    for i in range(0, time):
        if (time-i)*i >  distance:
            min = i
            break

    for i in range(time, 0, -1):
        if (time-i)*i > distance:
            max = i
            break

    return max-min+1

if __name__ == "__main__":
    content = readFile()

    print(first_star(content[0], content[1]))
    print(second_star(content[0], content[1]))