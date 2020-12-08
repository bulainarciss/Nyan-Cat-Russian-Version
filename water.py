import pygame
from pygame.sprite import Sprite
import random



class Water(Sprite):

    def __init__(self, nc_game,vodka):
        super().__init__()
        self.screen = nc_game.screen
        self.screen_rect = nc_game.screen.get_rect()
        self.settings = nc_game.settings
        self.image = self.settings.water_image
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.width - 50
        self.rect.y = random.randint(50, 550)
        while abs(self.rect.y - vodka.rect.y) <= 100:
            self.rect.y = random.randint(50, 550)
        self.x = float(self.rect.x)
        self.direction = 1

    def update(self):
        self.x -= self.settings.water_speed
        self.rect.x = self.x

    def check_edge(self):
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def draw_water(self):
        self.screen.blit(self.image, self.rect)