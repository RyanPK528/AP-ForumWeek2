import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 1000, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rocket Game")

# Load rocket image
rocket_image = pygame.image.load("Try It Yourself/12-3. Rocket/rocket.png")
rocket_rect = rocket_image.get_rect()
rocket_rect.center = (screen_width // 2, screen_height // 2)

# Set up clock
clock = pygame.time.Clock()

# Set up movement speed
speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys that are currently held down
    keys = pygame.key.get_pressed()

    # Update rocket position based on keys
    if keys[pygame.K_UP] and rocket_rect.top > 0:
        rocket_rect.y -= speed
    if keys[pygame.K_DOWN] and rocket_rect.bottom < screen_height:
        rocket_rect.y += speed
    if keys[pygame.K_LEFT] and rocket_rect.left > 0:
        rocket_rect.x -= speed
    if keys[pygame.K_RIGHT] and rocket_rect.right < screen_width:
        rocket_rect.x += speed

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Draw the rocket on the screen
    screen.blit(rocket_image, rocket_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
