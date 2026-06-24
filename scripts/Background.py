from scripts.Consts import ENTITY_SPEED, WIN_WIDTH
from scripts.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pass

    def render(self, window, camera_x, player=None):
        factor = ENTITY_SPEED[self.name] / 10

        tela_x = -(camera_x * factor) % WIN_WIDTH

        window.blit(self.surf, (tela_x, self.rect.y))
        window.blit(self.surf, (tela_x - WIN_WIDTH, self.rect.y))
        window.blit(self.surf, (tela_x + WIN_WIDTH, self.rect.y))