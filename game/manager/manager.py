import pygame as pg
from game.constants import *
from game.level.level import Level
from game.object.block import Block
from game.object.player import Player
from game.object.ball import Ball

class Manager():
    def __init__(self) -> None:
        self.level = 0
        self.draw_group = pg.sprite.Group()
        self.update_group = pg.sprite.Group()


    def spawn_level(self) -> None:
        # create level
        level = "level" + str(self.level)
        blocks = Level(level)
        for block in blocks.layout:
            spawn = Block(pg.Vector2(block[0],block[1]))
            self.update_group.add(spawn)
            self.draw_group.add(spawn)

        # spawn player
        player = Player(
            pg.Vector2(SCREEN_WIDTH / 2 + (PLAYER_WIDTH / 2),
                       SCREEN_HEIGHT * 0.95 - (PLAYER_HEIGHT / 2))
        )
        self.update_group.add(player)
        self.draw_group.add(player)

        # spawn ball
        ball = Ball(pg.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.75))
        self.update_group.add(ball)
        self.draw_group.add(ball)