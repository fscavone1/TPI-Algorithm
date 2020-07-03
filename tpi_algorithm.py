import snap
import graph_setup

#implementation of targeting with partial incentives (TPI)
def tpi(graph):
    count = 0
    count_2 = 0
    count_3 = 0
    nodes = []              #U

    #for loop to fill the nodes list of all nodes in the graph using their id
    for n in graph.Nodes():
        nodes.append(n.GetId())

    #initialization of useful variables
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

    # The for loop scrolls all nodes in the nodes list.
    for v in nodes:
        # The cycle stops when the list becomes empty.
        if not nodes:
            break
        # If the threshold is greater than the degree of the node, we update the value of the incentive and the threshold.
        # If the threshold is 0, we eliminate the node from the nodes list.
        if thresholds.get(v) > degrees.get(v):
            incentives[v] = incentives[v] + thresholds[v] - degrees[v]
            count_3 += incentives[v]
            count_2 += 1
            thresholds[v] = degrees[v]
            if thresholds[v] == 0:
                nodes.remove(v)
        # On the contrary, if the threshold is less than the degree, the heuristic created chooses among all
        # the remaining nodes the node that appears to have the maximum ratio shown and eliminates it from the network.
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

    print("Number of total incentives: ", count_2, " with total value of ", count_3, " and number of remaining nodes: ", count)
    return count_3