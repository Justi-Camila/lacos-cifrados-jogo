from scripts.Consts import WIN_WIDTH, C_WHITE
from scripts.Entity import Entity, text_game


class Paper(Entity):

    def __init__(self, name: str, position: tuple, text: str):
        super().__init__(name, position)
        self.rect = self.surf.get_rect(topleft=position)
        self.text = text
        self.text = self.text

    def move(self):
        pass

    def render(self, window, camera_x, player=None):
        tela_x = self.rect.x - camera_x

        if -self.rect.width < tela_x < WIN_WIDTH + 64:
            window.blit(self.surf, (tela_x, self.rect.y))

            if player and player.rect.colliderect(self.rect):
                pos_x = tela_x + (self.rect.width / 2)
                pos_y = self.rect.y - 40
                text_game(window, 20, "Aperte E para ler", C_WHITE, (pos_x, pos_y))

