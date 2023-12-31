import pygame.sprite
from monstre import Monstre, Mummy, Alien
from player import Player
from comet_event import CometFallEvent
from sounds import SoundManager

class Game:
    def __init__(self):

        #def si notre jeux et lancée ou non
        self.is_playing = False

        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        #group de monstre
        self.all_monstre = pygame.sprite.Group()
        self.pressed = {}

        #génre le sont
        self.sound_mangaer = SoundManager()

        #generer l'event commet event
        self.coment_event = CometFallEvent(self)

        self.score = 0

    def update(self, screen):
        #afficher le score sur l'ecarn
        fonnt = pygame.font.Font("PygameAssets-main/PixelifySans.ttf",25)
        score_text = fonnt.render(f"Score : {self.score}",1, (0,0,0))
        screen.blit(score_text,(20,20))

        # applique l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self .player.update_health_bar(screen)

        #actualiser la barre de remplissage de l'event coment_event
        self.coment_event.update_bar(screen)

        self.player.update_animation()

        # recuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres de notre jeu
        for monster in self.all_monstre:
            monster.move()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.coment_event.all_comets:
            comet.fall()

        # applique l'ensemble des image de mon group de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des image de mon group de monstre
        self.all_monstre.draw(screen)

        self.coment_event.all_comets.draw(screen)

        # Vérification de la dirrection du joeueur *
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def start(self):
        self.is_playing = True
        # Génère nos monstres en spécifiant leur classe
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.coment_event.percent = 0

    def game_over (self):
        if self.player.health <= 0:
            self.player.health = self.player.max_health
            self.coment_event.all_comets = pygame.sprite.Group()
            self.coment_event.rest_percent()
            self.all_monstre = pygame.sprite.Group()
            self.score = 0
            self.is_playing = False
            self.sound_mangaer.play('game_over')

    def spawn_monster(self, monster_class_name):
        self.all_monstre.add(monster_class_name.__call__(self))


    def chek_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def draw_all(self, screen):

        screen.blit(self.player.image, self.player.rect)
        # met a jour les barre hp et commet event
        self.player.update_health_bar(screen)
        self.coment_event.update_bar(screen)

        # applique l'ensemble des image de mon group de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des image de mon group de monstre
        self.all_monstre.draw(screen)

        #appliquer l'ensemble des image de mon group de commet
        self.coment_event.all_comets.draw(screen)

    def add_score(self,score_point):
        self.score += score_point

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
            elif event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

        # Ajoute d'autres gestionnaires d'événements ici