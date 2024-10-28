import pygame as pg
import csv

class Level():
    def __init__(self, name) -> None:
        self.name = name
        self.layout = []
        self.load_level()

    def load_level(self):
        file_name = "game/level/levels/" + self.name + ".csv"
        with open(file_name, "r") as levelfile:
            reader = csv.reader(levelfile)
            for line in reader:
                coord = pg.Vector2()
                coord.x = int(line[0])
                coord.y = int(line[1])
                self.layout.append(coord)