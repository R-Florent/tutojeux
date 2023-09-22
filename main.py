import pygame
from pygame.time import Clock

from game import Game

pygame.init()

pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080, 720))

# importe et ccharger le background du jeux
background = pygame.image.load('PygameAssets-main/bg.jpg')

clock = pygame.time.Clock()

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
            self.pressed[event.key] = True

            # Permet de savoir quand le joeur veut tirait un proctile avec la touche espace
            if event.key == pygame.K_SPACE:
                self.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            self.pressed[event.key] = False