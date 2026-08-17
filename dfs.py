def dfs(graph, start):
    """Depth-first search over an adjacency-list graph.

    `graph` maps a vertex to the list of its neighbours, e.g.
    {"a": ["b"], "b": ["c"], "c": []}.

    Returns the vertices reachable from `start` in DFS pre-order,
    each exactly once. Iterative (explicit stack), so graphs with
    cycles are traversed without infinite recursion.
    """
    visited = []
    seen = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        visited.append(vertex)
        for neighbour in reversed(graph.get(vertex, [])):
            if neighbour not in seen:
                stack.append(neighbour)

    return visited
