import pygame
from  pygameTools import PygameTools
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.ship_speed = 10
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.FPS = 60
        self.background_image =PygameTools.scale_image("images/GameBackgroundImage.jpg", 1)
        #bullet
        self.bullet_speed = 1.2
        self.bullet_weight = 3
        self.bullet_number = 10
        self.bullet_color = (60,60,60)

