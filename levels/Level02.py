from Collectible import Collectible, Constants
from Enemy import Constants, Enemy
from Objects import Door
from Platform import Constants, HorizontalMovablePlatform, Platform
from Player import Constants
from levels.BaseLevel import Level


class Level02(Level):
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