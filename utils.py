import copy
rowNr = 31
colNr = 38

def init(pygame, gameGrid): 
    pygame.init()
    pygame.display.set_caption("Conway's Game Of Life")
    win = pygame.display.set_mode((1800, 1800))
    global rowNr
    global colNr
    rowNr = len(gameGrid)
    colNr = len(gameGrid[0])
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
