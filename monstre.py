import pygame
import random
import animation
class Monstre(animation.AnimatieSprite):
    def __init__(self, game, monster_type, size , offset=0):
        super().__init__(monster_type, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.image = pygame.image.load('PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        print(self.image)
        self.rect.x = 1080 + random.randint(1, 600)
        self.rect.y = 540 - offset
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 5)

    def take_dmg(self, amount):
        self.health -= amount

        if self.health <= 0 :
            #le tuer
            # self.all_monstre.remove(self)

            #le faire respawn pour ne pas consomer trop de mémoire
            self.rect.x = 1080 + random.randint(1, 600)
            self.health = self.max_health
            self.velocity = random.randint(1, self.default_speed)

            if self.game.coment_event.is_full_loaded():
                self.game.all_monstre.remove(self)

                self.game.coment_event.attempt_fall()

            else:
              print("plui de météore")

    def update_animation(self):
        self.animate(loop=True)


    def update_health_bar(self, surface):

        #dessiner la barre de vie
        pygame.draw.rect(surface, (215, 5, 5), [self.rect.x + 10, self.rect.y - 30, self.max_health, 5])
        pygame.draw.rect(surface, (5, 215, 43), [self.rect.x + 10, self.rect.y -30, self.health, 5])


    def move(self):
        #le déplacment ne se fait que si il n'est pas en contacte avec le J
        if not self.game.chek_collision(self, self.game.all_players):
            self.rect.x -= self.velocity  # Déplace le joueur vers la droite
        else:
            self.game.player.take_dmg(self.attack)

#def classe Mummy
class Mummy(Monstre):

    def __init__(self, game):
        super().__init__(game , "mummy", (130,130))
        self.set_speed(5)

#def classe Mummy
class Alien(Monstre):

    def __init__(self, game):
        super().__init__(game , "alien",(300,300),140)
        self.max_health =250
        self.health =250
        self.set_speed(2)
        self.attack = 3