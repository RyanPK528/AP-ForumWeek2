import pygame
import sys

class GameCharacter:
    def __init__(self, image_path, screen_width, screen_height):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Load image
        self.image = pygame.image.load(image_path)
        self.image_rect = self.image.get_rect()

        # Set screen properties
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Game Character Display")

        # Set background color to match image background
        self.set_background_color()

    def set_background_color(self):
        # Get the color of the top-left pixel in the image (assuming it's the color for the whole background)
        background_color = self.image.get_at((0, 0))
        self.screen.fill(background_color)

    def draw_image_at_center(self):
        # Position the image to the center of the screen
        x = (self.screen_width - self.image_rect.width) // 2
        y = (self.screen_height - self.image_rect.height) // 2

        # Draw the image on the screen
        self.screen.blit(self.image, (x, y))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Draw the image at the center of the screen
            self.draw_image_at_center()

            # Update the display
            pygame.display.flip()

# Run the codes
image_path = "Try It Yourself/12-2. Game Character/character_img.bmp"
screen_width = 800
screen_height = 600

character = GameCharacter(image_path, screen_width, screen_height)
character.run()
