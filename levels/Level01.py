import pygame
from Platform import *
from Player import *
from Enemy import *
from Collectible import *
from Objects import *
from levels.BaseLevel import Level


class Level01(Level):
    def __init__(self):
        super().__init__()
        #создаем игрока, платформы, врагов и то, что будем собирать в игре
    def create_obj(self):
        super().create_obj()
        self.platforms_list += [Platform(50, 150, 100, 20),
                                Platform(100, 350, 100, 20),
                                HorizontalMovablePlatform(200, 250, 450, 100, 20, 1),
                                Platform(250, 170, 100, 20)]
        self.door = Door(Constants.field_size[0] - 200, Constants.field_size[1] - 25 - 60)
        self.enemies_list += [Enemy(120, 315)]
        self.collectibles_list += [Collectible(280, 135)]

