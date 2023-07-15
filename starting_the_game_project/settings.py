import pygame

from chapter_12.starting_the_game_project import pygameTools
from  pygameTools import PygameTools


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.FPS = 60
        self.background_image =PygameTools.scale_image("123.jpg", 0.05)
