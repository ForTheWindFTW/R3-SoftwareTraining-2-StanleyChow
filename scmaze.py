import random


def add_frontier(x, y, verts, frontier=None):
    def add_frontier_N():
        if 0 <= y - 1 < len(verts) and not verts[y - 1][x] and (x, y - 1) not in frontier:
            frontier.append((x, y - 1))
        return frontier

    def add_frontier_S():
        if 0 <= y + 1 < len(verts) and not verts[y + 1][x] and (x, y + 1) not in frontier:
            frontier.append((x, y + 1))
        return frontier

    def add_frontier_W():
        if 0 <= x - 1 < len(verts[0]) and not verts[y][x - 1] and (x - 1, y) not in frontier:
            frontier.append((x - 1, y))
        return frontier

    def add_frontier_E():
        if 0 <= x + 1 < len(verts[0]) and not verts[y][x + 1] and (x + 1, y) not in frontier:
            frontier.append((x + 1, y))
        return frontier

    if frontier is None or type(frontier) is not list:
        frontier = []

    add_frontier_N()
    add_frontier_S()
    add_frontier_W()
    add_frontier_E()

    return frontier


def adjacent(x, y, verts):
    return [(x + dx, y + dy) for dx, dy in zip((-1, 1, 0, 0), (0, 0, -1, 1)) if 0 <= x + dx < len(verts[0]) and 0 <= y + dy < len(verts) and verts[y + dy][x + dx]]


def mark(x, y, verts):
    verts[y][x] = True
    return


def gen_prim_maze(dim=None):
    """
    Generate a maze with a list of vertices of a graph using a variation of Prim's Algorithm
    """
    if dim is None:
        dim = 1
    if type(dim) in (int, float):
        dim = dim, dim

    graph = [[False] * dim[0] for _ in range(dim[1])], []
    x0, y0 = random.randrange(len(graph[0][0])), random.randrange(len(graph[0]))
    mark(x0, y0, graph[0])  # Marks point as visited
    frontier = add_frontier(x0, y0, graph[0])

    # Choose random pt, add adjacent to possibilities
    for _ in range(dim[0] * dim[1] - 1):
        to_x, to_y = random.choice(frontier)
        frontier.remove((to_x, to_y))

        mark(to_x, to_y, graph[0])
        add_frontier(to_x, to_y, graph[0], frontier)

        sources = adjacent(to_x, to_y, graph[0])
        from_x, from_y = sources[random.randrange(len(sources))]

        # Edges are from left to right and downwards
        if to_x < from_x or to_y < from_y:
            graph[1].append(((to_x, to_y), (from_x, from_y)))
        else:
            graph[1].append(((from_x, from_y), (to_x, to_y)))
    return graph
