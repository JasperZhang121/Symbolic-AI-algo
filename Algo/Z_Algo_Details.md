# Algorithm details

## Breadth First Search

BFS (Breadth-First Search) is a graph traversal algorithm that visits all the vertices of a graph in breadth-first order. The algorithm starts at the root node and explores all the neighboring nodes at the current depth level before moving on to the next depth level. BFS is guaranteed to find the shortest path between the starting node and any other reachable node.

When applying BFS on a tree, the algorithm visits all the nodes in a level before proceeding to the next level. The algorithm starts at the root node and explores its children nodes. It then proceeds to explore the children of the first level nodes in a left-to-right order, and so on. The order in which the nodes are visited is from left to right, level by level. The algorithm keeps track of the visited nodes to avoid infinite looping.

When applying BFS on a graph, the algorithm first visits the starting node, and then explores all its neighboring nodes. After that, it moves on to the neighboring nodes and explores their neighboring nodes. BFS can be visualized as a wave emanating from the starting node and expanding in all directions, level by level. The algorithm keeps track of the visited nodes to avoid revisiting them.

Here is an example of how BFS explores nodes in a tree:

```commandline
           A
         /   \
        B     C
       / \   / \
      D   E F   G
```

The order in which the nodes are visited using BFS is: A, B, C, D, E, F, G. The algorithm starts at node A, visits its children nodes B and C, then proceeds to visit the children nodes of B, which are D and E. After that, it moves on to the children nodes of C, which are F and G. The order in which the nodes are visited is from left to right, level by level.

Here is an example of how BFS explores nodes in a graph:

```commandline
     A -- B -- C
     |    |    |
     D -- E -- F
```
If we start BFS at node A, the order in which the nodes are visited is: A, B, D, E, C, F. The algorithm starts at node A, visits its neighboring nodes B and D. After that, it moves on to node B and visits its neighboring nodes E and C. Then it moves on to node D and visits its neighboring node E. Finally, it moves on to node E and visits its neighboring node F. The algorithm keeps track of the visited nodes to avoid revisiting them.

---

## Depth First Search

DFS stands for Depth First Search. It is another algorithm used for traversing or searching a tree or graph data structure. Unlike BFS, which explores all the neighboring nodes of a particular node before moving on to the next level of nodes, DFS explores as far as possible along each branch before backtracking.

Let's say we have the following graph:

```commandline
    A
   / \
  B   C
 / \   \
D   E   F
```

Here's how DFS works on this graph:

Start at node A and mark it as visited.
Move to one of its unvisited neighbors, such as B, and mark it as visited.
Move to one of B's unvisited neighbors, such as D, and mark it as visited.
Since D has no unvisited neighbors, backtrack to B and visit its other unvisited neighbor, E.
Since E has no unvisited neighbors, backtrack to A and visit its other unvisited neighbor, C.
Move to C's unvisited neighbor, F, and mark it as visited.
Since F has no unvisited neighbors, backtrack to C and then to A.
Since all nodes are visited, the search is complete. (A -> B -> D -> E -> C -> F)

---

## Iterative deepening Search

Iterative deepening is an algorithm that combines the benefits of both BFS and DFS. It runs DFS with a gradually increasing depth limit until the goal node is found.

```commandline
          A
         / \
        B   C
       / \   \
      D   E   F
```

Let's say we want to search for a path from node A to node F.

Start with depth limit 0, and perform a DFS search from node A, which will result in failure.
Increase the depth limit to 1, and perform a DFS search from node A, which will expand node B and C. As F is not found yet, we continue searching by performing a DFS search from node B, which will expand node D and E. The search from node C is also performed, but it only expands node F, which is the goal node, so we return the path from A to F.
If the goal node is not found at the current depth limit, we increase the limit to 2, and repeat the process. This time, the search from node A will expand nodes B, C, D, E, and F. The search from node B will expand nodes D and E, and the search from node C will expand node F. The search from node D and E will not expand any node. Since the goal node is found in the search from node C, we return the path from A to F.
We continue this process, increasing the depth limit until the goal node is found.
The node expand order for the example above by iterative deepening is:

```commandline
Depth limit 0: A
Depth limit 1: A, B, C
Depth limit 2: A, B, C, D, E, F
```

---

Uniform-cost search is a variant of Dijkstra's algorithm, where instead of maintaining a visited set, we maintain a priority queue of nodes to be explored in order of their path costs.

Let's say we have the following graph:

```commandline
       A
     /   \
    B     C
   / \     \
  D   E     F
 /         / \
G         H   I
```

The numbers next to each node indicate the cost to reach that node from the start node.

```commandline
       A:0
     /   \
  B:1     C:1
   / \     \
D:2   E:3   F:4
 /         / \
G:5       H:6 I:7
```

The queue is initially populated with the start node A. The nodes are expanded in the following order:

A (cost 0)
B (cost 1)
C (cost 1)
D (cost 2)
E (cost 3)
F (cost 4)
G (cost 5)
H (cost 6)
I (cost 7)

Priority Queue status: 


    


The optimal path from A to I is A -> C -> F -> I, which has a cost of 7.



