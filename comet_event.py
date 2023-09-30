import pygame
from comet import Comet
class CometFallEvent:

    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        #def  un group de commet
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed/4

    def is_full_loaded(self):
        return self.percent >=100

    def rest_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # Faire apparaître une boule de feu
#       comet = Comet()
        self.all_comets.add(Comet(self))  # Passer self.game comme argument

    def attempt_fall(self):

        if self.is_full_loaded():
            print("lancement de la plui de météorite")
            self.rest_percent()
            self.meteor_fall()


    def update_bar(self, surface):

        self.add_percent()

        self.attempt_fall()

        #bar noir ()
        pygame.draw.rect(surface,'black',[
            0,
            surface.get_height() -20,
            surface.get_width(),
            10
        ])
        #barre rouge
        pygame.draw.rect(surface, 'red', [
            0, #l'axe des x
            surface.get_height()-20, # l'axe de la fenetre
            (surface.get_width()/100)* self.percent, # longueur de la fentre
            10 # epaissuer de la barre
        ])