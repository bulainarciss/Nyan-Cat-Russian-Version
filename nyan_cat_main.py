import sys
import pygame
from time import sleep, time
from settings import Settings
from nyan_cat import Cat
from vodka import Vodka
from water import Water
from game_stats import GameStats
from scoreboard import ScoreBoard

class NyanCat:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption("Nyan Cat!")
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.cat = Cat(self)
        self.stats = GameStats(self)
        self.vodkas = pygame.sprite.Group()
        self.waters = pygame.sprite.Group()
        self.sb = ScoreBoard(self)

    def run_game(self):
        clock = pygame.time.Clock()
        last_time = time()
        while True:
            self._check_events()
            self.update_screen()
            if time() - last_time > 2:
                self._create_vodka()
                last_time = time()
            self.cat.move()
            self._update_vodkas()
            self._check_cat_water_collision()
            self._check_cat_vodka_collision()
            clock.tick(30)


    def _create_vodka(self):
        vodka = Vodka(self)
        water = Water(self, vodka)
        self.vodkas.add(vodka)

        for i in range(6):
            water = Water(self, vodka)
            self.waters.add(water)


    def _update_vodkas(self):
        self.vodkas.update()
        self.waters.update( )


    def update_screen(self):
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.cat.blitme()
        self.sb.show_score()
        for vodka in self.vodkas.sprites():
            vodka.draw_vodka()
        for water in self.waters.sprites():
            water.draw_water()
        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.cat.jump()

    def _check_cat_water_collision(self):
        if pygame.sprite.spritecollideany(self.cat, self.waters):
            if self.stats.cats_left > 0:
                self.stats.reset_stats()
                self.vodkas.empty()
                self.waters.empty()
                self.cat.center_cat()
                self.sb.prep_score()
                self.sb.prep_high_score()
                sleep(0.2)

    def _check_cat_vodka_collision(self):
        vodka = pygame.sprite.spritecollideany(self.cat, self.vodkas)
        if vodka:
            self.vodkas.remove(vodka)
            self.stats.score += 1
            self.sb.prep_score()
            self.settings.vodka_speed += 1
            self.settings.water_speed += 1
            if self.stats.high_score < self.stats.score:
                self.stats.high_score = self.stats.score
                self.sb.prep_high_score()






if __name__ == "__main__":
    nc = NyanCat()
    nc.run_game()
