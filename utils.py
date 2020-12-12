import copy
import pygame
from patterns import patternDict
from random import randrange

white = (255, 255, 255)
black = (0, 0, 0)
rowNr = 31
colNr = 38
cellSize = 50


def init(pygame, gameGrid, cellSize): 
    pygame.init()
    pygame.display.set_caption("Conway's Game Of Life")
    global rowNr
    global colNr
    rowNr = len(gameGrid)
    colNr = len(gameGrid[0])
    win = pygame.display.set_mode((colNr*cellSize, rowNr*cellSize))
    return win

#Recieves list of key presses to check for
def checkInputs(pygame, options):
    # check mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONUP:
            return pygame.mouse.get_pos()

        if event.type == pygame.KEYDOWN:
            if event.key in options:
                return event.key

def isValidPos(row, col):
    return row >= 0 and row < rowNr and col >= 0 and col < colNr

def neighbourSum(grid, row, col):
    sum = 0
    if grid[row][col] == 1:
        sum -= 1

    for deltaRow in range(-1, 2):
        for deltaCol in range(-1, 2):
            if isValidPos(row + deltaRow, col + deltaCol):
                sum += grid[row + deltaRow][col + deltaCol]
    return sum


def nextStatus(grid, row, col):
    sum = neighbourSum(grid, row, col)

    if grid[row][col] == 1:
        if sum == 2 or sum == 3:
            return 1
        else:
            return 0
    if grid[row][col] == 0:
        if sum == 3:
            return 1
        else:
            return 0
 
def updateGrid(grid):
    newGrid = copy.deepcopy(grid)
    for row in range (0, rowNr):
        for col in range(0, colNr):
            newGrid[row][col] = nextStatus(grid, row, col)
    return newGrid

def updateScreen(gameGrid, win):
    for row in range (0, rowNr):
        for col in range(0, colNr):
            if gameGrid[row][col] == 1:
                pygame.draw.rect(win, black, pygame.Rect(col*cellSize, row*cellSize, cellSize, cellSize))
            else:
                pygame.draw.rect(win, white, pygame.Rect(col*cellSize, row*cellSize, cellSize, cellSize))

    pygame.display.flip()


def getUserInput(gameGrid):
    while (True):
        print("Which pattern would you like to see?")

        for key in patternDict:
            print(" - {}".format(key))

        print(" - random")
        pattern = input("Option: ")

        if pattern in patternDict:
            gameGrid = patternDict[pattern]
            return gameGrid

        elif pattern == "random" or pattern == "Random":
            for i in range(0, 50):
                gameGrid.append([])
                for j in range(0, 50):
                    gameGrid[i].append(randrange(2))
            return gameGrid
            
        else:
            print("That isn't an available pattern!")
    