from utils import *
from patterns import gosper, pulsar, simkin
import pygame
from random import randrange
gameGrid = pulsar

# for i in range(0, 500):
#     gameGrid.append([])
#     for j in range(0, 500):
#         gameGrid[i].append(randrange(2))
cellSize = 50
win = init(pygame, gameGrid, cellSize)

white = (255, 255, 255)
black = (0, 0, 0)

rowNr = len(gameGrid)
colNr = len(gameGrid[0])

def updateScreen():
    for row in range (0, rowNr):
        for col in range(0, colNr):
            if gameGrid[row][col] == 1:
                pygame.draw.rect(win, black, pygame.Rect(col*cellSize, row*cellSize, cellSize, cellSize))
            else:
                pygame.draw.rect(win, white, pygame.Rect(col*cellSize, row*cellSize, cellSize, cellSize))

    pygame.display.flip()

updateScreen()


while True:
    pygame.time.wait(100)
    gameGrid = updateGrid(gameGrid)
    updateScreen()

    if checkInputs(pygame, [pygame.K_n, pygame.K_q]) == pygame.K_q:
        pygame.quit()
        quit()