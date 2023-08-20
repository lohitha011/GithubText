mport pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window and colors
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman Game")
black = (0, 0, 0)
yellow = (255, 255, 0)

# Pacman properties
pacman_x = 400
pacman_y = 300
pacman_radius = 20
pacman_speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Clear the screen
    screen.fill(black)

    # Draw Pacman
    pygame.draw.circle(screen, yellow, (pacman_x, pacman_y), pacman_radius)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
sys.exit()
