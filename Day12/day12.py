from functools import lru_cache

def readFile():
    f = open("./input.txt", "r")
    return [line.strip("\n") for line in f.readlines()]


@lru_cache
def arrangements(pixels, groups):
    if len(pixels) == 0:
        return 1 if len(groups) == 0 else 0
    if pixels.startswith("."):
        return arrangements(pixels.strip("."), groups)
    if pixels.startswith("?"):
        return arrangements(pixels.replace("?", ".", 1), groups) \
            + arrangements(pixels.replace("?", "#", 1), groups)
    if pixels.startswith("#"):
        if len(groups) == 0:
            return 0
        if len(pixels) < groups[0]:
            return 0
        if any(c == "." for c in pixels[0:groups[0]]):
            return 0
        if len(groups) > 1:
            if len(pixels) < groups[0] + 1 or pixels[groups[0]] == "#":
                return 0
            return arrangements(pixels[groups[0] + 1:], groups[1:])
        else:
            return arrangements(pixels[groups[0]:], groups[1:])

def first_star(lines):
    print(sum([arrangements(line.split(" ")[0], tuple(int(x) for x in line.split(" ")[1].split(","))) for line in lines]))

def second_star(lines):
    print(sum([arrangements("?".join([line.split(" ")[0]]*5), tuple(int(x) for x in line.split(" ")[1].split(","))*5) for line in lines]))


if __name__ == "__main__":
    lines=readFile()
    first_star(lines)
    second_star(lines)
   