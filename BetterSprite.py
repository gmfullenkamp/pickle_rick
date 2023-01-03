import os
import pygame


class BetterSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    @staticmethod
    def load_image(name, colorkey=None):
        fullname = os.path.join("images", name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print("Cannot load image: ", name)
            raise SystemExit(message)
        image = image.convert()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image, image.get_rect()
