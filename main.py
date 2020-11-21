import sys
import pygame
import scmaze
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 30  # refresh rate of pygame screen
STROKE_WIDTH = 5  # line width, in pixels
# GRID_DIM = (16, 12)  # number of tiles width and height-wise
GRID_DIM = (80, 60)

# screen dimensions, in pixels
WIDTH = 800
HEIGHT = 600

WINDOW_TITLE = 'Maze Generator - SC'


def draw_grid(screen, graph, stroke_width=max(1, STROKE_WIDTH)):
    """
    Draw all edges of a grid with the same size as given by 2-dimensional list graph[0],
    excluding the edges in graph[1]
    The width of each line is stroke_width, and the grid is scaled to fill the window
    while keeping all tiles square
    """
    # # Make stroke width the same as path width regardless of size
    # stroke_width = min(WIDTH // len(graph[0][0]), HEIGHT // len(graph[0])) // 2

    # Gets min size of square tiles, depending on which will fit in the window
    dim = min((WIDTH - stroke_width) / len(graph[0][0]), (HEIGHT - stroke_width) / len(graph[0]))

    # Offset to align strokes inside window when strokes are large
    offset = (stroke_width - 1) // 2

    # Length of each stroke
    # Usually greater than dim to include caps at the end of the line
    length = dim + stroke_width - 1

    # Draw bounding rectangle around grid
    board_rect_width = int(len(graph[0][0]) * dim + stroke_width)
    board_rect_height = int(len(graph[0]) * dim + stroke_width)
    pygame.draw.rect(screen, BLACK, (0, 0, board_rect_width, board_rect_height), stroke_width, 1)

    # Draw all grid lines/maze walls
    for y in range(len(graph[0])):
        for x in range(len(graph[0][0])):
            if y < len(graph[0]) - 1 and ((x, y), (x, y + 1)) not in graph[1]:
                # draw horizontal line if it is not on the bottom border and which should be drawn
                start_horiz = x * dim, (y + 1) * dim + offset
                end_horiz = start_horiz[0] + length, start_horiz[1]
                pygame.draw.line(screen, BLACK, start_horiz, end_horiz, stroke_width)
            if x < len(graph[0][0]) - 1 and ((x, y), (x + 1, y)) not in graph[1]:
                # draw vertical line if it is not on the right border and which should be drawn
                start_vert = (x + 1) * dim + offset, y * dim
                end_vert = start_vert[0], start_vert[1] + length
                pygame.draw.line(screen, BLACK, start_vert, end_vert, stroke_width)
    return graph


def main():
    # initaialize pygame
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    clock = pygame.time.Clock()
    screen.fill(WHITE)
    pygame.display.update()

    graph = scmaze.gen_prim_maze(GRID_DIM)
    running = True
    while running:
        t1 = 0
        # keep running at the right speed
        clock.tick(FPS)
        # process input (events)
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # create new maze on left click
                graph = scmaze.gen_prim_maze(GRID_DIM)
        screen.fill(WHITE)
        t1 = time.time_ns()
        draw_grid(screen, graph)
        if t1:
            print(f'{time.time_ns() - t1}ns = {(time.time_ns() - t1) / 1e3}us = {(time.time_ns() - t1) / 1e6}ms = {(time.time_ns() - t1) / 1e9}s time to draw')
        pygame.display.update()

    pygame.quit()
    sys.exit(0)


main()
