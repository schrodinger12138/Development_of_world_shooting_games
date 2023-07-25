import pygame
from pygame.sprite import Sprite


class HealthPointSys:

    def __init__(self, initArmorNumber, game_instances_ref):
        self.screen = game_instances_ref.screen
        self.image = pygame.image.load('images/Armor.PNG')
        self.screen_rect = game_instances_ref.screen.get_rect()
        self.armorNumber = 3
        self.armorNumber = range(initArmorNumber - 1)
        self.armorIconArray = []
        self.init_game_relate_data()

    def init_game_relate_data(self):
        for i in self.armorNumber:
            temp_icon = ArmorIcon(self.image, (200 + i * 80, 300), self.screen)
            self.armorIconArray.append(temp_icon)

    def recoverArmorNumber(self):
        self.armorNumber += 1
        temp_icon = ArmorIcon(self.image, (200 + (self.armorNumber + 1) * 80, 300), self.screen)
        self.armorIconArray.append(temp_icon)

    def DamageArmorNumber(self):
        self.armorNumber -= 1
        self.armorIconArray.remove(self.armorIconArray[self.armorIconArray.count()])
        if self.armorNumber < 0:
            self.postDamageProcess()

    # def postDamageProcess(self):

    # draw UI
    def draw_hp_ui(self):
        for tempSource in self.armorIconArray:
            tempSource.blitme()


class ArmorIcon(Sprite):
    def __init__(self, armor_icon, icon_rect, target_screen):
        self.image = armor_icon
        self.rect = icon_rect
        self.screen = target_screen

    def blitme(self):
        self.screen.blit(self.image, self.rect)
