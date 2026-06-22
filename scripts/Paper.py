from scripts.Entity import Entity


class Paper(Entity):

    def __init__(self, name: str, position: tuple, text: str):
        super().__init__(name, position)
        self.rect = self.surf.get_rect(topleft=position)
        self.text = text

    def move(self):
        pass
