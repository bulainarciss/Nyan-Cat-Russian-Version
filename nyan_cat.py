import pygame

class Cat():
    def __init__(self, nc_game):
        self.screen = nc_game.screen
        self.settings = nc_game.settings
        self.max_roation =self.settings.cat_roation
        self.gravity = 9.8
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.rot_vel = self.settings.cat_rot_vel
        self.screen_rect = nc_game.screen.get_rect()
        self.image = self.settings.cat_image
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def jump(self):

        self.vel = -10
        self.tick_count = 0

    def move(self):
        self.tick_count += 1
        displacement = self.vel * (self.tick_count) + 1.5*(self.tick_count)**2

        if displacement >= 16:
            displacement = 16
        if displacement < 0:
            displacement -= 2
        if self.rect.y + displacement >= -20:
            self.rect.y += displacement
        if self.rect.y >= 600:
            self.rect.y = 600

    def center_cat(self):
        self.rect.y = self.screen_rect.height / 2


