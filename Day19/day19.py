import re
import functools

def readFile():
    f = open("./input.txt", "r")

    return f.read().split("\n\n")



def first_start(workflowsString, ratingsStrings):
    workflows = {}
    for i, w in enumerate(workflowsString.split("\n")):
        workflows[w.split("{")[0]] = w.split("{")[1][:-1].split(",")
    
    pattern = r'([a-z])=(\d+)'
    ratings = []
    for i, w in enumerate(ratingsStrings.split("\n")):
        result_dict = {}
        matches = re.findall(pattern, w)
        for match in matches:
            letter, value = match
            result_dict[letter] = int(value)
        ratings.append(result_dict)

    s = 0
    for i, r in enumerate(ratings):
        current = "in"
        while current not in "AR":
            for j, w in enumerate(workflows[current]):
                if not ":" in w:
                    current = w
                    break
                workflow = w.split(":")
                if "<" in w:
                    if r[workflow[0].split("<")[0]] < int(workflow[0].split("<")[1]):
                        current = workflow[1]
                        break
                else:
                    if r[workflow[0].split(">")[0]] > int(workflow[0].split(">")[1]):
                        current = workflow[1]
                        break
        if current == "A":
            s += sum([r[x] for a, x in enumerate(r)])
    print(s)

def second_start(workflowsString):
    start_ranges = {cat:range for cat,range in zip(list('xmas'),[[1,4000]]*4)}

    reg1 = r'(\w+){(.*),(\w+)}'
    reg2 = r'(\w)(<|>)(\d+):(\w+)'
    workflow = dict()
    for line in workflowsString.split("\n"):
        name, _, end = re.findall(reg1, line)[0]
        rules =[(cat,op,int(val),dest) for cat,op,val,dest in re.findall(reg2, line)]
        workflow[name] = (rules, end)


    check_ranges(start_ranges,workflow['in'], workflow)
    print(count)

count = 0
def check_ranges(ranges: dict[str, list[int]], wf, workflow):
    global count
    leftover = {k:[x for x in v] for (k,v) in ranges.items()}
    for cat,op,val,target in wf[0]:
        ranges_copy = {k:[x for x in v] for (k,v) in leftover.items()}
        if op == '<':
            ranges_copy[cat][1] = val - 1
            leftover[cat][0] = val
        else:
            ranges_copy[cat][0] = val + 1
            leftover[cat][1] = val
        if target == 'A':
            product = functools.reduce(lambda x,y: x*y, [x[1]-x[0]+1 for x in ranges_copy.values()], 1)
            count += product
        elif target == 'R':
            pass
        else:
            check_ranges(ranges_copy, workflow[target], workflow)
    if wf[1] == 'A':
        product = functools.reduce(lambda x,y: x*y, [x[1]-x[0]+1 for x in leftover.values()], 1)
        count += product
    elif wf[1] == 'R':
        pass
    else:
        check_ranges(leftover, workflow[wf[1]], workflow)

if __name__ == "__main__":
    data=readFile()
    first_start(data[0], data[1])
    second_start(data[0])

    #second_star(data[0])
