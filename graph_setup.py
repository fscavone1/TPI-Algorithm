import snap
import random
from statistics import median

'''AGGIUNGERE MAC VERSION'''
filename = "Datasets/twitter.txt"

def create_graph(filename):
    graph = snap.LoadEdgeList(snap.PUNGraph, filename, 0, 1)
    #print_info(graph)
    return graph

def print_info(graph):
    for NI in graph.Nodes():
        print("node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))

def edge_random_probability(graph):
    print("Numero di archi iniziali:", graph.GetEdges())
    for n in graph.Nodes():
        remove_edge = []
        for e in n.GetOutEdges():
            random_edge_value = round(random.uniform(0.0, 0.5), 5)
            random_del_value = round(random.uniform(0.0, 0.5), 5)
            if random_edge_value+random_del_value<=0.5:
                remove_edge.append(e)
        for dest in remove_edge:
            graph.DelEdge(n.GetId(), dest)
    print("Numero di archi rimanenti:", graph.GetEdges())

def edge_degree_probability(graph):
    print("Numero di archi iniziali", graph.GetEdges())
    for n in graph.Nodes():
        remove_edge = []
        for e in n.GetOutEdges():
            random_edge_value = (1/n.GetDeg())
            random_del_value = random.random()
            if random_edge_value+random_del_value<=0.5:
                remove_edge.append(e)
        for dest in remove_edge:
            graph.DelEdge(n.GetId(), dest)
    print("Numero di archi rimanenti:", graph.GetEdges())

def set_random_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    for n in g.Nodes():
        max= n.GetDeg() + int((n.GetDeg()/100)*20+1)
        random_value = random.randint(0, max)
        g.AddIntAttrDatN(n.GetId(), random_value, "threshold")
        print("Valore di threshold del nodo", n.GetId(),"con valore", g.GetIntAttrDatN(n.GetId(), "threshold"))
    return g

def set_fixed_threshold(graph, value):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
    return g

def set_median_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    data=[]
    print("Numero di nodi del grafo:", g.GetNodes())
    count=0
    for n in g.Nodes():
        data.append(n.GetDeg())
    value = median(data)
    print("Il valore della mediana è:", value)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
        print("Valore di threshold del nodo", n.GetId(), "con valore", g.GetIntAttrDatN(n.GetId(), "threshold"))
        if n.GetDeg()<value:
            count+=1
    print("Numero di nodi al di sotto della mediana:", count)
    return g
