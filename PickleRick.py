from pygame.locals import *

from BetterSprite import BetterSprite


class PickleRick(BetterSprite):
    X_DIST = 3
    Y_DIST = 3
    SAFE_DISTANCE = 175

    def __init__(self, max_x, max_y):
        BetterSprite.__init__(self)
        self.maxX = max_x
        self.maxY = max_y
        self.image_right, self.rect = self.load_image("pickle_right.png", -1)
        self.image_left, self.rect = self.load_image("pickle_left.png", -1)
        self.image_up, self.rect = self.load_image("pickle_up.png", -1)
        self.image_down, self.rect = self.load_image("pickle_down.png", -1)
        self.image = self.image_right
        self.nuts = 0
        self.xMove = 0
        self.yMove = 0

    def startmove(self, key):
        if key == K_RIGHT:
            self.xMove = PickleRick.X_DIST
        elif key == K_LEFT:
            self.xMove = -PickleRick.X_DIST
        elif key == K_DOWN:
            self.yMove = PickleRick.Y_DIST
        elif key == K_UP:
            self.yMove = -PickleRick.Y_DIST

    def stopmove(self, key):
        if key == K_RIGHT:
            self.xMove = 0
        elif key == K_LEFT:
            self.xMove = 0
        elif key == K_DOWN:
            self.yMove = 0
        elif key == K_UP:
            self.yMove = 0

    def get_right_x(self):
        return self.rect.x + self.rect.width

    def get_bottom_y(self):
        return self.rect.y + self.rect.height

    def update(self):
        if self.xMove >= 0:
            self.image = self.image_right
        elif self.xMove < 0:
            self.image = self.image_left
        if self.yMove > 0:
            self.image = self.image_down
        elif self.yMove < 0:
            self.image = self.image_up
        if self.xMove != 0 or self.yMove != 0:
            local_x_move = self.xMove
            local_y_move = self.yMove
            if self.rect.x + self.xMove < 0 or self.get_right_x() + self.xMove > self.maxX:
                local_x_move = 0
            if self.rect.y + self.yMove < 0 or self.get_bottom_y() + self.yMove > self.maxY:
                local_y_move = 0
            self.rect.move_ip(local_x_move, local_y_move)
