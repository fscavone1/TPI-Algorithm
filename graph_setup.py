import snap
import random
from networkx import nx
from statistics import median
import math

#function for the realization of the graph starting from a dataset
def create_graph(filename):
    graph = snap.LoadEdgeList(snap.PUNGraph, filename, 0, 1)
    #print_info(graph)
    return graph

#function for the generation of a random graph
def random_graph_generator(nodes, edges, num):
    graph = nx.gnm_random_graph(nodes,edges)
    path = "Datasets/rnd_graph_"+num+".txt"
    fh = open(path, 'wb')
    nx.write_edgelist(graph, fh, encoding="utf-8")

    g = create_graph(path)
    #print_info(g)

#function for printing information relating to the input graph
def print_info(graph):
    for NI in graph.Nodes():
        print("node: %d, out-degree %d, in-degree %d" % (NI.GetId(), NI.GetOutDeg(), NI.GetInDeg()))
    print("Number of nodes: ", graph.GetNodes())
    print("Number of edges: ", graph.GetEdges())
    print("Maximum degree: ", graph.GetNI(snap.GetMxDegNId(graph)).GetDeg())
    print("Diameter (approximate): ", snap.GetBfsFullDiam(graph, 10))
    print("Triangles: ", snap.GetTriads(graph))
    print("Clustering coefficient: ", snap.GetClustCf(graph))

#function to eliminate edges with randomly generated probabilities
def edge_random_probability(graph):
    print("Number of starting edges: ", graph.GetEdges())
    for n in graph.Nodes():
        remove_edge = []
        for e in n.GetOutEdges():
            random_edge_value = round(random.uniform(0.1, 1), 5)
            random_del_value = round(random.uniform(0.1, 1), 5)
            if random_edge_value >= random_del_value:
                remove_edge.append(e)
        for dest in remove_edge:
            graph.DelEdge(n.GetId(), dest)
    print("Number of remaining edges: ", graph.GetEdges())

#function to eliminate edges with probability proportional to the degree of the node
def edge_proportional_to_degree_probability(graph):
    print("Number of starting edges: ", graph.GetEdges())
    for n in graph.Nodes():
        remove_edge = []
        for e in n.GetOutEdges():
            random_edge_value = (1/n.GetDeg())
            random_del_value = random.random()
            if random_edge_value >= random_del_value:
                remove_edge.append(e)
        for dest in remove_edge:
            graph.DelEdge(n.GetId(), dest)
    print("Number of remaining edges: ", graph.GetEdges())

#function to set random thresholds to the edges of the graph
def set_random_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    for n in g.Nodes():
        max= n.GetDeg() + int((n.GetDeg()/100)*20+1)
        random_value = random.randint(0, max)
        g.AddIntAttrDatN(n.GetId(), random_value, "threshold")
        #print("Threshold of the node ", n.GetId()," with value", g.GetIntAttrDatN(n.GetId(),"threshold"))
    return g

#function to set fixed thresholds to the edges of the graph
def set_fixed_threshold(graph, value):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
    return g

#function to set thresholds based on the value of the median in relation to the number of edges of the graph
def set_median_threshold(graph):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    data=[]
    print("Number of graph nodes: ", g.GetNodes())
    count=0
    for n in g.Nodes():
        data.append(n.GetDeg())
    value = median(data)
    print("The median value is: ", value)
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), value, "threshold")
        print("Threshold of the node ", n.GetId(), " with value ", g.GetIntAttrDatN(n.GetId(), "threshold"))
        if n.GetDeg()<value:
            count+=1
    print("Number of nodes below the median: ", count)
    return g

#function to set proportional to degree thresholds to the edges of the graph
def set_degree_proportional_thresholds(graph, value):
    g = snap.ConvertGraph(snap.PNEANet, graph)
    print("Number of graph nodes: ", g.GetNodes())
    for n in g.Nodes():
        g.AddIntAttrDatN(n.GetId(), math.floor(n.GetDeg() * value) + 1, "threshold")
    return g
