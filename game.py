import pygame.sprite
from monstre import Monstre
from class_Player import Player

class Game:
    def __init__(self):
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #group de monstre
        self.all_monstre = pygame.sprite.Group()
        self.pressed = {}
        self.is_playing = False


    def start(self):
        self.is_playing = True
        #genere notre monstre
        self.spawn_monster()
        self.spawn_monster()

    def game_over (self):
        if self.player.health <= 0:
            self.player.health = self.player.max_health
            self.all_monstre = pygame.sprite.Group()
            self.is_playing = False

    def update(self, screen):
        # applique l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self .player.update_health_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres de notre jeu
        for monster in self.all_monstre:
            monster.move()
            monster.update_health_bar(screen)

        # applique l'ensemble des image de mon group de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des image de mon group de monstre
        self.all_monstre.draw(screen)

        # Vérification de la dirrection du joeueur *
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()



    def spawn_monster(self):
        monstre = Monstre(self)
        self.all_monstre.add(monstre)

    def chek_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)