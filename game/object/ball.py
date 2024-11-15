import pygame as pg
from game.constants import *

class Ball(pg.sprite.Sprite):
    def __init__(self, position:pg.Vector2) -> None:
        super().__init__()
        self.position = position
        self.radius = BALL_RADIUS
        self.speed = BALL_SPEED // 2
        self.direction = pg.Vector2(0,1)
        self.active = False

    def update(self, delta_time) -> None:
        if self.active:
            velocity = self.direction * self.speed * delta_time
            self.position += velocity

    def draw(self, screen) -> None:
        self.rect = pg.draw.circle(screen, "red", self.position, self.radius)
