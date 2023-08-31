import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/player.png')
        print(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move_right(self):
         if not self.game.chek_collision(self,self.game.all_monstre):
             self.rect.x += self.velocity  # Déplace le joueur vers la droite

    def move_left(self):
        self.rect.x -= self.velocity  # Déplace le joueur vers la gauche

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))