import pygame
from game import Game
pygame.init()

pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080,720))

#importe et ccharger le background du jeux
background = pygame.image.load('PygameAssets-main/bg.jpg')

game = Game()

running = True


while running:
    #appliquer le back gound du jeux
    screen.blit(background,(0,-200))

    screen.blit(game.player.image, game.player.rect)

    #Vérification de la dirrection du joeueur *
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre à jour l'écran
    pygame.display.flip()

    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'évent est fermeture de fennetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeux a été quitter")
        #implémentation des touche de
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
