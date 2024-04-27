import pygame
from Platform import *
from Player import *
from Enemy import *
from Collectible import *
from Objects import *

class Level():
    def __init__(self):
        self.player = None
        self.platforms_list = []
        self.enemies_list = []
        self.collectibles_list = []
    def create_obj(self):
        self.player = Player(50, 50)
        self.platforms_list = [Platform(0, Constants.field_size[1] -25, Constants.field_size[0], 50, (0, 255, 0)),
                               Platform(0, 0, 10, Constants.field_size[1] -25),
                               Platform(Constants.field_size[0], 0, 10, Constants.field_size[1] -25),]
        self.enemies_list = []
        self.collectibles_list = []