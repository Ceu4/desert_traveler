#класс для игрока
from defines import Constants


import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        self.direction = pygame.math.Vector2()
        self.speed = 5

        #создание хитбокса для спрайта
        self.rect.x = x
        self.rect.y = y

        #компоненты скорости по оси X и Y
        self.x_velocity = 0
        self.y_velocity = 0

        #переменная-флаг для отслеживания в прыжке ли спрайт
        self.on_ground = False

    def update(self):
        # Обновление позиции игрока
        self.rect.x += self.x_velocity
        self.rect.y += self.y_velocity