import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('PygameAssets-main/player.png')
        print(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
