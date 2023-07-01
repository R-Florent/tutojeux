import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/player.png')
        print(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self):
        self.rect.x += self.velocity  # Déplace le joueur vers la droite

    def move_left(self):
        self.rect.x -= self.velocity  # Déplace le joueur vers la gauche

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))