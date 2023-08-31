import pygame.sprite
from monstre import Monstre
from class_Player import Player

class Game:
    def __init__(self):
        #generer notre joueur
        self.player = Player(self)
        #group de monstre
        self.all_monstre = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        #genere notre monstre
    def spawn_monster(self):
        monstre = Monstre()
        self.all_monstre.add(monstre)

    def chek_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite,group, False, pygame.sprite.collide_mask() )