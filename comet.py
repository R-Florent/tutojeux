import pygame
import random

class Comet(pygame.sprite.Sprite):
    
    def __init__(self,game):
        super().__init__()

        self.velocity = random.randint(1, 3)
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 1010)
        self.rect.y = - random.randint(30, 600)
        self.dmg = 4


    def fall(self):
        #le déplacment ne se fait que si il n'est pas en contacte avec le J
        if not self.game.chek_collision(self, self.game.all_players):
            self.rect.y -= self.velocity  # Déplace le joueur vers la droite
        else:
            self.game.player.take_dmg(self.attack)
    