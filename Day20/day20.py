import queue
import math
class Pulse:
    def __init__(self, f, to, power):
        self.origin = f
        self.to = to
        self.power = power

class Module:
    def __init__(self, name, conn):
        self.inputs = {}
        self.IsConjunction = False
        self.IsFlipFlop = False
        self.flipFlop = False
        if name.startswith('%'):
            self.IsFlipFlop = True
            self.Name =  name[1:]
            self.flipFlop = False
        elif name.startswith('&'):
            self.IsConjunction = True
            self.Name = name[1:]
        else:
            self.Name = name
        self.outputs = []
        for i, o in enumerate(conn.split(", ")):
            self.outputs.append(o)
    def addInputs(self, network):
        for i, n in enumerate(network):
            if self.Name in network[n].outputs:
                self.inputs[n] = "low"


def readFile():
    f = open("./input.txt", "r")
    return [line.strip("\n").split(" -> ") for line in f.readlines()]

def first_start(data):
    low = 0
    hi = 0
    
    network = {}
    for i, mod in enumerate(data):
        tmp = Module(str(mod[0]), str(mod[1]))
        network[tmp.Name] = tmp
    for i, a in enumerate(network):
        network[a].addInputs(network)

    q = queue.Queue()
    cycles = {}
    for i in range(15000):
        q.put(Pulse("button", "broadcaster", "low"))
        while not q.empty():
            curr = q.get()
            if curr.power == "high": hi += 1
            if curr.power == "low": low += 1
            if curr.to not in network:
                    continue
            power = curr.power
            if network[curr.to].IsConjunction:
                network[curr.to].inputs[curr.origin] = curr.power
                if "low" in network[curr.to].inputs.values():
                    power = "high"
                else: 
                    power = "low"
                if power == "low" and curr.to not in cycles:
                    cycles[curr.to] = i+1
            if network[curr.to].IsFlipFlop:
                if power == "high":
                    continue
                network[curr.to].flipFlop = not network[curr.to].flipFlop
                if network[curr.to].flipFlop:
                    power = "high"
                if not network[curr.to].flipFlop:
                    power = "low"

            for j, ne in enumerate(network[curr.to].outputs):
                q.put(Pulse(curr.to, ne, power))
        if i == 1000: 
            print(low*hi)
    print(math.lcm(*cycles.values()))
    
   

if __name__ == "__main__":
    data=readFile()
    first_start(data)