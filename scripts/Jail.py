import pygame.transform

from scripts.Entity import Entity


class Jail(Entity):
    def __init__(self, name: str, position: tuple, text: str):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (256, 256))
        self.rect = self.surf.get_rect(topleft=position)
        self.text = text

    def move(self):
        pass