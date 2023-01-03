import pygame
from pygame.locals import *
import random
import sys
import time

from Nut import Nut
from PickleRick import PickleRick
from Rat import Rat


class PygameMain:
    """Main Class, initializes the game"""
    COLOR_WHITE = ([250, 250, 250])
    COLOR_BLACK = ([0, 0, 0])
    MAX_SCORE = 1000

    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(PygameMain.COLOR_BLACK)
        self.rat_attacks = 0
        self.total_nuts = 1
        self.rat_sprites = None
        self.nut_sprites = None
        self.pickle_rick = None
        self.pickle_rick_sprites = None

    def run(self):
        self.load_sprites()

        while True:
            if self.rat_attacks < 10:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == KEYDOWN:
                        if event.key in [K_RIGHT, K_LEFT, K_UP, K_DOWN]:
                            self.pickle_rick.startmove(event.key)
                    elif event.type == KEYUP:
                        if event.key in [K_RIGHT, K_LEFT, K_UP, K_DOWN]:
                            self.pickle_rick.stopmove(event.key)
                # Screen
                self.screen.blit(self.background, (0, 0))
                self.pickle_rick.update()
                self.roll_for_rat()
                self.rat_sprites.update()
                self.pickle_rick_sprites.draw(self.screen)
                self.nut_sprites.draw(self.screen)
                self.rat_sprites.draw(self.screen)
                if len(self.nut_sprites.sprites()) > 0:
                    lst_cols = pygame.sprite.spritecollide(self.pickle_rick, self.nut_sprites, True)
                    self.total_nuts += len(lst_cols)
                    self.update_scores()
                else:
                    self.load_nuts()
                    self.update_scores()
                if len(self.nut_sprites.sprites()) > 0:
                    lst_cols = pygame.sprite.groupcollide(self.pickle_rick_sprites, self.rat_sprites, True, True)
                    if len(lst_cols) > 0:
                        self.load_pickle()
                        self.rat_attacks += 1
                        self.update_scores()
                for sprite in self.rat_sprites.sprites():
                    if sprite.off_screen():
                        sprite.kill()
                self.update_scores()
                pygame.display.flip()
                pygame.time.delay(15)
            else:
                font = pygame.font.Font(None, 64)
                text = font.render("The rats have defeated you.", True, (255, 0, 0))
                textpos = text.get_rect(center=[self.width / 2, self.height / 2 - 20])
                self.screen.blit(text, textpos)
                text = font.render("Nuts collected: %s" % self.total_nuts, True, (255, 0, 0))
                textpos = text.get_rect(center=[self.width / 2, self.height / 2 + 20])
                self.screen.blit(text, textpos)
                pygame.display.flip()
                time.sleep(30)
                sys.exit()

    def update_scores(self):
        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Rat Attacks: %d  --  Total Nuts: %s" % (self.rat_attacks, self.total_nuts), True,
                               (0, 255, 0))
            textpos = text.get_rect(centerx=self.width / 2)
            self.screen.blit(text, textpos)

    def roll_for_rat(self):
        if self.total_nuts > 500 and self.rat_attacks == 0 and random.randint(0, 10) == 0:
            self.rat_sprites.add(Rat(self.width, self.height, self.pickle_rick.rect))
        elif self.total_nuts > 250 and self.rat_attacks == 0 and random.randint(0, 50) == 0:
            self.rat_sprites.add(Rat(self.width, self.height, self.pickle_rick.rect))
        elif self.rat_attacks == 0:
            if random.randint(0, 100) == 0:
                self.rat_sprites.add(Rat(self.width, self.height, self.pickle_rick.rect))
        elif random.randint(0, PygameMain.MAX_SCORE) < (self.total_nuts / (self.rat_attacks * 10)):
            # TODO: Make sure rats don't spawn next to player
            self.rat_sprites.add(Rat(self.width, self.height, self.pickle_rick.rect))

    def load_sprites(self):
        self.load_pickle()
        self.load_nuts()
        self.rat_sprites = pygame.sprite.Group()

    def load_nuts(self):
        n_num_horizontal = int(self.width / 30)
        n_num_vertical = int(self.height / 30)
        self.nut_sprites = pygame.sprite.Group()
        for x in range(n_num_horizontal):
            for y in range(n_num_vertical):
                self.nut_sprites.add(Nut(pygame.Rect(x * 30, y * 30, 10, 10)))

    def load_pickle(self):
        try:
            self.pickle_rick.kill()
        except:
            pass
        self.pickle_rick = PickleRick(self.width, self.height)
        self.pickle_rick_sprites = pygame.sprite.RenderPlain(self.pickle_rick)
