import pygame
from pygame.sprite import Sprite
import random


class Vodka(Sprite):

    def __init__(self, nc_game):
        super().__init__()
        self.screen = nc_game.screen
        self.screen_rect = nc_game.screen.get_rect()
        self.settings = nc_game.settings
        self.image = self.settings.vodka_image
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.width - 50
        self.rect.y = random.randint(50,550)
        self.x = float(self.rect.x)
        self.direction = 1

    def update(self):
        self.x -= self.settings.vodka_speed
        self.rect.x = self.x

    def check_edge(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def draw_vodka(self):
        self.screen.blit(self.image, self.rect)