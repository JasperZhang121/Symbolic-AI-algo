import networkx as nx
import matplotlib.pyplot as plt

from Graph import graph as g
from Graph import graph_distance as gd

import Algo

if __name__ == '__main__':
    # visualize graph for testing algo
    g = g.graph3
    G = nx.DiGraph(g)
    # draw the graph
    nx.draw(G, with_labels=True)
    plt.show()

    # Search algorithms: default from A to D

    # BFS
    isFoundBFS = Algo.breadth_first_search(g, "A", "T")
    print(isFoundBFS)

    # DFS
    isFoundDFS = Algo.depth_first_search(g, "A", "T")
    print(isFoundDFS)

    # IDS
    isFoundIDS = Algo.iterative_deepening_search(g, "A", "T")
    print(isFoundDFS)

    # Graph with distance ----------------------------------------------------------------------------------------------

    # Uniform-Cost Search
    gd = gd.graph3
    G = nx.DiGraph(gd)
    # draw the graph
    nx.draw(G, with_labels=True)
    plt.show()

    isFoundUniform = Algo.uniform_cost(gd)
    print(isFoundUniform)
