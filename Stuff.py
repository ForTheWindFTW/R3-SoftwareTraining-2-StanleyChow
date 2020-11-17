import sys
import pygame
import scmaze

WIDTH = 800
HEIGHT = 400
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
X_OFFSET = 0
Y_OFFSET = 0


# ##########
# #  #     #
# #  ####  #
# #        #
# #  #  #  #
# #  #  #  #
# ##########


def draw_grid(graph, stroke_width=1):
    # graph = ([[True, True, True], [True, True, True], [True, True, True]], [((0, 1), (1, 1)), ((0, 0), (0, 1)), ((0, 1), (0, 2)), ((1, 1), (1, 2)), ((1, 1), (2, 1)), ((2, 0), (2, 1)), ((2, 1), (2, 2)), ((1, 0), (2, 0))])

    dim = min((WIDTH - stroke_width) / len(graph[0][0]), (HEIGHT - stroke_width) / len(graph[0]))
    offset = (stroke_width - 1) // 2
    length = dim + stroke_width - 1

    pygame.draw.rect(screen, BLACK, (0, 0, len(graph[0][0]) * dim + stroke_width, len(graph[0]) * dim + stroke_width), stroke_width, 1)
    for y in range(len(graph[0])):
        for x in range(len(graph[0][0])):
            if y < len(graph[0]) - 1 and ((x, y), (x, y + 1)) not in graph[1]:
                # print(f'V x{x}y{y} to x{x}y{y+1}')
                start_horiz = x * dim, (y + 1) * dim + offset
                end_horiz = start_horiz[0] + length, start_horiz[1]
                pygame.draw.line(screen, BLACK, start_horiz, end_horiz, stroke_width)
                # print('horiz line')
            if x < len(graph[0][0]) - 1 and ((x, y), (x + 1, y)) not in graph[1]:
                # print(f'V x{x}y{y} to x{x+1}y{y}')
                start_vert = (x + 1) * dim + offset, y * dim
                end_vert = start_vert[0], start_vert[1] + length
                pygame.draw.line(screen, BLACK, start_vert, end_vert, stroke_width)
                # print('vert line')
    return graph


# initaialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Grid')
clock = pygame.time.Clock()
screen.fill(WHITE)
pygame.display.update()

graph = scmaze.gen_prim_maze(30)
running = True
while running:
    # keep running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            graph = scmaze.gen_prim_maze((20, 30))
            screen.fill(WHITE)
            draw_grid(graph, 5)
            pygame.display.update()
    # screen.fill(WHITE)
    # draw_grid(graph, 10)
    # pygame.display.update()

pygame.quit()
sys.exit(0)
