import pygame
import numpy as np

state_init = (100, 100) # state_init allows us to see which cells are virus, antivirus, computer/background
cell_size = 5 # whatever game of life cells that are created, they will have 5 pixels to properly be seen

red_color = (255, 0, 0) # virus
black_color = (0, 0, 0) # background / computer

green_color = (0, 255, 0) # computer part
purple_color = (128, 0, 128) # computer part
yellow_color = (255, 255, 0) # computer part

pygame.init() # initialize pygame so that the simulation can start properly

# Window related settings
width = state_init[0] * cell_size # making the width to fit the 5 pixel cells and which state their in
height = state_init[1] * cell_size # making the height to fit the 5 pixel cells and which state their in
clock = pygame.time.Clock() # this clock allows us to control the frames per second for the simulation

window = pygame.display.set_mode((width, height)) # creates the window
pygame.display.set_caption("Virus/Malware Within A Computer Simulator") # caption for the window

# since we are done with the setting up, now it's generating the cells and initializing it to 0
state = np.zeros(state_init)
for i in range(state_init[0]):
    for j in range(state_init[1]):
        if (np.random.random() < 0.2):
            state[i][j] = 1

def state_update_rules():
    global state
    new_state = np.zeros(state_init)
    for i in range(state_init[0]):
        for j in range(state_init[1]):
            neighbor_virus_cells = state[max(0, i - 1):min(state_init[0], i + 2), max(0, j - 1):min(state_init[1], j + 2)]
            virus_cells_alive = int(np.sum(neighbor_virus_cells)) - int(state[i][j])
            if (state[i][j] == 0 and virus_cells_alive == 3):
                new_state[i][j] = 1
            elif (state[i][j] == 1 and (virus_cells_alive == 2 or virus_cells_alive == 3)):
                new_state[i][j] = 1
            elif (state[i][j] == 1 and virus_cells_alive >= 4):
                new_state[i][j] = -1
    state = state + new_state
    state = np.clip(state, 0, 1)

def state_drawing():
    window.fill(black_color)
    pygame.draw.rect(window, purple_color, (10, 30, 100, 70))
    pygame.draw.rect(window, purple_color, (99, 30, 50, 70))
    for i in range(state_init[0]):
        for j in range(state_init[1]):
            if (state[i][j] == 1):
                pygame.draw.rect(window, red_color, (i * cell_size, j * cell_size, cell_size, cell_size))

# thie while loop block of code is so that the "game" or simulation can actually run and execute the program
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            quit()

    state_update_rules()
    state_drawing()
    pygame.display.flip()
    clock.tick(10)