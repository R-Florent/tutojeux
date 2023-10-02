import pygame

class AnimatieSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.images = animation.get(sprite_name)
        self.current_image = 0  # Commencer l'animation
        self.animation = False
        self.image = self.images[self.current_image]  # Charger la première image

    #méthode qui démar l'annimation
    def start_animation(self):
        self.animation = True

    def animate(self , loop = False):

        #Es que l'annimation est sur true donc doit étre lancée ?
        if self.animation:
            #passage à l'image suivante
            self.current_image += 1

            #vérifier si on a attenti la fin de l'animation
            if self.current_image >= len(self.images):
                #remmetre l'annimation  a la 1er etape
                self.current_image = 0

                if loop is False:
                    self.animation = False

            self.image = self.images[self.current_image]




#definir une fonction pour charger les image d'un sprite

def load_animation_images(sprite_name):
    #charger les 24 images de c'est sprite
    images =[]
    #recuperer le chemin du dossier pour ce sprtie
    path = f"PygameAssets-main/{sprite_name}/{sprite_name}"

    for i in range(1, 24):
        image_path = path + str(i) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenue de la liste avec les image
    return images


#définir un dictionnaire qui va contenir les image chargée de chque image
animation = {
    'mummy': load_animation_images('mummy'),
    'player' : load_animation_images('player')

}