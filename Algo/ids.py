def iterative_deepening_search(graph, start_node="A", end_node="D"):
    """
    Perform an iterative deepening search on a graph.

    Args:
        graph (dict): A dictionary representing the graph, with node names as keys and lists of neighbor nodes as values.
        start_node (str, optional): The node to start the search from. Defaults to "A".
        end_node (str, optional): The node to search for. Defaults to "D".

    Returns:
        bool: True if the target node is found, False otherwise.

    Prints:
        str: If the target node is found, prints the path taken to reach it, along with the depth of the node.

    """
    limit, depth = 100, 0

    while depth < limit:

        stack, visited = [(start_node, [start_node], 0)], set()
        while stack:
            cur, move, current_depth = stack.pop()
            if cur == end_node:
                path = "->".join(move)
                print(f"IDS found {end_node} at depth {current_depth}, path is {path}")
                return True
            if depth == current_depth:
                break
            successors = graph[cur]

            for x in successors:
                if x not in visited:
                    visited.add(x)
                    temp = move.copy()
                    temp.append(x)
                    stack.append((x, temp, current_depth+1))
        depth += 1

    print("Cannot find the target")
    return False

def ids_not_uniformed_cost(graph, start_node="A", end_node="D"):
    """
    Find a path from the start node to the end node in a graph using iterative deepening search.

    Args:
    - graph (dict): A dictionary representing the graph, where the keys are node labels and the values are dictionaries
                    of neighbor nodes and their corresponding edge costs.
    - start_node (str): The label of the starting node. Default is "A".
    - end_node (str): The label of the target node. Default is "D".

    Returns:
    - True if a path from start_node to end_node is found, False otherwise.

    This function implements iterative deepening search (IDS) to find a path from the start node to the end node in a graph.
    The search starts at the root node (specified by start_node) and explores the graph in a depth-first manner up to a
    certain depth limit. If the target node (specified by end_node) is found, the function returns True and prints the
    path from start_node to end_node. If the target node is not found within the depth limit, the function returns False.
    """

    limit, depth = 100, 0

    while depth < limit:

        stack, visited = [(start_node, [start_node], 0)], {start_node:0}
        while stack:
            cur, move, current_cost = stack.pop()
            if cur == end_node:
                path = "->".join(move)
                print(f"IDS_not_uniformed-cost found {end_node} at cost {current_cost}, path is {path}")
                return True
            if depth == current_cost:
                break
            successors = graph[cur]

            for x in successors:
                new_cost = current_cost + int(graph[cur][x])
                if x not in visited or new_cost < visited[x]:
                    visited[x] = new_cost
                    temp = move.copy()
                    temp.append(x)
                    stack.append((x, temp, new_cost))
        depth += 1

    print("Cannot find the target")
    return False
