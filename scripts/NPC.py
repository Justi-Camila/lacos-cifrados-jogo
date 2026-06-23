import pygame.transform

from scripts.Entity import Entity


class NPC(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.flip(self.surf, True, False)

    def move(self):
        pass