import pygame as pg
from game.constants import *

class Block(pg.sprite.Sprite):
    def __init__(self, position:pg.Vector2) -> None:
        super().__init__()
        self.position = position
        self.width = LEVEL_BLOCK_WIDTH
        self.height = LEVEL_BLOCK_HEIGHT
        self.health = 2


    def update(self, delta_time) -> None:
        if self.health <= 0:
            #delete
            pass

    def draw(self, screen) -> None:
        pg.draw.rect(screen,"white",
                     pg.Rect(self.position.x - (self.width),
                            self.position.y - (self.height),
                            self.width, self.height), 4)
