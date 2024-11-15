from typing import List, Tuple
import pygame as pg
import csv

def load_level(name: str) -> List[Tuple[int,int]]:
    layout = []
    file_name = "game/level/levels/" + name + ".csv"
    with open(file_name, "r") as levelfile:
        reader = csv.reader(levelfile)
        for line in reader:
            coord = pg.Vector2()
            coord.x = int(line[0])
            coord.y = int(line[1])
            layout.append(coord)
    return layout
