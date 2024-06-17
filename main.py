import pygame
from random import randint, uniform

pygame.display.set_caption('Sand Simulator')
width = height = 700
w = 10
cols = width // w + 1
rows = height // w + 1
clock = pygame.time.Clock()
hueValue = 200

def make2DGrid(cols, rows):
    array = [[0 for i in range(cols)] for j in range(rows)]
    return array


grid = make2DGrid(cols, rows)


def redraw(window):
    window.fill((240, 240, 240))

    for i in range(cols):
        for j in range(rows):
            if grid[i][j] > 0:
                color = pygame.Color(194, 178, 128)
                h, s, v, a = color.hsva
                color.hsva = (h, s, v, a)
                pygame.draw.rect(window, color, pygame.Rect(i*w, j*w, w, w))
    nextGrid = make2DGrid(cols, rows)

    for i in range(cols):
        for j in range(rows):
            state = grid[i][j]
            if state > 0:
                below = grid[i][j + 1]
                dir = 1
                if uniform(0, 1) < 0.5:
                    dir *= - 1
                belowA = belowB = None
                if 0 <= i + dir <= cols-1:
                    belowA = grid[i + dir][j + 1]
                if 0 <= i - dir <= cols - 1:
                    belowB = grid[i - dir][j + 1]

                if below == 0 and j < rows - 2:
                    nextGrid[i][j] = 0
                    nextGrid[i][j + 1] = grid[i][j]
                elif belowA == 0 and j < rows - 2:
                    nextGrid[i + dir][j+1] = grid[i][j]
                elif belowB == 0 and j < rows - 2:
                    nextGrid[i - dir][j+1] = grid[i][j]
                else:
                    nextGrid[i][j] = 1

    for i in range(cols):
        for j in range(rows):
            grid[i][j] = nextGrid[i][j]

    pygame.display.update()
    clock.tick(30)

def main():

    window = pygame.display.set_mode((width, height))
    play = True

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            mousecol = x // w + 1
            mouserow = y // w + 1
            matrix = 5
            extent = matrix // 2
            for i in range(-extent, extent):
                for j in range(-extent, extent):
                    if uniform(0, 1) < 0.75:
                        col = mousecol + i
                        row = mouserow + j
                        if 0 <= col <= cols - 1 and 0 <= row <= rows - 1:
                            grid[col][row] = hueValue


        redraw(window)


main()
