import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Le jeux qu'il est trop bien ")
screen = pygame.display.set_mode((1080, 720))

# importe et ccharger le background du jeux
background = pygame.image.load('PygameAssets-main/bg.jpg')

game = Game()

running = True

while running:
    # appliquer le back gound du jeux
    screen.blit(background, (0, -200))

    # applique l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    # recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # applique l'ensemble des image de mon group de projectiles
    game.player.all_projectiles.draw(screen)

    # appliquer l'ensemble des image de mon group de monstre
    game.all_monstre.draw(screen)

    # Vérification de la dirrection du joeueur *
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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
