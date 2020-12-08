import pygame.font
from pygame.sprite import Group
from nyan_cat import Cat

class ScoreBoard:

    def __init__(self, nc_game):
        self.nc_game = nc_game
        self.screen = nc_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = nc_game.settings
        self.stats = nc_game.stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_high_score()
        self.prep_score()
        self.show_score()

    def prep_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, self.settings.text_bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):

        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (73, 33, 106))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20



    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)