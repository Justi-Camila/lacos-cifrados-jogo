import pygame

from scripts.Consts import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from scripts.Level import Level
from scripts.Menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Laços Cifrados")

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, "Level", menu_return)
                level.run()

            if menu_return == MENU_OPTION[1]:
                pygame.quit()
                quit()
