import matplotlib.pyplot as plt

def create_graph(results,thresholds,title):
    plt.figure(figsize=(12,8))
    plt.plot(range(thresholds), results[results.columns[1]])
    plt.ylabel(results.columns[1])
    plt.xlabel(results.columns[0])
    plt.title(title)
    plt.show()