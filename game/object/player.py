import pygame as pg
from game.constants import *

class Player(pg.sprite.Sprite):
    def __init__(self, position:pg.Vector2) -> None:
        super().__init__()
        self.position = position
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.move_speed = PLAYER_SPEED
        self.direction = pg.Vector2()
    
    def update(self, delta_time) -> None:
        self.direction = pg.Vector2()
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
                self.direction.x = -1
        if keys[pg.K_d]:
                self.direction.x = 1
        self.position += self.direction * self.move_speed * delta_time

    def draw(self, screen) -> None:
        pg.draw.rect(screen,"blue", 
                pg.Rect(self.position.x - (self.width),
                    self.position.y - (self.height), 
                    self.width, self.height))