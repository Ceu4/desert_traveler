#класс для платформы
from defines import Constants


import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        #создание изображения для спрайта
        self.image = pygame.Surface((width, height))
        self.image.fill(Constants.BLUE)

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class HorizontalMovablePlatform(Platform):
    def __init__(self, x1, x2, y, width, height, speed):    
        super().__init__(x1, y, width, height)
        self.x1 = x1
        self.x2 = x2
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x <= self.x1:
            self.rect.x = self.x1
            self.speed *= -1
        elif self.rect.x >= self.x2:
            self.rect.x = self.x2
            self.speed *= -1
            