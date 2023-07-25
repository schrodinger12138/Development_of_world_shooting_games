import pygame
from settings import Settings
from ship import Ship


class HealthPointSys:
    armorNumber = 0
    armorIconArray = []

    def __init__(self, initArmorNumber):
        self.armorNumber = range(initArmorNumber - 1)
        self.image = pygame.image.load('images/Armor.PNG')
        self.init_game_relate_data()

    def init_game_relate_data(self):

        for i in self.armorNumber:
            self.rect = self.image.get_rect()
            self.armorIconArray.append(self.image)

    def recoverArmorNumber(self, recoverCount):
        self.armorNumber += recoverCount

    def DamageArmorNumber(self, damageCount):
        self.armorNumber -= damageCount
        if self.armorNumber < 0:
            self.postDamageProcess()

    # def postDamageProcess(self):
