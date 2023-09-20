import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 1
        self.player = player
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 4
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        #verifier si le projectile entre en collision avec un monstre
        for monstre in self.player.game.chek_collision(self, self.player.game.all_monstre):
            self.remove()
            monstre.take_dmg(self.player.attack)


        if self.rect.x > 1080:
            self.remove()