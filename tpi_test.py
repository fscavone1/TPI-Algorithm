import tpi_algorithm
import graph_setup
import numpy as np
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#import of the datasets
facebook = os.path.join('Datasets', 'facebook_combined.txt')
twitter = os.path.join('Datasets', 'twitter.txt')
twitch = os.path.join('Datasets', 'musae_PTBR.txt')
gnutella = os.path.join('Datasets', 'p2p_Gnutella04.txt')

rnd_1 = os.path.join('Datasets', 'rnd_graph_1.txt')
rnd_2 = os.path.join('Datasets', 'rnd_graph_2.txt')
rnd_3 = os.path.join('Datasets', 'rnd_graph_3.txt')

# RANDOM PROBABILITY - FIXED THRESHOLD
def random_fixed_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_rf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(path)
        graph_setup.edge_random_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_fixed_threshold(graph, i+1)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# RANDOM PROBABILITY - FIXED THRESHOLD x5
def random_fixed_test2():
    file_name = "Tests/test_rf_twitter.csv"
    open(file_name, 'w+').write("Threshold Incentives\n")
    iterations = 51

    graph = graph_setup.create_graph(twitter)
    graph_setup.edge_random_probability(graph)
    for i in range (5,iterations,5):
        g = graph_setup.set_fixed_threshold(graph, i)
        tot_incentives = tpi_algorithm.tpi(g)
        open(file_name, 'a+').write("%d %d\n" % (i, tot_incentives))

# RANDOM PROBABILITY - RANDOM THRESHOLD
def random_random_test(dataset, path):
    avg = 0
    file_name = "Tests/"+dataset+"_tests/test_rr.csv"
    open(file_name, 'w+').write("Iteration Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(path)
        graph_setup.edge_random_probability(graph)
        g = graph_setup.set_random_threshold(graph)
        tot_incentives = tpi_algorithm.tpi(g)
        avg += tot_incentives
        open(file_name, 'a+').write("%d %d\n" % (j+1, tot_incentives))

    open(file_name, 'a+').write("Media %d\n" % (avg/iterations))

# RANDOM PROBABILITY - PROPORTIONAL TO DEGREE THRESHOLD
def random_proportional_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_rp.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(path)
        graph_setup.edge_random_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_degree_proportional_thresholds(graph, (i+1)/10)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))

# PROPORTIONAL TO DEGREE PROBABILITY - PROPORTIONAL TO DEGREE THRESHOLD
def proportional_proportional_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pp.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(path)
        graph_setup.edge_proportional_to_degree_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_degree_proportional_thresholds(graph, (i + 1) / 10)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y + 1, avg[y] / iterations))

# PROPORTIONAL TO DEGREE PROBABILITY - FIXED THRESHOLD
def proportional_fixed_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pf.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(path)
        graph_setup.edge_proportional_to_degree_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_fixed_threshold(graph, i+1)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))
        
# PROPORTIONAL TO DEGREE PROBABILITY - RANDOM THRESHOLD
def proportional_random_test(dataset, path):
    avg = np.zeros(10)
    file_name = "Tests/"+dataset+"_tests/test_pr.csv"
    open(file_name, 'w+').write("Threshold AVG_Incentives\n")
    iterations = 50

    for j in range(0, iterations):
        graph = graph_setup.create_graph(path)
        graph_setup.edge_proportional_to_degree_probability(graph)
        for i in range(0, 10):
            g = graph_setup.set_random_threshold(graph)
            tot_incentives = tpi_algorithm.tpi(g)
            avg[i] += tot_incentives

    for y in range(0, 10):
        open(file_name, 'a+').write("%d %d\n" % (y+1, avg[y]/iterations))
