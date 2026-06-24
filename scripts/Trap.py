from scripts.Consts import WIN_WIDTH
from scripts.Entity import Entity


class Trap(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        pass

    def render(self, window, camera_x, player=None):
        tela_x = self.rect.x - camera_x

        if -self.rect.width < tela_x < WIN_WIDTH + 64:
            window.blit(self.surf, (tela_x, self.rect.y))
