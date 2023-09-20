import pygame
import random

class Monstre(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = random.randint(1, 5)
        self.image = pygame.image.load('PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        print(self.image)
        self.rect.x = 1080 + random.randint(1, 600)
        self.rect.y = 540
        print(self.velocity)
    def take_dmg(self, amount):
        self.health -= amount

        if self.health <= 0:
            #le tuer
            # self.all_monstre.remove(self)

            #le faire respawn pour ne pas consomer trop de mémoire
            self.rect.x = 1080 + random.randint(1, 600)
            self.health = self.max_health
            self.velocity = random.randint(1, 5)



    def update_health_bar(self, surface):
        #definir une couleur pour notre jauge de vie
        bar_color_red = (215, 5, 5)
        bar_color = (5, 215, 43)

        #définir la posistion de notre jauge de vie
        bar_position = [self.rect.x + 10, self.rect.y -30, self.health, 5]
        bar_position_red = [self.rect.x + 10, self.rect.y - 30, self.max_health, 5]

        #dessiner la barre de vie
        pygame.draw.rect(surface, bar_color_red, bar_position_red)
        pygame.draw.rect(surface, bar_color, bar_position)



    def move(self):
        #le déplacment ne se fait que si il n'est pas en contacte avec le J
        if not self.game.chek_collision(self, self.game.all_players):
            self.rect.x -= self.velocity  # Déplace le joueur vers la droite
        