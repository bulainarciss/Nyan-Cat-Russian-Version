import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_image = pygame.image.load("imgs/background.bmp")
        self.cat_image = pygame.image.load("imgs/nyan_cat.bmp")
        self.cat_roation = 25
        self.cat_rot_vel = 20
        self.vodka_image = pygame.image.load("imgs/vodka.bmp")
        self.vodka_speed = 10
        self.water_image = pygame.image.load("imgs/water.bmp")
        self.water_image = pygame.transform.scale(self.water_image, (70, 80))
        self.water_speed = 10
        self.cats_limit = 3
        self.text_bg_color = (0,100,21)