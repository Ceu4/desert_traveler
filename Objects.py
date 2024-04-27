import pygame


class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #создание изображения для спрайта
        self.image = pygame.image.load('graphics/Door_close.png').convert_alpha()

        #создание хитбокса для спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

