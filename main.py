from utils import *
import pygame
gameGrid = []

gameGrid = getUserInput(gameGrid)

win = init(pygame, gameGrid, cellSize)

while True:
    pygame.time.wait(100)
    gameGrid = updateGrid(gameGrid)
    updateScreen(gameGrid, win)

    if checkInputs(pygame, [pygame.K_n, pygame.K_q]) == pygame.K_q:
        pygame.quit()
        quit()