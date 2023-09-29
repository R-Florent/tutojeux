import pygame
import random

import game


class Comet(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.game = game  # Stocke la référence à l'objet Game
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 1010)
        self.rect.y = -random.randint(30, 600)
        self.velocity = random.randint(1, 3)
        self.dmg = 4

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            print("sol")
