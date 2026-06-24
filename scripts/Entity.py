from abc import ABC, abstractmethod

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from scripts.Consts import ENTITY_HEALTH, ENTITY_DAMAGE, FONT_PATH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load("./assets/images/" + name + ".png").convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def render(self, window, camera_x, player=None):
        pass

def text_game(window: Surface, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
    text_font: Font = pygame.font.Font(FONT_PATH, size=text_size)
    text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
    text_rect: Rect = text_surf.get_rect(center=text_center_pos)
    window.blit(source=text_surf, dest=text_rect)