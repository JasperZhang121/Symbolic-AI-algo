def depth_first_search(graph, start_node="A", end_node="D"):
    """
    Perform a depth-first search on a graph.

    Args:
        graph (dict): A dictionary representing the graph, with node names as keys and lists of neighbor nodes as values.
        start_node (str, optional): The node to start the search from. Defaults to "A".
        end_node (str, optional): The node to search for. Defaults to "D".

    Returns:
        bool: True if the target node is found, False otherwise.

    Prints:
        str: If the target node is found, prints the path taken to reach it, along with the depth of the node.

    """
    frontier, discovered = [(start_node, [start_node], 0)], {start_node}

    while frontier:
        current, move, depth = frontier.pop()
        if current == end_node:
            path = "->".join(move)
            print(f"DFS: found {end_node} at depth {depth}, the path taken is: {path}")
            return True
        for neighbor in graph[current]:
            if neighbor not in discovered:
                temp = move.copy()
                temp.append(neighbor)
                frontier.append((neighbor, temp, depth + 1))
                discovered.add(neighbor)

    print(f"DFS: {end_node} not found")
    return False
