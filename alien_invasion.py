import pygame
import game_functions as gf
from game_objects import Button, GameStats, Scoreboard, Ship
from settings import Settings
from pygame.sprite import Group


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.ai_settings = Settings()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, self.ai_settings.screen_height))
        self.play_button = Button(screen=self.screen, msg="Press to start")
        self.stats = GameStats(ai_settings=self.ai_settings)
        self.scoreboard = Scoreboard(self.ai_settings, self.screen, self.stats)
        self.ship = Ship(self.ai_settings, self.screen)
        self.bullets = Group()
        self.aliens = Group()
        gf.create_fleet(self.ai_settings, self.screen, self.ship, self.aliens)

    def reset(self):
        self.bullets = Group()
        self.aliens = Group()
        gf.create_fleet(self.ai_settings, self.screen, self.ship, self.aliens)

    def start(self):
        while True:
            self._game_step()

    def _game_step(self):
        gf.check_events(self.ai_settings, self.screen, self.stats, self.scoreboard, self.play_button, self.ship,
                        self.aliens, self.bullets)
        if self.stats.game_active:
            self.ship.update()
            gf.update_bullets(self.ai_settings, self.screen, self.stats, self.scoreboard, self.ship, self.aliens,
                              self.bullets)
            gf.update_aliens(self.ai_settings, self.screen, self.stats, self.scoreboard, self.ship, self.aliens,
                             self.bullets)
        gf.update_screen(self.ai_settings, self.screen, self.stats, self.scoreboard, self.ship, self.aliens,
                         self.bullets, self.play_button)


if __name__ == '__main__':
    Game().start()
