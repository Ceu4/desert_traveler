from defines import Constants
from Player import Player
from Platform import Platform, HorizontalMovablePlatform
from Enemy import Enemy
from Collectible import Collectible
from CameraGroup import CameraGroup

import pygame

class Engine:
    def __init__(self):
        #создаем экран, счетчик частоты кадров и очков
        self.screen = pygame.display.set_mode(Constants.win_size)
        self.clock = pygame.time.Clock()
        self.score = 0

        #счёт игры
        self.font = pygame.font.Font(None, 36) # создание объекта, выбор размера шрифта
        self.score_text = self.font.render("Счёт: 0", True, Constants.BLACK) # выбор цвета и текст
        self.score_rect = self.score_text.get_rect() # создание хитбокса текста
        self.score_rect.topleft = (Constants.win_size[0] // 2, 100) # расположение хитбокса\текста на экране

        #игровой цикл
        self.win = False
        self.running = True

        #создаем групп спрайтов
        self.camera_group = CameraGroup()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.collectibles = pygame.sprite.Group()

        self.door = None
        self.player = None
        self.platforms_list = []
        self.enemies_list = []
        self.collectibles_list = []
        
    #функция для проверки коллизий c платформой
    def check_collision_platforms(self, object):
        #перебираем все платформы из списка (не группы спрайтов)
        for platform in self.platforms_list:
            if object.rect.colliderect(platform.rect):
                if object.y_velocity > 0: # Если спрайт падает
                    #меняем переменную-флаг
                    object.on_ground = True
                    #ставим его поверх платформы и сбрасываем скорость по оси Y
                    object.rect.bottom = platform.rect.top
                    object.y_velocity = 0
                elif object.y_velocity < 0: # Если спрайт движется вверх
                    #ставим спрайт снизу платформы
                    object.rect.top = platform.rect.bottom
                    object.y_velocity = 0
                elif object.x_velocity > 0: # Если спрайт движется вправо
                    #ставим спрайт слева от платформы
                    object.rect.right = platform.rect.left
                elif object.x_velocity < 0: # Если спрайт движется влево
                    #ставим спрайт справа от платформы
                    object.rect.left = platform.rect.right

    #функция проверки коллизии выбранного объекта с объектами Enemies
    def check_collision_enemies(self, object):
        #running делаем видимой внутри функции чтобы было возможно
        #завершить игру
        #global running

        #в списке проверяем
        for enemy in self.enemies_list:
            #при коллизии
            if object.rect.colliderect(enemy.rect):
                #объект пропадает из всех групп спрайтов и игра заканчивается
                object.kill()
                self.running = False

    #проверка 
    def check_collision_collectibles(self, object):
        #делаем видимыми объекты для подбора в игре и очки
        #global collectibles_list
        #global score
        #если object касается collictible 
        for collectible in self.collectibles_list:
            if object.rect.colliderect(collectible.rect):
                #убираем этот объект из всех групп
                collectible.kill()
                #убираем этот объект из списка (чтобы не было проверки коллизии)
                self.collectibles_list.remove(collectible)
                #прибавляем одно очко
                self.score += 1

    def cheak_collision_door(self, object):
        if object.rect.colliderect(self.door.rect):
            self.win = True
            self.running = False

    def load_level(self, level):
        self.camera_group.empty()
        self.enemies.empty()
        self.platforms.empty()
        self.collectibles.empty()

        self.win = False
        self.running = True

        level.create_obj()

        self.enemies_list = level.enemies_list
        self.platforms_list = level.platforms_list
        self.collectibles_list = level.collectibles_list
        self.player = level.player
        self.door = level.door

        #в трех циклах добавляем объекты в соответствующие группы
        for i in self.enemies_list:
            self.camera_group.add(i)
            self.enemies.add(i)

        for i in self.platforms_list:
            self.camera_group.add(i)
            self.platforms.add(i)

        for i in self.collectibles_list:
            self.camera_group.add(i)
            self.collectibles.add(i)

        #отдельно добавляем игрока
        self.camera_group.add(self.door)
        self.camera_group.add(self.player)
        

    def update_score(self):
        #обновление счёта на экране
        self.score_text = self.font.render("Счёт: " + str(self.score), True, Constants.BLACK)
        self.screen.blit(self.score_text, self.score_rect)

    def player_control(self):
        #проверяем нажатие на клавиши для перемещения
        keys = pygame.key.get_pressed()
        self.player.x_velocity = 0
        if keys[pygame.K_LEFT]:
            self.player.x_velocity = -5
        if keys[pygame.K_RIGHT]:
            self.player.x_velocity = 5
        #условие прыжка более сложное
        if keys[pygame.K_UP] and self.player.on_ground == True:
            self.player.y_velocity = -9
            self.player.on_ground = False

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # управляем игроком
            self.player_control()

            #гравитация для игрока
            self.player.y_velocity += 0.3 

            #обновляем значения атрибутов игрока и врагов
            #self.player.update()
            #self.enemies.update()
            #self.platforms.update()
            self.camera_group.update()

            #отрисовываем фон, платформы, врагов и собираемые предметы
            self.screen.fill(Constants.WHITE)
            #self.camera_group.draw(self.screen)
            #self.enemies.draw(self.screen)
            #self.collectibles.draw(self.screen)

            self.camera_group.custom_draw(self.player)

            #проверяем все возможные коллизии
            self.check_collision_platforms(self.player)
            self.check_collision_enemies(self.player)
            self.check_collision_collectibles(self.player)
            self.cheak_collision_door(self.player)

            self.update_score()


            #обновление экрана и установка частоты кадров
            pygame.display.update()
            self.clock.tick(60)

