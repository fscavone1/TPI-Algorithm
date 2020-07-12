import matplotlib.pyplot as plt
import pandas as pd

def create_graph(test_type, thresholds,title):

    facebook_results = pd.read_csv("Tests/facebook_combined_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)
    musae_results = pd.read_csv("Tests/musae_PTBR_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)
    gnutella_results = pd.read_csv("Tests/p2p_gnutella04_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)
    rnd_results_1 = pd.read_csv("Tests/rnd_graph_1_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)
    rnd_results_2 = pd.read_csv("Tests/rnd_graph_2_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)
    rnd_results_3 = pd.read_csv("Tests/rnd_graph_3_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)

    plt.figure(figsize=(12,8)) 
   
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    ax1.plot(range(thresholds), facebook_results[facebook_results.columns[1]],label='facebook_combined')
    ax1.plot(range(thresholds), musae_results[musae_results.columns[1]], label='musae_PTBR')
    ax1.plot(range(thresholds), gnutella_results[gnutella_results.columns[1]], label='p2p_gnutella04')
    ax1.plot(range(thresholds), rnd_results_1[rnd_results_1.columns[1]], label='rnd_graph_1')
    ax1.plot(range(thresholds), rnd_results_2[rnd_results_2.columns[1]], label='rnd_graph_2')
    ax1.plot(range(thresholds), rnd_results_3[rnd_results_3.columns[1]], label='rnd_graph_3')
    
    ax1.set_title(title)
    ax1.set_xlabel(facebook_results.columns[0])
    ax1.set_ylabel(facebook_results.columns[1])

    fig1.show()


def create_comparison_graphs(dataset1, dataset2 ,test_type, thresholds,title):

    dataset1_results = pd.read_csv("Tests/"+dataset1+"_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)
    dataset2_results = pd.read_csv("Tests/"+dataset2+"_tests/test_" + test_type + ".csv", delimiter=' ', skiprows=0, low_memory=False)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    ax1.plot(range(thresholds), dataset1_results[dataset1_results.columns[1]], label=dataset1)
    ax1.plot(range(thresholds), dataset2_results[dataset2_results.columns[1]], label=dataset2)
    
    ax1.set_title(title)
    ax1.set_xlabel(dataset1_results.columns[0])
    ax1.set_ylabel(dataset1_results.columns[1])
    ax1.legend( loc= 'upper left')
    fig1.show()