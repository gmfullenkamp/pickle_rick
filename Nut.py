from BetterSprite import BetterSprite


class Nut(BetterSprite):
    def __init__(self, rect=None):
        BetterSprite.__init__(self)
        self.image, self.rect = self.load_image("nut.png", -1)
        if rect is not None:
            self.rect = rect
