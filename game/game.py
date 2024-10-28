import pygame as pg
from game.constants import *
from game.manager.manager import Manager

class Game():
    def __init__(self, title, res) -> None:
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode(res)
        self.title = title
        self.delta_time = 0.0
        self.is_running = True
        self.manager = Manager()

    
    def run(self) -> None:
        pg.display.set_caption(self.title)
        self.manager.spawn_level()
        while self.is_running:
            self.screen.fill("black")
            # event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                    
            # update
            for x in self.manager.update_group:
                x.update(self.delta_time)
            
            # draw
            for y in self.manager.draw_group:
                y.draw(self.screen)

            pg.display.flip()
            self.delta_time = (self.clock.tick(FRAMERATE) / 1000)
        pg.quit()