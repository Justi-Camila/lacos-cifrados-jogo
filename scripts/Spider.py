from scripts.Entity import Entity


class Spider(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.direcao = -1

    def move(self):
        pass

    def render(self, window, camera_x, player=None):
        pass