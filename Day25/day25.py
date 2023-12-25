from os import path
import networkx as nx
import math

def readFile():
    f = open("./input.txt", "r")
    data = []
    for line in f.readlines():

        data.append([line.strip("\n").split(": ")[0], line.strip("\n").split(": ")[1].split(" ")])
    return data


def first_start(data):
    G = nx.Graph()

    for line in data:
        edges = list(zip([line[0]] * len(line[1]), line[1]))
        G.add_edges_from(edges, capacity=1)

    bridges = nx.minimum_edge_cut(G)
    G.remove_edges_from(bridges)

    groups = nx.connected_components(G)
    print(math.prod([len(g) for g in groups]))

if __name__ == "__main__":
    data = readFile()
    first_start(data)