import pygame
from pygame.sprite import Sprite
import math
class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, player_number):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.player_number = player_number
        self.rect = pygame.Rect(0 , 0 , self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect1 = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship1.rect.midtop if player_number == 1 else ai_game.ship2.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class BulletType(Bullet):
    def __init__(self, ai_game):
        """Create a circular bullet object at the ship's current position."""
        super().__init__(ai_game)  # Call the parent class constructor
        # Additional attributes for CircleBullet
        self.barrage_radius = 120
        self.num_bullets = 10