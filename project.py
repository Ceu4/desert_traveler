from Collectible import Collectible
from Enemy import Enemy
from Platform import Platform
from Player import Player
from defines import Constants
from Engine import Engine
from levels.Level02 import Level02
from levels.Level01 import *

####################################################################################
# Данный код представляет собой каркас для игры в жанре платформер                 #
# В нем определены: классы главного героя, врагов, собираемых предметов и платформ #
# управление с помощью клавиатуры, проверка коллизий объектов                      #
# Проект можно запустить для демонстрации функционала                              # 
####################################################################################

################################################################
#При запуске:                                                  #
# синие элементы - платформы,                                  #
# красный элемент - враг,                                      #
# зеленый элемент - игрок,                                     #
# желтый элемент - собираемый предмет                          #
#                                                              #
#Управление: стрелки клавиатуры для движения, пробел для прыжка#
################################################################

#подключние бибилиотек
import pygame

#инициализация Pygame
pygame.init()

# Добавим пару уровней для демонстрации функционала
Level_List = [Level01(), Level02()]

eng = Engine()

for l in Level_List:
    eng.load_level(l)
    eng.main_loop()
    if not(eng.win):
        break

if eng.win:
    # вывести окошко рещультатов
    print("Win!")
else:
    # вести окошко об проигрыше
    print("Loose...")

pygame.quit()