from queue import PriorityQueue


def uniform_cost(graph, start_node="A", end_node="D"):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start_node, [start_node]))

    while not pq.empty():
        cost, node, path = pq.get()

        if node == end_node:
            print("Uniform_cost found the shortest path: ", '->'.join(path))
            return True

        if node in visited:
            continue
        visited.add(node)

        for neighbor, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_path = path + [neighbor]
            pq.put((new_cost, neighbor, new_path))

    return False
