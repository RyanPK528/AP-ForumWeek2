import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 600))
bg_color = 	(135, 206, 235)
    
pygame.display.set_caption("Blue Sky Window")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
                
    screen.fill(bg_color)
    pygame.display.flip()

