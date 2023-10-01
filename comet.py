import pygame
import random

import game
from player import Player


class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()

        self.game = game  # Stocke la référence à l'objet Game
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 1010)
        self.rect.y = -random.randint(30, 600)
        self.velocity = random.randint(1, 3)
        self.dmg = 4
        self.comet_event = comet_event

    def removeComet(self):
        self.comet_event.all_comets.remove(self)

        if len(self.comet_event.all_comets) == 0:
            print("event fini")

            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            print("sol")
            self.removeComet()

            if len(self.comet_event.all_comets) == 0 :
                print("coment_event fini")
                self.comet_event.rest_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.chek_collision(
            self, self.comet_event.game.all_players ):
            print("commet a toucher un joeur")
            self.removeComet()
            for player in self.comet_event.game.all_players:
                player.take_dmg(20)