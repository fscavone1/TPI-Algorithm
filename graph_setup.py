import snap
import random
from datetime import datetime

'''AGGIUNGERE MAC VERSION'''
filename = "Datasets/twitchDE.csv"


def create_graph(filename):
    #graph = snap.LoadEdgeList(snap.PUNGraph, filename, 0, 1, ',')
    graph = snap.GenRndGnm(snap.PUNGraph, 100, 1000)
    #print_info(graph)
    return graph


def print_info(graph):
    for NI in graph.Nodes():
        print("node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))

def edge_random_probability(graph):

    print("numero di archi: ", graph.GetEdges())
    count = 0
    for n in graph.Nodes():
        remove_edge = []
        for e in n.GetOutEdges():
            random_edge_value = round(random.random(), 5)
            random_del_value = round(random.random(), 5)



            if random_edge_value>=random_del_value:
                print("random_edge_value: %f, random_del_value: %f" %(random_edge_value, random_del_value))
                #print("sono stato cancellato: ", e.GetSrcNId(), e.GetDstNId())
                #graph.DelEdge(e.GetSrcNId(), e.GetDstNId())
                remove_edge.append(e)
        print("list: ", remove_edge)
        for dest in remove_edge:
            graph.DelEdge(n.GetId(), dest)
            count +=1
    print("count: ", count)
    print("numero di archi FINE: ", graph.GetEdges())

g=create_graph(filename)
edge_random_probability(g)
