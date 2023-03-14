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