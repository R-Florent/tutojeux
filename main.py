import pygame
from pygame.time import Clock
import math
from game import Game

pygame.init()

pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080, 720))

# importe et charger le background du jeux et +
background = pygame.image.load('PygameAssets-main/bg.jpg')
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

clock = pygame.time.Clock()

#chager notre jeux
game = Game()

running = True

#boucle de jeux

while running:

    clock.tick(90)

    # appliquer le back gound du jeux
    screen.blit(background, (0, -200))

    #vérife si le jeux et en marche
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(banner, banner_rect)


    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'évent est fermeture de fennetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("jeux a été quitter")
        # implémentation des touche de
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Permet de savoir quand le joeur veut tirait un proctile avec la touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False