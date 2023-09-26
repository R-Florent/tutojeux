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

# Charger le bouton et le redimensionner
btn = pygame.image.load('PygameAssets-main/button.png')
btn = pygame.transform.scale(btn, (400, 150))

# Obtenir le rectangle du bouton
btn_rect = btn.get_rect()

# Calculer la position du bouton au centre de l'écran
btn_x = math.ceil(screen.get_width() / 3.33)
btn_y = math.ceil(screen.get_height() / 2)
btn_rect.topleft = (btn_x, btn_y)


clock = pygame.time.Clock()

#chager notre jeux
game = Game()

running = True

#boucle de jeux

while running:

    game.handle_events()
    game.update(screen)
    game.draw(screen)
    pygame.display.flip()
    clock.tick(90)

    # appliquer le back gound du jeux
    screen.blit(background, (0, -200))

    #vérife si le jeux et en marche
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(btn, (btn_x, btn_y))
        screen.blit(banner, banner_rect)

    # mettre à jour l'écran
    pygame.display.flip()