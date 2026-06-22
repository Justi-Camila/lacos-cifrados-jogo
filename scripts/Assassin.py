from scripts.Entity import Entity


class Assassin(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pass