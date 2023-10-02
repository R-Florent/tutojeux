import pygame

class AnimatieSprite(pygame.sprite.Sprite):

    def __iter__(self, sprite_name):
        super().__iter__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'animation
        self.image = animation.get(sprite_name)

    def animate(self):

        #passage à l'image suivante
        self.current_image += 1

        #vérifier si on a attenti la fin de l'animation
        if self.current_image >= len(self.images):
            #remmetre l'annimation  a la 1er etape
            self.current_image = 0

        self.image = self.image[self.current_image]




#definir une fonction pour charger les image d'un sprite

def load_animation_images(sprite_name):
    #charger les 24 images de c'est sprite
    images =[]
    #recuperer le chemin du dossier pour ce sprtie
    path = f"assets/{sprite_name}/{sprite_name}"

    for i in range(1, 24):
        image_path = path + str(i) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenue de la liste avec les image
    return images


#définir un dictionnaire qui va contenir les image chargée de chque image
animation = {
    'mummy': load_animation_images('mummy')


}