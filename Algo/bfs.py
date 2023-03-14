def breadth_first_search(graph, start_node="A", end_node="D"):
    """
        Perform a breadth-first search on a graph to find a target node.

        Parameters:
        -----------
        graph : dict
            A dictionary representing the graph, with node names as keys and lists of neighbor nodes as values.
        start_node : str, optional
            The node to start the search from. Default is "A".
        end_node : str, optional
            The node to search for. Default is "D".

        Returns:
        --------
        bool
            True if the target node is found, False otherwise.

        Prints:
        -------
        str
            If the target node is found, prints the path taken to reach it, along with the depth of the node.

        Examples:
        ---------
        >>> graph = {'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}
        >>> breadth_first_search(graph)
        Found D at depth 2, the path taken is: A->C->D
        True
        """

    frontier, discovered, depth = [(start_node, [start_node])], {start_node}, 0

    while frontier:
        current, move = frontier.pop(0)
        if current == end_node:
            path = "->".join(move)
            print(f"BFS: found {end_node} by depth {depth}, the path taken is: {path}")
            return True
        for neighbor in graph[current]:
            if neighbor not in discovered:
                temp = move.copy()
                temp.append(neighbor)
                frontier.append((neighbor, temp))
                discovered.add(neighbor)
        depth += 1

    print("Cannot found the target")
    return False
