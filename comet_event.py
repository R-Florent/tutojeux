import pygame

class CometFallEvent:

    def __init__(self):
        self.percent = 0

    def add_percent(self):
        self.percent +=1

    def update_bar(self,surface):
        #bar noir ()
        pygame.draw.rect(surface,'black',[
            0,
            surface.get_height(),
            surface.get_width(),
            10
        ])
        #barre rouge
        pygame.draw.rect(surface, 'red', [
            0, #l'axe des x
            surface.get_height(), # l'axe de la fenetre
            (surface.get_width()/100)* self.percent, # longueur de la fentre
            10 # epaissuer de la barre
        ])