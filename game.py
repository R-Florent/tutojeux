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
        self.spawn_monster()
        self.spawn_monster()
        #genere notre monstre

    def update(self, screen):
        # applique l'image de mon joueur
        self.game = game
        screen.blit(self.player.image, self.game.player.rect)

        # actualiser la barre de vie du joueur
        self.game.player.update_health_bar(screen)

        # recuperer les projectiles du joueur
        for projectile in self.game.player.all_projectiles:
            projectile.move()

        # recuperer les monstres de notre jeu
        for monster in self.game.all_monstre:
            monster.move()
            monster.update_health_bar(screen)

        # applique l'ensemble des image de mon group de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des image de mon group de monstre
        self.all_monstre.draw(screen)

        # Vérification de la dirrection du joeueur *
        if self.pressed.get(pygame.K_RIGHT) and self.game.player.rect.x + self.game.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.game.player.rect.x > 0:
            self.player.move_left()



    def spawn_monster(self):
        monstre = Monstre(self)
        self.all_monstre.add(monstre)

    def chek_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)