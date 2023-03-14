import networkx as nx
import matplotlib.pyplot as plt

import graph as g
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
