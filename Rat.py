import math
import pygame
import random

from BetterSprite import BetterSprite
from PickleRick import PickleRick


class Rat(BetterSprite):
    MAX_SPEED = 2

    def __init__(self, max_x, max_y, pickle_rect=None):
        BetterSprite.__init__(self)
        self.maxX = max_x
        self.maxY = max_y
        self.image, self.rect = self.load_image("rat.png", -1)

        while True:
            x = random.randint(0, max_x - self.rect.width)
            y = random.randint(0, max_y - self.rect.height)
            self.rect = pygame.Rect(x, y, 15, 15)
            if pickle_rect is not None and self.distance(pickle_rect, self.rect) < PickleRick.SAFE_DISTANCE:
                continue
            break
        while True:
            self.xMove = random.randint(-Rat.MAX_SPEED, Rat.MAX_SPEED)
            self.yMove = random.randint(-Rat.MAX_SPEED, Rat.MAX_SPEED)
            if self.xMove != 0 or self.yMove != 0:
                break

    def update(self):
        if self.xMove != 0 or self.yMove != 0:
            self.rect.move_ip(self.xMove, self.yMove)

    def get_right_x(self):
        return self.rect.x + self.rect.width

    def get_bottom_y(self):
        return self.rect.y + self.rect.height

    def off_screen(self):
        return self.rect.x < 0 or \
               self.rect.y < 0 or \
               self.get_bottom_y() > self.maxY or \
               self.get_right_x() > self.maxX

    @staticmethod
    def distance(tuple1, tuple2):
        return math.sqrt(math.pow(tuple1[0] - tuple2[0], 2) + math.pow(tuple1[1] - tuple2[1], 2))
