import random
from colorama import Fore, Style, init

init()


width = 5
height = 5
dead = 0
alive = 1
possible_states = [dead,alive]
board_state = []

def dead_state(width,height):
    for i in  range(width):
        board_state.append([dead for j in range(height)])
    return board_state
def random_state(width,height):
    for i in  range(width):
        board_state.append([random.choice(possible_states) for j in range(height)])
    return board_state
def render(board_state):
    # Loop over each row in the board state
    for row in board_state:
        # Convert each cell in the row to a character and join them with a space
        row_str = ""
        for cell in row:
            if cell == alive:
                row_str += Fore.BLUE + '#' + Style.RESET_ALL
            else:
                row_str += Fore.RED + '#' + Style.RESET_ALL
        # Add borders and print the row
        print(f"|{row_str}|")

random_board = random_state(width, height)
#print(dead_state(width, height))
render(random_board)