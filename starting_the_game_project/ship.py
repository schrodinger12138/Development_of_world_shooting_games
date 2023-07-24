import pygame
from settings import Settings


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game, player_number):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # Determine the player's starting position based on player_number.
        if player_number == 1:
            self.rect.midbottom = self.screen_rect.midbottom
            self.rect.x += 100
        elif player_number == 2:
            self.rect.midbottom = self.screen_rect.midbottom
            # Offset the second ship's starting position to the left.
            self.rect.x -= 100

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Ship speed settings
        self.normal_speed = self.settings.ship_speed
        self.fast_speed = self.settings.ship_speed * 2  # Double the normal speed

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self._get_current_speed()
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self._get_current_speed()
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self._get_current_speed()
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self._get_current_speed()

    def _get_current_speed(self):
        """Get the current speed based on whether the 'ctrl' key is pressed."""
        return self.fast_speed if pygame.key.get_mods() & pygame.KMOD_CTRL else self.normal_speed

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
