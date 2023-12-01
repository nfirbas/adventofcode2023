from string import digits

def readFile():
    f = open("./input.txt", "r")
    return f.readlines()

def first_star():
        sum = 0

        for line in lines:
            value = ''.join(c for c in line if c in digits)
            if len(value) == 0:
                continue
            sum += int(value[0]+value[len(value)-1])

        print(sum)

def second_star():
        sum = 0

        for line in lines:
            value = line.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine')
            value = ''.join(c for c in value if c in digits)
            if len(value) == 0:
                continue
            sum += int(value[0]+value[len(value)-1])

        print(sum)


if __name__ == "__main__":
    lines = readFile()

    first_star()
    second_star()
