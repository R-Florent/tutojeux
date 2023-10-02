import pygame

import animation
from projectile import Projectile

class Player(animation.AnimatieSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
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
        self.start_animation()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface, (215, 5, 5), [self.rect.x + 50, self.rect.y +20, self.max_health, 7])
        pygame.draw.rect(surface, (5, 215, 43), [self.rect.x + 50, self.rect.y +20, self.health, 7])

    def take_dmg(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()
 #           pygame.quit()