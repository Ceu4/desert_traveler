#класс для патрулирующих врагов
from defines import Constants


import pygame


import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        #создание изображения для спрайта
        self.image = pygame.Surface((32, 32))
        self.image.fill(Constants.RED)

        #начальная позиция по Х, нужна для патрулирования
        self.x_start = x
        #выбор направления начального движения
        self.direction = random.choice([-1, 1])

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #компоненты скорости по оси Х и Y
        self.x_velocity = 1
        self.y_velocity = 0

    def update(self):
        #если расстояние от начальной точки превысило 50
        #то меняем направление
        if abs(self.x_start - self.rect.x) > 50:
            self.direction *= -1

        #движение спрайта по оси Х
        self.rect.x += self.x_velocity * self.direction