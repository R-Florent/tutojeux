import pygame
from game import Game
pygame.init()

pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080,720))

#importe et ccharger le background du jeux
background = pygame.image.load('PygameAssets-main/bg.jpg')

game = Game

running = True

while running:
    #appliquer le back gound du jeux
    screen.blit(background,(0,-200))

    screen.blit(game.player.image, game.player.rect)

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'évent est fermeture de fennetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeux a été quitter")
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()