import snap
import graph_setup

def tpi(graph):
    count = 0
    count_2 = 0
    count_3 = 0

    nodes = []              #U
    for n in graph.Nodes():
        nodes.append(n.GetId())
    incentives = {}         #s(v)
    degrees = {}            #delta(v)
    thresholds = {}         #k(v)
    neighbors = {}          #N(v)
    for v in graph.Nodes():
        incentives[v.GetId()] = 0
        degrees[v.GetId()] = v.GetOutDeg()
        thresholds[v.GetId()] = graph.GetIntAttrDatN(v.GetId(), "threshold")
        temp_neigh = []
        for Id in v.GetOutEdges():
            temp_neigh.append(Id)
        neighbors[v.GetId()] = temp_neigh

    for v in nodes:
        if not nodes:
            break
        if thresholds.get(v) > degrees.get(v):
            incentives[v] = incentives[v] + thresholds[v] - degrees[v]
            count_3 += incentives[v]
            #print("Incentivo di ", v, " con valore: ", incentives[v])
            count_2 += 1
            thresholds[v] = degrees[v]
            if thresholds[v] == 0:
                nodes.remove(v)
        else:
            count += 1
            local_max = {}
            for u in nodes:
                if degrees[u] != 0:
                    local_max[u] = (thresholds[u]*(thresholds[u]+1))/(degrees[u]*(degrees[u]+1))
            node = max(local_max, key=local_max.get)

            if neighbors[node] is not None:
                for u in neighbors[node]:
                    degrees[u] -= 1
                    if neighbors[u] is not None:
                        neighbors[u] = neighbors[u].remove(node)
                nodes.remove(node)

    print("Numero di incentivi totali:", count_2, "con valore totale di", count_3, "e numero di nodi restanti:", count)


G2=graph_setup.create_graph("Datasets/gnutella.txt")
#G2=snap.GenRndGnm(snap.PUNGraph, 100, 1000)
graph_setup.edge_degree_probability(G2)
g=graph_setup.set_random_threshold(G2)
#print("GRAPH BEFORE:")
#graph_setup.print_info(g)
tpi(g)
#print("GRAPH AFTER:")
#graph_setup.print_info(g)