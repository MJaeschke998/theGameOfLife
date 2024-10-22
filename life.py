import pygame
import random
import time
from colorama import Fore, Style, init
#initialize pygame
pygame.init()

#constants for the game
width = 50
height = 50
cell_size = 20
dead = 0
alive = 1
possible_states = [dead,alive]
board_state = []

# Colors for alive and dead cells
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
base_board_state = [
    [1,1,1,0,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,0,0,0,0],
    [1,0,0,1,1]
]

# Create a Pygame window
screen = pygame.display.set_mode((width * cell_size, height * cell_size))
pygame.display.set_caption("Conway's Game of Life")


def count_live_neighbors(board, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    live_neighbors = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        # Check if neighbor is within bounds
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            live_neighbors += board[nx][ny]
    return live_neighbors

def dead_state(width,height):
    for i in  range(width):
        board_state.append([dead for j in range(height)])
    return board_state


def random_state(width,height):
    for i in  range(width):
        board_state.append([random.choice(possible_states) for j in range(height)])
    return board_state

def next_board_state(board):
    new_board = [[dead for j in range(len(board[0]))] for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            live_neighbors = count_live_neighbors(board, i, j)
            if board[i][j] == alive:
                # Rule 1 and 3: Underpopulation or Overpopulation
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[i][j] = dead
                # Rule 2: Survival
                else:
                    new_board[i][j] = alive
            else:
                # Rule 4: Reproduction
                if live_neighbors == 3:
                    new_board[i][j] = alive
    return new_board

def render(board_state):
    # Loop over each row in the board state
    for i,  row in enumerate(board_state):
        for j, cell in enumerate(row):
            x = j * cell_size
            y = i * cell_size
            color = BLUE if cell == alive else RED
            pygame.draw.rect(screen, color, pygame.Rect(x,y,cell_size,cell_size))
    pygame.display.flip()



def run_forever(init_state):
    """Runs the Game of Life forever, starting from the given initial state.
    Parameters
    ----------
    init_state: the Game state to start at
    Returns
    -------
    This function never returns - the program must be forcibly exited!
    """
    next_state = init_state
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            screen.fill(BLACK)  # Fill the screen with black before rendering the new state
            render(next_state)
            next_state = next_board_state(next_state)
            time.sleep(0.03)

if __name__ == "__main__":
    init_state = random_state(width,height)
    run_forever(init_state)