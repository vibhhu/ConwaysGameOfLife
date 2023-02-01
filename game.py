import copy
import pygame

# NUM_ROWS, NUM_COLUMNS = 60, 50
# BOX_WIDTH, BOX_HEIGHT, SPACING = 10, 10, 1

NUM_ROWS, NUM_COLUMNS = 320, 270
BOX_WIDTH, BOX_HEIGHT, SPACING = 2, 2, 0

BLACK, DEAD, ALIVE = (0, 0, 0), (255, 255, 255), (50, 50, 50)
WINDOW_DIMENSIONS = [555, 670]

board = [[0 for _ in range(NUM_COLUMNS)] for _ in range(NUM_ROWS)]
newBoard = copy.deepcopy(board)


# BLOCK
board[NUM_ROWS // 2][NUM_COLUMNS // 2] = 1
board[NUM_ROWS // 2 - 1][NUM_COLUMNS // 2] = 1
board[NUM_ROWS // 2][NUM_COLUMNS // 2 - 1] = 1
board[NUM_ROWS // 2 - 1][NUM_COLUMNS // 2 - 1] = 1


pygame.init()
window = pygame.display.set_mode(WINDOW_DIMENSIONS)
pygame.display.set_caption("The Game of Life")

def display_board():
    clock = pygame.time.Clock()
    for y in range(NUM_ROWS):
        for x in range(NUM_COLUMNS):
            state = ALIVE if board[y][x] == 1 else DEAD
            pygame.draw.rect(window, state, [(x + 1) * SPACING + BOX_WIDTH * x, (y + 1) * SPACING + BOX_HEIGHT * y, BOX_HEIGHT, BOX_HEIGHT]) 
    pygame.display.flip()
    clock.tick(100)


def click_handler():
    x, y = pygame.mouse.get_pos()
    x, y = x // (BOX_WIDTH + SPACING), y // (BOX_HEIGHT + SPACING)
    board[y][x] = 1 if board[y][x] == 0 else 0

def event_handler():
    finished = False
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_handler()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    finished = True
                       
                if event.key == pygame.K_x: 
                    global board 
                    board = [[0 for _ in range(NUM_COLUMNS)] for _ in range(NUM_ROWS)]
                    initialize_board()   
    return finished                
        
def initialize_board():
    finished = False
    while not finished:
        window.fill(BLACK)
        finished = event_handler()
        display_board()                         


def run_simulation():
    global board
    finished = False
    while not finished:
        for y in range(NUM_ROWS):
            for x in range(NUM_COLUMNS):
                # dummy condition to preserve if-else structure to switch between game variations
                if (0 == 1):
                    print('')
                
                # Secret sauce
                if y + 1 < NUM_ROWS and board[y + 1][x] == 1:
                    newBoard[y][x] = 1 

                
                # # wrapping
                elif y == NUM_ROWS - 1:
                    newBoard[y][x] = board[0][x] 

                else:        
                    neighbors = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if not (dx == 0 and dy == 0): 
                                # wrapping
                                if board[((y + dy) % NUM_ROWS)][((x + dx) % NUM_COLUMNS)] == 1:
                                    neighbors += 1
                    if board[y][x] == 1:
                        newBoard[y][x] = 1 if neighbors in range(2, 4) else 0
                    if board[y][x] == 0:
                        newBoard[y][x] = 1 if neighbors == 3 else 0
                    
        board = copy.deepcopy(newBoard)
        display_board()
        
        finished = event_handler()
                               
initialize_board()
run_simulation()
pygame.quit()
	