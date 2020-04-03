from utils import *
from patterns import gosper, pulsar
import pygame
gameGrid = pulsar
win = init(pygame, gameGrid)

white = (255, 255, 255)
black = (0, 0, 0)
cellSize = 60

rowNr = len(gameGrid)
colNr = len(gameGrid[0])

def updateScreen():
    for row in range (0, rowNr):
        for col in range(0, colNr):
            if gameGrid[row][col] == 1:
                pygame.draw.rect(win, black, pygame.Rect(col*cellSize + 50, row*cellSize + 50, cellSize, cellSize))
            else:
                pygame.draw.rect(win, white, pygame.Rect(col*cellSize + 50, row*cellSize + 50, cellSize, cellSize))

    pygame.display.flip()

updateScreen()


while True:
    pygame.time.wait(200)
    gameGrid = updateGrid(gameGrid)
    updateScreen()

    if checkInputs(pygame, [pygame.K_n, pygame.K_q]) == pygame.K_q:
        pygame.quit()
        quit()