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
        self.platforms_list += [Platform(50, 50, 100, 20),
                                Platform(250, 150, 100, 20),
                                Platform(450, 250, 100, 20),
                                Platform(650, 350, 100, 20),
                                Platform(850, 450, 100, 20),
                                Platform(1050, 350, 100, 20),
                                Platform(1250, 250, 100, 20),
                                Platform(1450, 150, 100, 20),
                                Platform(1650, 50, 100, 20),
                                Platform(1050, 550, 100, 20),
                                Platform(1250, 650, 100, 20),
                                Platform(1450, 750, 100, 20),
                                Platform(1650, 850, 100, 20),
                                Platform(650, 350, 100, 20),
                                HorizontalMovablePlatform(300, 600, 50, 100, 20, 1)]


        self.door = Door(Constants.field_size[0] - 200, Constants.field_size[1] - 25 - 60)

        self.enemies_list += [Enemy(120, 315)]

        self.collectibles_list += [Collectible(280, 135)]



Platform(50, 150, 100, 20)
HorizontalMovablePlatform(200, 250, 450, 100, 20, 1)