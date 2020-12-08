class GameStats:

    def __init__(self, nc_game):
        self.settings = nc_game.settings
        self.reset_stats()
        self.game_active = True
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        self.cats_left = self.settings.cats_limit
        self.score = 0
        self.level = 1
        self.settings.vodka_speed = 10
        self.settings.water_speed = 10


