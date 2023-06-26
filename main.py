import pygame
from class_Player import Player
from game import Game



pygame.init()

pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080,720))

#importe et ccharger le background du jeux
background = pygame.image.load('PygameAssets-main/bg.jpg')


running = True

while running:

    #appliquer le back gound du jeux
    screen.blit(background,(0,-200))

    screen.blit(Game.player.image, Game.player.rect)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'évent est fermeture de fennetre
        if event.type == pygame.QUIT:
            runnig = False
            pygame.quit()
            print("jeux a été quitter")