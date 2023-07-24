import sys
import pygame
import math
from settings import Settings
from ship import Ship
from  bullet import  Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("U1S1Alien Invasion")
        clock = pygame.time.Clock()
        clock.tick(self.settings.FPS)
        #self.ship = Ship(self)
        self.ship1 = Ship(self, player_number=1)
        self.bullets_player1 = pygame.sprite.Group()
        self.ship2 = Ship(self, player_number=2)
        self.bullets_player2 = pygame.sprite.Group()
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            #self.ship.update()
            self.ship1.update()
            self.ship2.update()
            self._update_bullets()
            self._update_screen()
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)#deL(BreakGame)up...123456
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship1.moving_right = True
        elif event.key == pygame.K_LEFT :
            self.ship1.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship1.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship1.moving_down = True
        elif event.key == pygame.K_d:  # Right Shift key for player 2
            self.ship2.moving_right = True
        elif event.key == pygame.K_a:  # 'A' key for player 2
            self.ship2.moving_left = True
        elif event.key == pygame.K_w:  # 'W' key for player 2
            self.ship2.moving_up = True
        elif event.key == pygame.K_s:  # 'S' key for player 2
            self.ship2.moving_down = True
        elif event.key == pygame.K_DELETE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_TAB:
            self._fire_bullet_barrage()
    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship1.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship1.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship1.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship1.moving_down = False
        elif event.key == pygame.K_d:  # 'D' key for player 2
            self.ship2.moving_right = False
        elif event.key == pygame.K_a:  # 'A' key for player 2
            self.ship2.moving_left = False
        elif event.key == pygame.K_w:  # 'W' key for player 2
            self.ship2.moving_up = False
        elif event.key == pygame.K_s:  # 'S' key for player 2
            self.ship2.moving_down = False
    def _fire_bullet(self):
        if len(self.bullets_player1) < self.settings.bullet_number:
            new1_bullet = Bullet(self, player_number=1)
            self.bullets_player1.add(new1_bullet)
        if len(self.bullets_player1) < self.settings.bullet_number:
            new2_bullet = Bullet(self, player_number=2)
            self.bullets_player1.add(new2_bullet)
    def _fire_bullet_barrage(self,barrage_radius=120, num_bullets=10):
        if len(self.bullets_player1) < self.settings.bullet_number:
            for i in range(num_bullets):
                angle = i * (360 / num_bullets)  # Calculate angle between bullets
                radians = math.radians(angle)  # Convert angle to radians
                new1_bullet = Bullet(self, player_number=1)  # Create a new bullet
                new1_bullet.rect.x = self.ship1.rect.centerx + int(
                    barrage_radius * math.cos(radians))  # Calculate bullet x-coordinate
                new1_bullet.rect.y = self.ship1.rect.centery - int(
                    barrage_radius * math.sin(radians))  # Calculate bullet y-coordinate
                self.bullets_player1.add(new1_bullet)  # Add the bullets to the group
        if len(self.bullets_player2) < self.settings.bullet_number:
            for i in range(num_bullets):
                angle = i * (360 / num_bullets)  # Calculate angle between bullets
                radians = math.radians(angle)  # Convert angle to radians
                new2_bullet = Bullet(self, player_number=2)  # Create a new bullet
                new2_bullet.rect.x = self.ship2.rect.centerx + int(
                    barrage_radius * math.cos(radians))  # Calculate bullet x-coordinate
                new2_bullet.rect.y = self.ship2.rect.centery - int(
                    barrage_radius * math.sin(radians))  # Calculate bullet y-coordinate
                self.bullets_player2.add(new2_bullet)



    def _update_bullets(self):
        self.bullets_player1.update()
        for bullet in self.bullets_player1:
            if bullet.rect.bottom <= 0:
                self.bullets_player1.remove(bullet)
        self.bullets_player2.update()
        for bullet in self.bullets_player2:
            if bullet.rect.bottom <= 0:
                self.bullets_player2.remove(bullet)
    def _update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # 绘制背景
        self.screen.blit(self.settings.background_image, (0, 0))
        self.ship1.blitme()
        self.ship2.blitme()
        for bullet in self.bullets_player1.sprites():
            bullet.draw_bullet()
        for bullet in self.bullets_player2.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
