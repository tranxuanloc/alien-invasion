import pygame


class Ship:
    def __init__(self, ai_game: "AlienInvasion"):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Set the ship position at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw the ship
        self.screen.blit(self.image, self.rect)

    def update(self):
        #  Update the ship's position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
