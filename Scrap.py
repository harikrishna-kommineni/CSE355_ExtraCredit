import pygame
import numpy as np

# Define the size of the grid
grid_size = (100, 100)

# Define the size of each cell in pixels
cell_size = 5

# Define the colors of the cells
alive_color = (255, 255, 255)
dead_color = (0, 0, 0)
born_color = (255, 0, 0)

# Define the probability of a cell starting alive
start_alive_prob = 0.2

# Initialize Pygame
pygame.init()

# Set up the window
screen_width = grid_size[0] * cell_size
screen_height = grid_size[1] * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of Life with Color")

# Set up the clock
clock = pygame.time.Clock()

# Set up the initial grid
grid = np.zeros(grid_size)
for i in range(grid_size[0]):
    for j in range(grid_size[1]):
        if np.random.random() < start_alive_prob:
            grid[i][j] = 1

# Define the function to update the grid
def update_grid():
    global grid
    new_grid = np.zeros(grid_size)
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            neighbors = grid[max(0, i-1):min(grid_size[0], i+2),
                              max(0, j-1):min(grid_size[1], j+2)]
            num_alive = int(np.sum(neighbors)) - int(grid[i][j])
            if grid[i][j] == 0 and num_alive == 3:
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and (num_alive == 2 or num_alive == 3):
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and num_alive <= 1:
                new_grid[i][j] = -1
            elif grid[i][j] == 1 and num_alive >= 4:
                new_grid[i][j] = -1
    grid += new_grid
    grid = np.clip(grid, 0, 1)

# Define the function to draw the grid
def draw_grid():
    screen.fill(dead_color)
    pygame.draw.rect(screen, born_color, (grid_size[0], grid_size[1], 30, 45))
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, alive_color, (i*cell_size, j*cell_size, cell_size, cell_size))
            elif grid[i][j] == -1:
                pygame.draw.rect(screen, born_color, (i*cell_size, j*cell_size, cell_size, cell_size))

# Run the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the grid
    update_grid()

    # Draw the grid
    draw_grid()

    # Update the screen
    pygame.display.flip()

    # Delay to control the frame rate
    clock.tick(60)