from scripts.Entity import Entity


class Trap(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        pass
