import pygame

class Monstre(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 20
        self.max_health = 20
        self.attack = 5
        self.velocity = 5
        self.image = pygame.image.load('PygameAssets-main/mummy.png')
        print(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def move(self):
        