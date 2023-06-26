import networkx as nx
import matplotlib.pyplot as plt
import Algo
import time

from CSP.solver import backtrack, backtrack_AC_3
from Graph import graph as g
from Graph import graph_distance as gd
from Graph.grid import Grid
from CSP import Csp

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

    #
    gdd = gd.graph2

    isFoundIDS_Not_uniform_cost = Algo.ids_not_uniformed_cost(gdd, "A", "F")
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

    # use grid data struct
    start = (0, 0)
    target = (4, 4)
    obstacles = {(2, 2), (3, 2), (2, 3), (3, 3)}
    grid = Grid(5, 5, obstacles)

    print(Algo.a_star_search(grid, start, target))
    print(Algo.a_star_search(grid, start, (4, 3)))

    # CSP starts ------------------------------------------------------------------------------------------------------
    print("\n Simple CSP: \n")

    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    colors = ['red', 'green', 'blue',]
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }
    csp = Csp.MapColoringCSP(regions, colors, neighbors)

    # Call basic backtrack
    assignment = {}
    result = backtrack(assignment, csp)
    print(result)

    # Call AC-3 backtrack
    csp = Csp.MapColoringCSP(regions, colors, neighbors)
    assignment = {}
    result = backtrack_AC_3(assignment, csp)
    print(result)



