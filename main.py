import pygame
from class_Player import Player
from game import Game

pygame.init()

import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500



pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080,720))

#importe et ccharger le background du jeux
background = pygame.image.load('PygameAssets-main/bg.jpg')

player = Player()

running = True

while running:

    #appliquer le back gound du jeux
    screen.blit(background,(0,-200))

    screen.blit(player.image, (0,0))

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'évent est fermeture de fennetre
        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()
            print("jeux a été quitter")