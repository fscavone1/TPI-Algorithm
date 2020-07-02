import tpi_algorithm
import graph_setup
import numpy as np
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#import of the datasets
dataset_fb = os.path.join('Datasets', 'facebook_combined.txt')
dataset_twt = os.path.join('Datasets', 'twitter.txt')
dataset_gn = os.path.join('Datasets', 'gnutella.txt')

# RANDOM PROBABILITY - FIXED THRESHOLD
def random_fixed_test():
    avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    file_name = "Tests/test_rf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(dataset_fb)
        graph_setup.edge_random_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_fixed_threshold(graph, i+1)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# RANDOM PROBABILITY - FIXED THRESHOLD x5
def random_fixed_test2():
    file_name = "Tests/test_rf2.csv"
    open(file_name, 'w+').write("Threshold Incentives\n")
    iterations = 51

    graph = graph_setup.create_graph(dataset_twt)
    graph_setup.edge_random_probability(graph)
    for i in range (5,iterations,5):
        g = graph_setup.set_fixed_threshold(graph, i)
        tot_incentives = tpi_algorithm.tpi(g)
        open(file_name, 'a+').write("%d %d\n" % (i, tot_incentives))

# RANDOM PROBABILITY - RANDOM THRESHOLD
def random_random_test():
    avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    file_name = "Tests/test_rr.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(dataset_fb)
        graph_setup.edge_random_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_random_threshold(graph)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# RANDOM PROBABILITY - PROPORTIONAL TO DEGREE THRESHOLD
def random_proportional_test():
    avg = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    file_name = "Tests/test_rp.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(dataset_fb)
        graph_setup.edge_proportional_to_degree_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_degree_proportional_thresholds(graph, (i+1)/10)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

#print("GRAPH BEFORE:")
#graph_setup.print_info(g)

#print("GRAPH AFTER:")
#graph_setup.print_info(g)

#output.to_csv(os.path.join(base_dir, 'Output.csv'),index=False)
#tech = pd.read_csv(tech_path)

#random_fixed_test2()

#random_proportional_test()

