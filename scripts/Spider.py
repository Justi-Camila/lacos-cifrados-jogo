import pygame

from scripts.Consts import ENTITY_SPEED
from scripts.Entity import Entity


class Spider(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direcao = 1
        self.passos = 0
        self.sprite = self.surf

    def move(self):
        self.rect.x += ENTITY_SPEED[self.name] * self.direcao
        self.passos += 1

        if self.passos >= 200:
            self.direcao *= -1 #Inverte a direcao (1 e -1)
            self.passos = 0
            if self.direcao == -1:
                self.surf = pygame.transform.flip(self.sprite, True, False)
            else:
                self.surf = self.sprite


    def render(self, window, camera_x, player=None):
        tela_x = self.rect.x - camera_x
        window.blit(self.surf, (tela_x, self.rect.y))
