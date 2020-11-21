import random


def add_frontier(x, y, graph, frontier=None):
    """
    Adds the vertices adjacent to (x, y) in graph to frontier and returns it, if it is a unique element
    """
    def add_frontier_N():
        if 0 <= y - 1 < len(graph[0]) and not graph[0][y - 1][x] and (x, y - 1) not in frontier:
            frontier.append((x, y - 1))
        return frontier

    def add_frontier_S():
        if 0 <= y + 1 < len(graph[0]) and not graph[0][y + 1][x] and (x, y + 1) not in frontier:
            frontier.append((x, y + 1))
        return frontier

    def add_frontier_W():
        if 0 <= x - 1 < len(graph[0][0]) and not graph[0][y][x - 1] and (x - 1, y) not in frontier:
            frontier.append((x - 1, y))
        return frontier

    def add_frontier_E():
        if 0 <= x + 1 < len(graph[0][0]) and not graph[0][y][x + 1] and (x + 1, y) not in frontier:
            frontier.append((x + 1, y))
        return frontier

    if frontier is None or type(frontier) is not list:
        frontier = []

    add_frontier_N()
    add_frontier_S()
    add_frontier_W()
    add_frontier_E()

    return frontier


def adjacent(x, y, graph):
    """
    Returns a list with all points adjacent to the vertex at (x, y)
    """
    return [(x + dx, y + dy) for dx, dy in zip((-1, 1, 0, 0), (0, 0, -1, 1)) if 0 <= x + dx < len(graph[0][0]) and 0 <= y + dy < len(graph[0])]


def visit(x, y, graph):
    """
    Sets the vertex (x, y) in graph to be visited (True)
    """
    graph[0][y][x] = True


def gen_prim_maze(dim=None):
    """
    Generate a maze with a list of vertices of a graph using a variation of Prim's Algorithm
    Assumes dim is None (size of maze is 1x1) or an int or a 2-tuple giving both width and height of a maze to generate
    """
    if dim is None:
        dim = 1
    if type(dim) is (int):
        dim = dim, dim

    # Initialize (V, E) of the graph where all vertices are False
    graph = [[False] * dim[0] for _ in range(dim[1])], []

    # Select a random vertex and visits it (True)
    x0, y0 = random.randrange(len(graph[0][0])), random.randrange(len(graph[0]))
    visit(x0, y0, graph)

    # Add the 'frontier' vertices; adjacent vertices that are not visited and not yet added
    frontier = add_frontier(x0, y0, graph)

    # Choose random pt, add adjacent to possibilities
    # Perform this to all vertices, note the -1 due to the initial vertex above
    for _ in range(dim[0] * dim[1] - 1):
        to_x, to_y = random.choice(frontier)
        frontier.remove((to_x, to_y))

        visit(to_x, to_y, graph)
        add_frontier(to_x, to_y, graph, frontier)

        # sources = [pos for pos in adjacent(to_x, to_y, graph) if graph[0][pos[1]][pos[0]]]
        sources = list(filter(lambda pos: graph[0][pos[1]][pos[0]], adjacent(to_x, to_y, graph)))
        from_x, from_y = random.choice(sources)

        # Edges are from left to right and downwards
        if to_x < from_x or to_y < from_y:
            graph[1].append(((to_x, to_y), (from_x, from_y)))
        else:
            graph[1].append(((from_x, from_y), (to_x, to_y)))
    return graph
