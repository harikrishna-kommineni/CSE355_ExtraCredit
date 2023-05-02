import pygame
import numpy as np

state_init = (100, 100) # state_init allows us to see which cells are virus, antivirus, computer/background
cell_size = 5 # whatever game of life cells that are created, they will have 5 pixels to properly be seen

red_color = (255, 0, 0) # virus
black_color = (0, 0, 0) # background / computer
green_color = (0, 255, 0) # anti-virus

purple_color = (128, 0, 128) # computer part
yellow_color = (255, 255, 0) # computer part

pygame.init() # intialize pygame so that the simulation can start properly

# Window related settings
width = state_init[0] * cell_size # making the width to fit the 5 pixel cells and which state their in
height = state_init[1] * cell_size # making the height to fit the 5 pixel cells and which state their in
clock = pygame.time.Clock() # this clock allows us to control the frames per second for the simulation
window = pygame.display.set_mode((width, height)) # creates the window
pygame.display.set_caption("Virus/Malware Simulator") # caption for the window

# since we are done with the setting up, now it's generating the cells and intializing it to 0
state = np.zeros(state_init)
for i in range(state_init[0]):
    for j in range(state_init[1]):
        if (np.random.random() < 0.2):
            state[i][j] = 1

