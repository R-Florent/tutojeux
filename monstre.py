import pygame

class Monstre(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 20
        self.max_health = 20
        self.attack = 5
        self.velocity = 1
        self.image = pygame.image.load('PygameAssets-main/mummy.png')
        self.rect = self.image.get_rect()
        print(self.image)
        self.rect.x = 1080
        self.rect.y = 500

    def update_health_bar(self, surface):
        #definir une couleur pour notre jauge de vie
        bar_color = (215, 5, 5)
        #('05D72B')

        #définir la posistion de notre jauge de vie
        bar_position = [self.rect.x + 10, self.rect.y -20, self.health, 5]

        #dessiner la barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

    def move(self):
        #le déplacment ne se fait que si il n'est pas en contacte avec le J
        if not self.game.chek_collision(self, self.game.all_players):
            self.rect.x -= self.velocity  # Déplace le joueur vers la droite
        