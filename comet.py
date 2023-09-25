import pygame

class Comet(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()

        self.velocity = 2
        self.image = pygame.image.load('PygameAssets-main/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    